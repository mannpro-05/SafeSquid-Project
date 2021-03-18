function handleFormSubmit(event) {
  event.preventDefault();
  const date = document.getElementById('startdate').value;
  const time = document.getElementById('starttime').value;
  const data = new FormData(event.target);
  const formJSON = Object.fromEntries(data.entries());

  // for multi-selects, we need special handling
  formJSON.fields = data.getAll('fields');
  if (date !== '' && document.getElementById('enddate').value === '' ){
        alert("Please fill the End date form")
    }
  if (time !== '' && document.getElementById('endtime').value === ''){
        alert("Please fill the End time form")
    }
    else{
        var table = $('#myTable').DataTable();
        table.destroy();

        $.ajax({
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify(formJSON),
        dataType: 'json',
        url: 'http://127.0.0.1:5000/returnData',

    })
        .done(function (data){
            console.log(data.data.DATA);
            console.log(data.data.COLUMNS,"hello");
            $(document).ready( function() {
                $('#myTable').empty();
            $('#myTable').dataTable({
                "columnDefs": [
            {"className": "dt-center", "targets": "_all"}
            ],
                "data": data.data.DATA,
                "columns": data.data.COLUMNS,
                "bDestroy": true
            });
        });})
  const results = document.querySelector('.results pre');
  results.innerText = JSON.stringify(formJSON, null, 2);
  }

}

function hello(event){
    event.preventDefault();
    const data = new FormData(event.target);
    const formJSON = Object.fromEntries(data.entries());
    const email = document.getElementById('mailUsername').value;
    const pass = document.getElementById('password').value;
    const cpass = document.getElementById('confirm_password').value;
    if(email !== ""){
        console.log(JSON.stringify(formJSON));
        if(pass === "" || cpass === "")
        {
            alert("Password field/fields is/are empty!!");
        }
        else if(pass.localeCompare(cpass)){
            alert("passwords do not match!!!");
        }
        else{
            delete formJSON["CONFIRM_MAIL_PASSWORD"];
            $.ajax({
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify(formJSON),
        dataType: 'json',
        url: 'http://127.0.0.1:5000/mailConfig',

    })
        .done(function (data) {
                document.getElementById('opt').innerHTML = data.message;
            })
        }
    }
    else{
        delete formJSON["CONFIRM_MAIL_PASSWORD"];
            $.ajax({
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify(formJSON),
        dataType: 'json',
        url: 'http://127.0.0.1:5000/mailConfig',

    })
        .done(function (data) {
                document.getElementById('opt').innerHTML = data.message;
            })
        }
    const results = document.querySelector('.results pre');
    results.innerText = JSON.stringify(formJSON, null, 2);


}



const form = document.querySelector('.contact-form');
const test = document.querySelector('.config-form');
if (test){
    test.addEventListener('submit', hello)
}
else{
    form.addEventListener('submit', handleFormSubmit);
}
