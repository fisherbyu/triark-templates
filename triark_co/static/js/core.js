// function OutputCode(content) {
//     output = HEADER + '\n' + content + '\n' + SIGNATURE + '\n' + FOOTER;
//     navigator.clipboard.writeText(output);
// }

function copy(valForm) {
    navigator.clipboard.writeText(valForm.val.value);
};

// function send(valForm) {
//     // Send a POST request with the form data
//   fetch('/render', {
//     method: 'POST',
//     body: valForm
//   })
//   .then(response => {
//     // Handle the response here
//     console.log('Form submitted successfully');
//   })
//   .catch(error => {
//     // Handle any errors here
//     console.error('Error submitting form', error);
//   });
// }

function send(valForm) {
   var target = document.getElementById("render");
   target.innerHTML = valForm.val.value;
};