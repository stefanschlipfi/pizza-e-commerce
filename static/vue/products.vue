var vueapp = new Vue({
    delimiters: ['[[', ']]'],
    el: '#products-vue-app',
    data: {
        products: [],
        err_messages: [],
        filters: {'All':'','Pizza':'Pizza','Pasta':'Pasta','Salate':'Salate'},
        active_filter: 'All',
        loading: true,
    },

    created () {
       this.load_products()
    },
    methods: {

        load_products: function(){
            this.api_call('/api/products/?format=json&category=' + this.filters[this.active_filter],'GET')
            .then(response => {
                this.init_products(response.data)
            })
        },
        init_products: function(event_list){
            this.products = []
            event_list.forEach(item => {
                this.products.push(item);
            });
        },
        show_product_detail: function(product){
            alert("Show detail: " + product.name)
        },
        add_to_card: function(product){
            alert(product.name)
        },
        select_filter: function(){
            var dropdown = document.getElementById('filter_dropdown')
            this.active_filter = dropdown.options[dropdown.selectedIndex].text;
            this.load_products()
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
            this.loading = true;
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