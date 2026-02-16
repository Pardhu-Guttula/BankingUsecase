// Epic Title: Role-based Access Control

document.addEventListener('DOMContentLoaded', function () {
    console.log('JavaScript loaded successfully!');

    function createPermission() {
        const permissionName = document.getElementById('permission-name').value;
        const permissionDescription = document.getElementById('permission-description').value;

        fetch('/api/permissions', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'x-access-token': localStorage.getItem('access_token')
            },
            body: JSON.stringify({ name: permissionName, description: permissionDescription })
        })
        .then(response => response.json())
        .then(data => {
            console.log('Permission created:', data);
            alert('Permission created successfully!');
        })
        .catch(error => console.error('Error creating permission:', error));
    }

    // Attach create permission function to the button click event
    document.getElementById('create-permission-button').addEventListener('click', createPermission);
});