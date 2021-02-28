# enlighten-me--SpaceJam

### requirements
- python3.9
- pipenv 
  - Get it by running **pip install pipenv**

### Setup Guide
##### 1.Cloning the repo
- Clone the repo or fork it and then clone from your profile.
- Cd into **project folder**

##### 2.Pipenv and migrations
- Go to directory where the pipfile is and run **pipenv sync --dev**
- Activate pipenv by doing **pipenv shell**
- Go into the src folder where the manage.py sits and run the following:
  - **python manage.py migrate**
  
##### 3.Super user and Profile
- Create super user by doing the following:
  - **python manage.py createsuperuser** (optional)
  
##### 5.Running the server
- Go the folder where your manage.py sits and the following commands to run the server:
  - **python manage.py runserver**
