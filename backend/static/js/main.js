// Epic Title: Core Banking System Integration

// JavaScript code to handle API interactions and display data
document.addEventListener('DOMContentLoaded', function () {
    console.log('JavaScript loaded successfully!');

    // Function to fetch external data
    function fetchExternalData() {
        fetch('/api/external-data', {
            headers: {
                'x-access-token': localStorage.getItem('access_token')
            }
        })
        .then(response => response.json())
        .then(data => {
            console.log('Data fetched:', data);
            // Handle and display data as needed
        })
        .catch(error => console.error('Error fetching data:', error));
    }

    // Fetch data on page load
    fetchExternalData();
});