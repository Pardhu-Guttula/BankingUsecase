// Epic Title: Interaction History and Documentation Upload

// JavaScript code to handle file upload
document.addEventListener('DOMContentLoaded', function () {
    console.log('JavaScript loaded successfully!');
    var form = document.getElementById('upload-form');

    form.addEventListener('submit', function (event) {
        event.preventDefault();
        
        var formData = new FormData(form);
        fetch('/api/upload', {
            method: 'POST',
            body: formData,
            credentials: 'include'
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                alert('Error: ' + data.error);
            } else {
                alert('File uploaded successfully!');
            }
        })
        .catch(error => console.error('Error uploading file:', error));
    });
});