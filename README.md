Steps taken to set up this project:

(terminal)
1. django-admin startproject Finetech
2. django-admin startapp finetech
3. python3 manage.py migrate (used mysqlite3)
4. python3 manage.py createsuperuser
5. python3 manage.py runserver (to test run project)

(finetech)
1. added 'receipting' app to apps in settings.py
2. included receipting urls to project urls


(receipting)
1. created urls.py and forms.py
2. created model Receipt and ran migrations
3. created templates and static folders for html and css pages
4. started working on views

(tests)
1. write tests for both models and views 
2. run python3 manage.py test
