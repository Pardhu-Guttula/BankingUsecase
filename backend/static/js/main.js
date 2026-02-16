// Epic Title: Role-based Access Control

document.addEventListener('DOMContentLoaded', function () {
    console.log('JavaScript loaded successfully!');

    function createRole() {
        const roleName = document.getElementById('role-name').value;
        const roleDescription = document.getElementById('role-description').value;

        fetch('/api/roles', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'x-access-token': localStorage.getItem('access_token')
            },
            body: JSON.stringify({ name: roleName, description: roleDescription })
        })
        .then(response => response.json())
        .then(data => {
            console.log('Role created:', data);
            alert('Role created successfully!');
        })
        .catch(error => console.error('Error creating role:', error));
    }

    // Attach create role function to the button click event
    document.getElementById('create-role-button').addEventListener('click', createRole);
});