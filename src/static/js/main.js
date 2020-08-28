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
        task: '',
        tasks:[]
       }
    },
    async created() {
        var response =await fetch('http://127.0.0.1:8000/services/api/service_provider/')
        this.tasks = await response.json();
    },
    methods: {
        contactPr(id){
            var vm = this;

            sendRequest('' + id + '/subscribe_post/','post')
            .then(function(response){
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

