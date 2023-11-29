# Online_food_delivery_management-system
A complete web-based infrastructure called the Online Food Delivery Management System was created to make ordering, delivering, and managing meal deliveries easier. Customers may browse and order from several restaurants, examine menus, and securely pay using this system.

## Installation Steps

1. Create a virtual environment:
    ```
    python3 -m venv venv
    ```

2. Activate the virtual environment:
    - On Windows:
        ```
        .\venv\Scripts\activate
        ```
    - On Unix or MacOS:
        ```
        source venv/bin/activate
        ```

3. Install the dependencies from the requirements.txt file:
    ```
    pip install -r requirements.txt
    ```

4. Create a database in MySQL using phpMyAdmin.

5. Run the migration command:
    ```
    python manage.py migrate
    ```

6. Start the server:
    ```
    python manage.py runserver
    ```
