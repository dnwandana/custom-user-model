# custom-user-model

A Django project that use a custom user model. 

Before you use this, you should probably read the documentation about [Customizing authentication in Django](https://docs.djangoproject.com/en/dev/topics/auth/customizing/).

## Quickstart

1. Clone this repository
   
    ```bash
    git clone https://github.com/dnwandana/custom-user-model.git
    ```

2. Move to the cloned repo directory   
   
   ```bash
   cd custom-user-model
   ```

3. Activate your virtualenv
   
4. Install the required dependencies
   
   ```bash
   pip install -r requirements.txt 
   ```

5. Move the directory to `custom_user_model`, run `makemigrations` and `migrate` command
   
   ```bash
   cd custom_user_model
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Create a `superuser`
   
   Run the command below, and you'll be prompted an email, username, first & last name, and also password.

   ```bash
   python manage.py createsuperuser
   ```

7. Run the app and check the admin site

   ```bash
   python manage.py runserver
   ```