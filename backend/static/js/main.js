// Epic Title: Interaction History and Documentation Upload

// JavaScript code to handle saving and resuming application progress
document.addEventListener('DOMContentLoaded', function () {
    console.log('JavaScript loaded successfully!');

    var form = document.getElementById('application-form');
    var saveButton = document.getElementById('save-progress');

    // Function to save progress
    function saveProgress(event) {
        event.preventDefault();

        var formData = new FormData(form);
        var jsonObject = {};
        formData.forEach((value, key) => {
            jsonObject[key] = value;
        });

        fetch('/api/save-progress', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ form_data: jsonObject }),
            credentials: 'include'
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                alert('Error: ' + data.error);
            } else {
                alert('Progress saved successfully!');
            }
        })
        .catch(error => console.error('Error saving progress:', error));
    }

    // Function to retrieve progress
    function retrieveProgress() {
        fetch('/api/retrieve-progress', {credentials: 'include'})
            .then(response => response.json())
            .then(data => {
                if (data[0]) {
                    const formData = data[0].form_data;
                    Object.keys(formData).forEach(key => {
                        form.elements[key].value = formData[key];
                    });
                }
            })
            .catch(error => console.error('Error retrieving progress:', error));
    }

    // Add event listeners
    saveButton.addEventListener('click', saveProgress);
    window.addEventListener('load', retrieveProgress);
});