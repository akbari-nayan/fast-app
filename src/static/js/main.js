function sendRequest(url, method, data) {
    var r = axios({
       method:method,
       url:url,
       data:data,
       xsrfCookieName: 'csrftoken',
       xsrfHeaderName:'X-CSRFToken',
       headers: {
           'X-Requested-With':'XMLHttpRequest'
       }      
   })
   return r
}
var app = new Vue({
    el:'#app',// id of div
    data () {
       return{
        task:{
            'postId': '',
          },
           tasks:[]
       }
    },
    async created() {
        var response =await fetch('http://127.0.0.1:8000/services/api/posts/')
        this.tasks = await response.json();
    },
    methods: {
        contactMe(){
            var vm = this;
            console.log(this.task)
            // var formData = this.FormData();
            var postId = vm.task; 
            // console.log(postId)
            sendRequest('/services/','post',postId)
            .then(function(response){
                    // vm.task =
            })
        }
    }
})


var serviceApp = new Vue({
    el:'#serviceApp',// id of div
    data () {
       return{
           tasks:[]
       }
    },
    async created() {
        var response =await fetch('http://127.0.0.1:8000/services/api/service_provider/')
        this.tasks = await response.json();
    }
})



// var app = new Vue({
//     el:'#app',// id of div
//     delimiters: ['[[', ']]'],
//     data: {
//         task:'',
//         tasks:[
//             {content : 'hyy'}
//         ]
//     },
//     created() {
//         var vm = this;
//         // axios('{% static_cdn-media_root %}')
//         var r = sendRequest('','get')
//             .then(function(response){
//                 vm.tasks = response.data.tasks;
//             })
//     },
//     methods: {
//         contactMe(){
//             var vm = this;
//             // var formData = this.FormData();
//             var postId = vm.task; 
//             // console.log(postId)
//             sendRequest('/services/','post',postId)
//             .then(function(response){
//                     vm.task =
//             })
//         }
//     }
// })