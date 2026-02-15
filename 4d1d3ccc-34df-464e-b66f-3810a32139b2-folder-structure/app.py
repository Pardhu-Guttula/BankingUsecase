# Epic Title: Role-based Access Control

from backend.app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)


# File 11: Schema Definition for Permissions Table in database/22_create_permissions_table.sql