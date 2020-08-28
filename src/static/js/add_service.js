var addService = new Vue({
   el:'#addService',// id of div
   data () {
      return{
          service:{
            'service_name': '',
            'content'     : '',
          },
          services:[]
      }
   },

   async created() {
       var response =await fetch('http://127.0.0.1:8000/services/api/posts/')
       this.services = await response.json();
   },

   methods:{
        async addService(){
            var response =await fetch('http://127.0.0.1:8000/services/api/service_provider/',{
                method: 'post',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(this.service)
            });
            this.services.push(await response.json()) 
        }
   }

})
