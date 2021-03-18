$(document).ready(function(){
    const test = {"page":"queryingPage", "dataBase":"queryDatabase.csv"};
    const data = new FormData(document.getElementById('queryForm'));
    const formJSON = Object.fromEntries(data.entries());
    formJSON.fields = data.getAll('fields');
    $.ajax({
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify(formJSON),
        dataType: 'json',
        url: 'http://127.0.0.1:5000/displayDefault',
    })
        .done(function (data){
            $('#myTable').empty();
            $('#myTable').dataTable({
                "columnDefs": [
            {"className": "dt-center", "targets": "_all"}
            ],
                "data": data.data.DATA,
                "columns": data.data.COLUMNS,
                "bDestroy": true
            });
        })
});