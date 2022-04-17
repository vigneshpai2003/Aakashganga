rm db.sqlite3
python manage.py makemigrations
python manage.py migrate
echo 'from scripts import *; init()' | python manage.py shell
python manage.py runserver