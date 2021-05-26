$('form').on('submit', event => {
  event.preventDefault();
  let body = {
    form: $('form').serialize()
  };
  fetch(event.target.action, {
    method: event.target.method,
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(body)
  })
    .then(response => response.text())
    .then(data => console.log(JSON.parse(data)))
    .catch(error => console.warn(error));
});
