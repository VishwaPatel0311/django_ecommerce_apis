# steps to run the code
```
git clone https://github.com/VishwaPatel0311/django_ecommerce_apis.git
```
```
cd django_ecommerce_apis
```
* create virtualenv
```
virtualenv venv
```
* setup virtualenv
```
source venv/bin/activate
```
* install requirements
```
pip install -r requirements.txt
```
* make migrations
```
python manage.py makemigrations
```
* migrate the database
```
python manage.py migrate
```
* create superuser
```
python manage.py createsuperuser
```
* to run the code
```
python manage.py runserver
```
* admin superuser credentials
```
username: vishwa
password: Admin@2023
```