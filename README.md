# FixtureGenerator
App used for generating tournament fixture automatically
# Installation

To install this in local server after downloading and extracting the repo.

1. Create a python 3.7 virtualenv and activate
2. Then run
  ```commandline
   cd FixtureGenerator
   pip install -r requirements.txt
   ```
   
## Initialize database

```commandline
python manage.py makemigration
python manage.py migrate
```
## Create super user
```commandline
python manage.py createsuperuser
```
Enter necessary details for creating super user. This user can be used for 
login into admin panel.

## Running the local server

   ```commandline
    python manage.py runserver
   ```
### Using app

1. Can register 10 teams
2. After creating the 10th team it automatically generate
fixture.
3. Can access the fixture in the schedule url
4. Admin can login and update the fixture values.
5. Admin panel is available only for logged in user.