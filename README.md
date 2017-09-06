# ft_companysee
A little Django project for technical interview

## Installation
```
# Clone the project
git clone https://github.com/avallete/ft_companysee.git
cd ft_companysee

# Set-up virtualenv for the project
virtualenv --system-site-packages -p python2.7 venv; source venv/bin/activate
pip install -r requirements.txt

# Set-up database
./manage.py makemigrations
./manage.py migrate
./manage.py populate_db

# Run dev server
./manage.py runserver
```
