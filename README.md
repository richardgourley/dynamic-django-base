# Dynamic Django Base

## INTRO
This base project will save you time updating urls in numerous places. You can maintain site pages and django app information in one place - the admin!

**A base starter project - pages and website sections can appear dynamically anywhere you like on your website:**

**Created in the admin:**
- **Flat Pages** 
  - Create pages such as 'about us'.
  - Dynamically appear in the navbar, sidebar and footer.
- **Website sections** 
  - Title, text, url and image of any django apps you create.
  - Dynamically appear on the homepage as a grid and in navbar menu.
  - Dynamically appear under category headings in the sidebar and footer.

- When you create a new django app, you can add information about the app as a website section with text, image and url.
- You can load the tags (from template tags) to include website sections and categories anywhere you like in your project.

## FEATURES

Completely adpatable, the base project consists of:

- Base HTML
- Flat Pages
- Website Sections
- Homepage

For these demo images, I created two flat pages and three website sections that appear under two website categories:

- Base HTML file with a sidebar:

![Base Sidebar](https://github.com/richardgourley/dynamic-django-base/blob/main/base_html_sidebar.png)

----

- Base HTML full width page with a website sections grid:

![Base Full width](https://github.com/richardgourley/dynamic-django-base/blob/main/base_html_fullwidth.png)

## GETTING STARTED

- This project is development ready NOT production ready. (See docs for deploying a Django project)
- All project and app files are included in the 'dynamicdjangobase' directory.
- The 'dynamicdjangobase' directory will be created inside your virtual environment when you run django startapp.

STEPS

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

- Install tinmyce-django

```
pip install django-tinymce
```

- Install pillow for images - Imaging Library adds image processing capabilities to your Python interpreter.

```
pip install Pillow
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

There are other django libraries and web development libraries worth looking at that I always use such as 
- python decouple (for setting up a .env file to hide your secret key and production database variables)
- django-compressor (for Bootstrap)
- django-libsass (for Bootstrap)



