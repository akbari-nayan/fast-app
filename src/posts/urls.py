from rest_framework.routers import DefaultRouter


from django.urls import path,include
from .views import ServiceFormView,PostCreateView,PostList,Subscribe



router = DefaultRouter()
router.register(r'service_provider',PostList,basename='servise-provider')
app_name = 'posts'

urlpatterns = [
    path('api/',include(router.urls)),
    path('',ServiceFormView.as_view(),name='services-list-view'),
    path('add',PostCreateView.as_view(),name='add-new-post'),
    path('<str:id>/subscribe_post/',Subscribe.as_view())
]