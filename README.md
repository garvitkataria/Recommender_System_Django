# Recommender_System_Django


## Angular FrontEnd Server
https://github.com/garvitkataria/Recommender_System_Angular

### Setup The Project

1. Create Virtual Environment
          
          mkvirtualenv --python=/usr/bin/python3.5 myenv
     
2. Install Dependencies by pip

          pip install -r requirements.txt

3. Start the virtual environment and Go to the project directory

        source bin/activate
        cd Recommender_System_Django-master
    
4. Run Django Server

        python manage.py runserver
        

## DEMO
1. <h5>Step 1</h5>
Enter your email and Phone no. to get started.

![alt text](https://github.com/garvitkataria/Recommender_System_Django/blob/master/Demo_Images/step1.png)

2. <h5>Step 2</h5>
Rate atleast 10 movies to unlock recommendation feature button.

![alt text](https://github.com/garvitkataria/Recommender_System_Django/blob/master/Demo_Images/step2.png)

3. <h5>Step 3</h5>
You can check the movie recommendations by these 3 Algorithms.
<ul>
<li> Item-Item Collaborative Filtering</li>
<li> User-User Collaborative Filtering</li>
<li> Single Value Decomposition</li>
</ul>

4. <h5>Step 4</h5>
Click on finish button to go back to the welcome page.

![alt text](https://github.com/garvitkataria/Recommender_System_Django/blob/master/Demo_Images/step3.png)



## Directory Structure

          ├── AuthUser
          │   ├── __init__.py
          │   ├── __pycache__
          │   │   ├── __init__.cpython-36.pyc
          │   │   ├── admin.cpython-36.pyc
          │   │   ├── models.cpython-36.pyc
          │   │   ├── serializers.cpython-36.pyc
          │   │   ├── urls.cpython-36.pyc
          │   │   └── views.cpython-36.pyc
          │   ├── admin.py
          │   ├── apps.py
          │   ├── migrations
          │   │   ├── 0001_initial.py
          │   │   ├── 0002_auto_20190202_0515.py
          │   │   ├── 0003_auto_20190202_0515.py
          │   │   ├── 0004_remove_user_avatar.py
          │   │   ├── __init__.py
          │   │   └── __pycache__
          │   │       ├── 0001_initial.cpython-36.pyc
          │   │       ├── 0002_auto_20190202_0515.cpython-36.pyc
          │   │       ├── 0003_auto_20190202_0515.cpython-36.pyc
          │   │       ├── 0004_remove_user_avatar.cpython-36.pyc
          │   │       └── __init__.cpython-36.pyc
          │   ├── models.py
          │   ├── serializers.py
          │   ├── tests.py
          │   ├── urls.py
          │   └── views.py
          ├── Demo_Images
          │   ├── step1.png
          │   ├── step2.png
          │   └── step3.png
          ├── Movie
          │   └── 97332
          ├── README.md
          ├── RecomendationSystem
          │   ├── __init__.py
          │   ├── __pycache__
          │   │   ├── __init__.cpython-36.pyc
          │   │   ├── settings.cpython-36.pyc
          │   │   ├── urls.cpython-36.pyc
          │   │   └── wsgi.cpython-36.pyc
          │   ├── settings.py
          │   ├── urls.py
          │   └── wsgi.py
          ├── db.sqlite3
          ├── default.jpg
          ├── manage.py
          ├── movies
          │   ├── __init__.py
          │   ├── __pycache__
          │   │   ├── __init__.cpython-36.pyc
          │   │   ├── admin.cpython-36.pyc
          │   │   ├── models.cpython-36.pyc
          │   │   ├── serializers.cpython-36.pyc
          │   │   ├── urls.cpython-36.pyc
          │   │   └── views.cpython-36.pyc
          │   ├── admin.py
          │   ├── apps.py
          │   ├── migrations
          │   │   ├── 0001_initial.py
          │   │   ├── 0002_auto_20190202_0645.py
          │   │   ├── 0003_auto_20190202_1356.py
          │   │   ├── 0004_auto_20190202_1637.py
          │   │   ├── __init__.py
          │   │   └── __pycache__
          │   │       ├── 0001_initial.cpython-36.pyc
          │   │       ├── 0002_auto_20190202_0645.cpython-36.pyc
          │   │       ├── 0003_auto_20190202_1356.cpython-36.pyc
          │   │       ├── 0004_auto_20190202_1637.cpython-36.pyc
          │   │       └── __init__.cpython-36.pyc
          │   ├── models.py
          │   ├── serializers.py
          │   ├── tests.py
          │   ├── urls.py
          │   └── views.py
          ├── rating
          │   ├── __init__.py
          │   ├── __pycache__
          │   │   ├── __init__.cpython-36.pyc
          │   │   ├── admin.cpython-36.pyc
          │   │   ├── models.cpython-36.pyc
          │   │   ├── serializers.cpython-36.pyc
          │   │   ├── urls.cpython-36.pyc
          │   │   └── views.cpython-36.pyc
          │   ├── admin.py
          │   ├── apps.py
          │   ├── migrations
          │   │   ├── 0001_initial.py
          │   │   ├── __init__.py
          │   │   └── __pycache__
          │   │       ├── 0001_initial.cpython-36.pyc
          │   │       └── __init__.cpython-36.pyc
          │   ├── models.py
          │   ├── serializers.py
          │   ├── tests.py
          │   ├── urls.py
          │   └── views.py
          └── requirements.txt
