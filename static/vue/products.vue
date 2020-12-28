var vueapp = new Vue({
    delimiters: ['[[', ']]'],
    el: '#app',
    data: {
        products: [],
    },

    created () {
        this.api_call('/api/products/?format=json','GET')
        .then(response => {
            this.init_products(response.data)
        })
    },
    methods: {

        init_products: function(event_list){
            this.products = []
            event_list.forEach(item => {
                this.products.push(item);
            });
        },

        show_error_message(HTTP_CODE,message){
            error = ''.concat("Code: ",HTTP_CODE,' ',message)
            this.err_messages.push(error)
        },
        api_call: function(url,method,json_data="{}"){
            resp = this.async_api_call_axios(url,method,json_data)
            resp.then(e => {
                this.err_messages = []
            });
            resp.catch(error => {
                this.show_error_message(error.response.status,error.response.data['message'])
            });
            resp.finally(() => {
                this.loading = false;
            });
            return resp
        },
        async_api_call_axios: async(url,method,json_data) =>{
            return await axios({
                url: url,
                method: method,
                data: json_data,
                proxy: '',
                headers: {'Content-Type':'application/json','X-CSRFToken': Cookies.get('csrftoken')}
            });
        }
    }

});