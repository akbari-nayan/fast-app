from django.shortcuts import render, redirect
from django.views.generic import  FormView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post, Subscription
from service_pr.models import Client, ServiceProvider
from .forms import PostModelForm
from users.models import CustomUser
from django.core.mail import send_mail
from .tasks import sleepy, send_email_task
from .serializers import PostSerializer
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated




# Create your views here.



class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'post_id'



class PostList(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    permissions_classes = (IsAuthenticated,)

    def get_queryset(self, username=None):
        user = ServiceProvider.objects.get(name=self.request.user)
        print(user) 
        queryset = Post.objects.filter(author=user)
        return queryset


class PostCreateView(FormView):
    model = Post
    template_name = "posts/add_services.html"
    form_class = PostModelForm
    success_url = reverse_lazy('posts:services-list-view')

    def form_valid(self, form):
        request = self.request
        prdvdr = ServiceProvider.objects.get(name=request.user)
        form = PostModelForm(request.POST, request.FILES)
        inst = form.save(commit=False)
        inst.author = prdvdr
        inst.save()
        return super().form_valid(form)


class ServiceFormView(LoginRequiredMixin, APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'posts/posts_list.html'


    def get(self, request):
        if (self.request.user.is_client):
            return render(request,'posts/posts_list.html')
        elif (self.request.user.is_service_provider):
            servic_prvdr = ServiceProvider.objects.get(name=self.request.user)
        return render(request,'posts/posts_list.html',{'service_provider':servic_prvdr})


    def post(self, request):
        client_ = CustomUser.objects.get(username=self.request.user)
        request = self.request
        postid = request.GET.get('postId')
        post_read = Post.objects.get(pk=postid)
        srpvdr_ = CustomUser.objects.get(username=post_read.author)
        subject = 'new service'
        message = f'{client_} want your {post_read.service_name} service.'
        To = srpvdr_.email
        From = client_.email
        send_email_task(subject, message, From, To)
        return redirect('posts:services-list-view')

