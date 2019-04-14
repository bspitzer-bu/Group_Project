# Group project

## Setup

### Local

#### Initially Setup
1. `git clone https://github.com/Amanda-Wakefield/Group_Project.git`
2. `pip install -r requirements/development.txt`
3. `python manage.py migrate`
4. `python manage.py runserver`

#### After Database Modification
1. `python manage.py makemigrations`
2. `python manage.py migrate`
3. `python manage.py runserver`

#### Create Superuser
1. `python manage.py createsuperuser`

### Docker
1. `docker run -d -p 8000:8000 awakefield/group_project`
