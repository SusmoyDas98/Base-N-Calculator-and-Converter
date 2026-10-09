const app = Vue.createApp(
    {
        data(){
            return {
                from_base : 2,
                to_base : 2,
                // swap_not: "Swap Bases",
                swap_done: "Swapped !!!",
                swap_status: "Swap Bases",
            }
        },
        methods:{
            swapBases(){
                let temp = this.from_base;
                this.from_base = this.to_base;
                 this.to_base = temp;
                 this.swap_status = this.swap_done;
                 setTimeout(function(){
                    this.swap_status = "Swap Bases";
                 }.bind(this),200);
                 
            }
        }
    }
)

app.mount("#app")