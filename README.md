# Dynamic Django Base

## INTRO
This base project will save you time updating urls in numerous places. You can maintain site pages and django app information in one place - the admin!

**A base starter project - pages and website sections can appear dynamically anywhere you like on your website:**

**Created in the admin:**
- **Flat Pages** 
  - Create pages such as 'about us'.
  - Dynamically appear in the navbar, sidebar and footer.
- **Website sections** 
  - Title, text, url and image of any django apps you create - usable anywhere on your website with by loading a template tag (see basehtml app).
  - Dynamically appear on the homepage as a grid and in navbar menu.
  - Dynamically appear under category headings in the sidebar and footer.

## FEATURES

Completely adpatable, the base project consists of:

- Base HTML
- Flat Pages
- Website Sections
- Homepage

## FEATURES

For these demo images, I created two flat pages and three website sections that appear under two website categories:

----

![Base Sidebar](https://github.com/richardgourley/dynamic-django-base/blob/main/base_html_sidebar.png)

----

![Base Full width](https://github.com/richardgourley/dynamic-django-base/blob/main/base_html_fullwidth.png)

## GETTING STARTED

- This project is development ready NOT production ready. (See docs for deploying a Django project)
- All project and app files you will need to get started with this project are included in the 'dynamicdjangobase' directory.
- **NOTE: If you are new to Django, some of these files will be created automatically when you start a Django project.** This is normal.
- **NOTE: Other directories will be created such as migrations (when you make changes to models) and pycache (caches python files).** Again this is expected.
- The project directory 'dynamicdjangobase' will be created automatically inside your virtual environment when you run django startapp.

**STEPS**

- Setup a directory where you will place the project.
- In the Linux or Mac terminal or Windows terminal (Start -> Windows System -> Command Prompt) navigate to the directory.

- Setup a virtual environment (presuming you have Python installed on your system)...

- Activate the virtual environment - (dynamicdjangobase) must appear at the start of the line if activated correctly.

```
LINUX/ MAC: source bin/activate
WINDOWS: Scripts\activate
```

- Install django

```
pip install django
```

- Install tinmyce-django - text editor for flat pages

```
pip install django-tinymce
```

- Install pillow for images - Imaging Library adds image processing capabilities to your Python interpreter.

```
pip install Pillow
```

- Install python-decouple

```
pip install python-decouple
```

- Start django project (you can call it anything you prefer)

```
django-admin startproject dynamicdjangobase
```
- Start all of the apps included in the project - app directories will be created automatically...

```
django-admin startapp basehtml
django-admin startapp flatpages
django-admin startapp homepage
django-admin startapp websitesections
```
- When you have copied over all of the files from this repo to your app directories, migrate the changes to the database - (inserts tables for the models)
- Make sure you are in the directory 'dynamicdjangobase' with the file 'manage.py' inside...

```
python manage.py makemigrations
python manage.py migrate
```
- Setup a .env file in the same project level directory that contains 'manage.py'
- Copy the secret key variable directly (without ' ') from the project 'settings.py' file like this...

```
.env file....

SECRET_KEY=the_secret_key_number_in_settings.py
DEBUG=True
```
- Look at how SECRET_KEY and DEBUG are hidden by python-decouple in the 'settings.py' file.
- You can add any database names and passwords to your .env file in production.

There are other django libraries available for working with Bootstrap... check out the docs for:
- django-compressor (for Bootstrap)
- django-libsass (for Bootstrap)



