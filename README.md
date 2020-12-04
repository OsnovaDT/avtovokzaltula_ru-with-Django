# Install necessary libraries
Installation is explained for Linux Ubuntu

You need to install next:
1) Python
2) PIP
3) Django
4) Social Auth
5) Debug toolbar
6) Simple captcha
7) Psycopg2 for Postgres

For it you can print in your console next commands:
1) sudo apt-get install python3.8
2) sudo apt-get install python3-pip
3) pip3 install django
4) pip3 install social-auth-app-django
5) python -m pip3 install django-debug-toolbar
6) pip3 install  django-simple-captcha
7) pip3 install psycopg2

# Create database and database user
Here I use postgresql and will show settings for it.

Next you need to create user for database and database:
  1.  Open psql and print "create user <user_name> with password '<user_password>'"
  2.  Print 'create database <database_name> owner <user_name>'

# Add .env file
Next open this project and create .env file in your project folder (this is where the .gitignore file is).

# Set SECRET_KEY and DEBUG
Then you need to write next parameters in .env file and set values for them:
1.  SECRET_KEY (your site secret key). Here you can set any string that you want if you won't deploy this site on a remote server.
2.  DEBUG (set True if you will use this site only on your computer)
  
# Set parameters for database
3.  DB_NAME (Name your database)
4.  DB_USER (User name which can use database)
5.  DB_PASSWORD (User password for database)
6.  DB_HOST (Host which you will use for database; If DEBUG = True, set here value '127.0.0.1')

# Set parameters for sending email messages
7.  EMAIL_HOST_USER (Host user for send email messages. If DEBUG = True, set here your email address)
8.  EMAIL_HOST_PASSWORD (Password for host use, If DEBUG = True, set here your email password)

# Set parameters for VK login
9.  SOCIAL_AUTH_VK_OAUTH2_KEY (VK key for login with VK; For get this key you need to create a VK application.
You can do it here: https://vk.com/apps?act=manage)
10. SOCIAL_AUTH_VK_OAUTH2_SECRET (VK secret key for login with VK)

# Notice about Pgbouncer
If you don't use Pgbouncer, in settings.py in parameter DATABASES for 'default' database in PORT instead of 6432 set 5432

# Make and implement migrations
1.  Print 'python3 manage.py makemigrations' in your console
2.  Then print there 'python3 manage.py migrate'

# Create superuser and run server
If you use Windows, instead of 'python3' you need to use 'python' next:
  1.  Create superuser by command 'python3 manage.py createsuperuser'.
  2.  Run server by command 'python3 manage.py runserver'.

# Add data in your database
Then transfer on 'http://127.0.0.1:8000/admin', login and fill data.

# Enjoy
After this transfer on 'http://127.0.0.1:8000/index' and enjoy!
