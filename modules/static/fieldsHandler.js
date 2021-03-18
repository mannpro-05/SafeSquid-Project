function handleFormSubmit(event) {
  event.preventDefault();

  const data = new FormData(event.target);
  const formJSON = Object.fromEntries(data.entries());

  // for multi-selects, we need special handling
   $.ajax({
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify(formJSON),
            dataType: 'json',
            url: 'http://127.0.0.1:5000/save',

        })
            .done(function (data) {
                document.getElementById('opt').innerHTML = data.message;
            })
        document.getElementById('input-form').reset();
}

const form = document.querySelector('.inp-form');
form.addEventListener('submit', handleFormSubmit);