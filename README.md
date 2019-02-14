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
        
## API Docs
1. API to get all the movies or post a new movie

          http://35.200.250.64:8007/movies/

2. API to get all the users or post a new user
          
          http://35.200.250.64:8007/user/
          
3. API to get all the ratings or post a new rating
          
          http://35.200.250.64:8007/rating/
          
4. API to get recommendation by Item-Item Collaborative Filtering
          
          http://35.200.250.64:8007/rating/recommend/?user_id=1
          
5. API to get recommendation by User-User Collaborative Filtering
           
          http://35.200.250.64:8007/rating/recommend2/?user_id=1

6. API to get recommendation by Singular Value Decomposition(SVD)
          
          http://35.200.250.64:8007/rating/recommend3/?user_id=1

## MovieLens Dataset
https://github.com/garvitkataria/Recommender_System_Django/tree/master/DataScraping/data

This dataset (ml-latest-small) describes 5-star rating and free-text tagging activity from [MovieLens](http://movielens.org), a movie recommendation service. It contains 100836 ratings and 3683 tag applications across 9742 movies. These data were created by 610 users between March 29, 1996 and September 24, 2018. This dataset was generated on September 26, 2018.


## Data Scraping

https://github.com/garvitkataria/Recommender_System_Django/DataScraping/MovieDataScraping.ipynb

Scrapped Movie Data from IMDB:
https://github.com/garvitkataria/Recommender_System_Django/blob/master/DataScraping/ScrappedMovieData.json
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
          │   ├── admin.py
          │   ├── apps.py
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
          │   ├── settings.py
          │   ├── urls.py
          │   └── wsgi.py
          ├── db.sqlite3
          ├── default.jpg
          ├── manage.py
          ├── movies
          │   ├── __init__.py
          │   ├── admin.py
          │   ├── apps.py
          │   ├── models.py
          │   ├── serializers.py
          │   ├── tests.py
          │   ├── urls.py
          │   └── views.py
          ├── rating
          │   ├── __init__.py
          │   ├── admin.py
          │   ├── apps.py
          │   ├── models.py
          │   ├── serializers.py
          │   ├── tests.py
          │   ├── urls.py
          │   └── views.py
          └── requirements.txt
