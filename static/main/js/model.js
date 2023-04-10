$(document).ready( function () {
    $("#id_mark_model").html('');
    
    $("#id_mark_model").append(`
        <option value="">Выберите марку</option>
    `)
    $("#id_marks").change(function (event) {
        var mark_from_form = event.target.value;
        $.ajax({
            url: `/api/models?mark=${mark_from_form}`,
            type: 'get',
            success: function (data){
                $("#id_mark_model").html('');
                $("#id_mark_model").append(`
                        <option value="" disabled>Выберите модель</option>
                    `)
                data.forEach(element => {
                    $("#id_mark_model").append(`
                        <option value="${element.id}">${element.name}</option>
                    `);
                    })
                }
            });
    });

    // $.ajax({
    //   url: `/api/models?mark=${}`,
    //   type: 'get',
    //   success: function (data){
        
    //   }
    // });
});