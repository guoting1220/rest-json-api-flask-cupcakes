$(async function () {
    const BASE_URL = "http://127.0.0.1:5000/api";

    function generateCupcakeHTML(cupcake) {
        $(`
            <div id=${cupcake.id} class="col mb-4">
                <div class="card">
                    <img src=${cupcake.image} class="card-img-top" alt="No Picture">
                    <div class="card-body">                    
                        <p class="card-text">
                            <b>Flavor: </b> ${cupcake.flavor}       
                        </p>
                        <p class="card-text">
                            <b>Size: </b> ${cupcake.size}
                        </p>
                        <p class="card-text">
                            <b>Rating: </b> ${cupcake.rating}
                        </p>
                        <a class="delete-btn btn btn-sm btn-info">Delete</a>
                    </div>
                </div>
            </div>
        `).appendTo($("#cupcake-list"))
    }

    async function showCupcakeList() {
        const res = await axios.get(`${BASE_URL}/cupcakes`);
        // const res = await axios.get("http://127.0.0.1:5000/api/cupcakes");
     
        for (let cake of res.data.cupcakes) {            
            generateCupcakeHTML(cake);
        }
    }

    $("#add-btn").on('click', async function(e){
        e.preventDefault();
        let flavor = $("#flavor").val();
        let size = $("#size").val();
        let rating = $("#rating").val();
        let image = $("#image").val();

        const res = await axios.post(`${BASE_URL}/cupcakes`, {
            flavor, 
            size,
            rating,
            image
        })

        generateCupcakeHTML(res.data.cupcake);     
        // doesn't work?  
        // $("#add-form").reset();  
        $("#add-form").trigger("reset");       
    });


    $("#cupcake-list").on('click', '.delete-btn', async function(e){
        const $to_be_deleted = $(e.target).parent().parent().parent();
        const cake_id = $to_be_deleted.attr("id");

        await axios.delete(`${BASE_URL}/cupcakes/${cake_id}`);

        $to_be_deleted.remove();
    })


    showCupcakeList();
});