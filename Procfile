web: gunicorn cv_main.wsgi:application --log-file - --log-level debug
python manage.py collectstatic --noinput
python manage.py makemigrations cvApiReviews
python manage.py makemigrations cvApp
python manage.py migrate