# Learning Log

Learning from [this](https://www.youtube.com/playlist?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p) tutorial.



## 1. Getting Started
1. `django-admin startproject Learning_Django`: Created the project directory, and necessary files.
1. `py manage.py runserver`: Started the server. PyCharm also has a *Django Server* configuration which lets to specify a host and a port.



## 2. Applications and Routes
1. In Django, a single project can have multiple apps.
1. `py manage.py startapp blog`: Started a new app named *blog*.
1. Inside `blog\views.py`, created a function to receive and response to an http request.
1. Created a new file `blogs\urls.py`, which is almost similar to the initial `urls.py`.
1. Included `blogs.urls` in the path of initial `urls.py`.
1. Created a new function in `blog\views.py` to handle the *about page* of blog.
1. Added that path in `blog\urls.py`.
1. Learnt to change the path patterns in main `urls.py` to change how the site navigates.



## 3. Templates
1. Created a subdirectory `templates` in `blog` directory (which, by the way, we are also calling our *blog app*).
1. Created sub-subdirectory `blog` in `blog\templates`. This redundancy they say is just a Django convention.
1. Created `.html` pages in `blog\templates\blog`.