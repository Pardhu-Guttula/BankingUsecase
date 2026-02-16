// Epic Title: Interaction History and Documentation Upload

// JavaScript code to handle fetching and displaying interaction history
document.addEventListener('DOMContentLoaded', function () {
    console.log('JavaScript loaded successfully!');
    var socket = io.connect('http://' + document.domain + ':' + location.port);
    
    // Function to fetch interaction history
    function fetchInteractionHistory() {
        fetch('/api/interaction-history', {credentials: 'include'})
            .then(response => response.json())
            .then(data => {
                const historyDiv = document.getElementById('interaction-history');
                historyDiv.innerHTML = '';
                data.forEach(interaction => {
                    const interactionDiv = document.createElement('div');
                    interactionDiv.classList.add('interaction-record');
                    interactionDiv.textContent = `${interaction.timestamp}: ${interaction.action}`;
                    historyDiv.appendChild(interactionDiv);
                });
            })
            .catch(error => console.error('Error fetching interaction history:', error));
    }
    
    // Fetch interaction history on page load
    fetchInteractionHistory();
});