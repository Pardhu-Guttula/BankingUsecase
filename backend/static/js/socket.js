# Epic Title: Real-time Status Updates

document.addEventListener("DOMContentLoaded", () => {
    const socket = io();

    socket.on('connect', () => {
        console.log('Connected to real-time updates');
    });

    socket.on(`user_${USER_ID}`, (message) => {
        alert(`New update: ${message}`);
    });
});


# File 4: Base HTML Template Modification to Include SocketIO Script in authentication/templates/base.html