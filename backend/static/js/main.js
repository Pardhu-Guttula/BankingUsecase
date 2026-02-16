// Epic Title: Real-time Status Updates and Notifications

// JavaScript code to handle any interactive elements for consistency
document.addEventListener('DOMContentLoaded', function () {
    console.log('JavaScript loaded successfully!');
    var socket = io.connect('http://' + document.domain + ':' + location.port);

    socket.on('status_update', function(msg) {
        var statusElement = document.getElementById("status-" + msg.request_id);
        if (statusElement) {
            statusElement.textContent = "Status: " + msg.status;
        } else {
            console.log("Status element for request " + msg.request_id + " not found.");
        }
        showNotification(msg.status, msg.request_id);
    });

    function showNotification(message, requestId) {
        const notificationsDiv = document.getElementById("notifications");
        const notification = document.createElement("div");
        notification.classList.add("notifications");
        notification.textContent = `Request ${requestId}: ${message}`;

        notificationsDiv.appendChild(notification);

        setTimeout(() => {
            notification.remove();
        }, 5000);
    }
});