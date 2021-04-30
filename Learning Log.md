# Learning Log

Learning from [this](https://www.youtube.com/playlist?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p) tutorial of Corey Schafer.



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
1. In main `settings.py` registered (added) `blog.apps.BlogConfig` as and installed app. **This is better to do immediately after creating a new app.**
1. In `blog\views.py` rendered html pages instead of direct html response string.
1. Created some dummy data in `blog\views`. The data is an array of json objects, if I'm not mistaken.
1. Created a *dictionary* named `context` in `home(request)` function of `blog\views`.
1. Did some magical loop codes in `home.html`. Don't know what they are called actually.
1. Used if-else condition to change the title of html pages!
1. Added a base html page.
1. Added Bootstrap css and js to that base html.
1. Added sample code to base html.
1. Created `blog\static`, then `blog\static\blog`, as per convention.
1. Added sample `main.css` file in that static directory.
1. Loaded and linked that css in base html.
1. Added custom code to `home.html`.
1. Soft-coded url route in base html. This feels good!



## 4. Admin Page
1. `py manage.py makemigrations`: Creates the database table, or has something to do with it.
1. `py manage.py migrate`: After the previous command, we have to run this. ¯\\\_(ツ)_/¯
1. Only then can we use `py manage.py createsuperuser` to create a...super user, of course.
1. Learnt to work with admin page of Django. This feels awesome!



## 5. Database and Migrations
1. Created a *Post* class in `models.py`.
1. Then ran `py manage.py makemigrations` and `py manage.py migrate` consecutively for reasons which I don't fully understand.
1. *Saw* how he was using shell to query stuffs. Added a post with him.
1. Formatted date style.
1. Now comes the **crucial part**. Registered the *Post* model (which was created in shell) in `blogs\admin.py`, so that it would be shown in Django admin panel. And it shows, and it feels awesome again!



## 6. User Registration
1. Created a new app using `py manage.py startapp users`.
1. Registered it in `settings.py`.
1. Django provides its own user registration form! Wow!
1. Added a `register.html` page.
1. Updated `urlpatterns` in a different way.
1. Responded to POSTs in registration form.
1. Created `forms.py` to customize registration form.
1. Used `django-crispy-forms` package to decorate the registration form.



## 7. Login and Logout System
1. Created login and logout views, and pages.
1. Added `LOGIN_REDIRECT_URL`.
1. Updated login-logout stuffs...
1. Added profile page.
1. Required login to view profile page.



## 8. User Profile and Picture
1. Created Profile model in *users* app.
1. Ran `py manage.py makemigrations` and `py manage.py migrate`.
1. **Registered** this model in `users\admin.py`.
1. **Just found out that Python Console within Pycharm is *really* beautiful to handle Django Shell commands!**
1. Added custom `MEDIA_ROOT` and `MEDIA_URL`.
1. Reorganized profile page.
1. Initiated profile when a new user is created.



## 9. Update User Profile
1. Nothing made sense here, but everything works with a beauty.
1. Profile picture shown in home page.



## 10. Create, Update, and Delete Posts
1. Did some stuffs which I don't understand and changed the ordering of posts with a magical command.
1. Added functionality to view individual posts.
1. Post links in home page now take us to the destination.
1. Added functionality to create a post, and then redirect user to that post.
1. Login is now required to go to the creat post page.
1. Added functionality to update post—with a massive flaw—anyone can edit anybody's post! :3
1. None can update others' post now!
1. Added functionality to delete post. Django feels real good now.
1. Now user can find create, update and delete button where necessary.



## 11. Pagination
1. Added basic pagination where each page has 2 posts.
