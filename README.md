# 2019fa-final-project-patchcasey
2019fa-final-project-patchcasey created by GitHub Classroom
[![Build Status](https://travis-ci.com/csci-e-29/2019fa-final-project-patchcasey.svg?token=5ichzqk8s8tsSTcNuNkm&branch=master)](https://travis-ci.com/csci-e-29/2019fa-final-project-patchcasey)
[![Maintainability](https://api.codeclimate.com/v1/badges/e7671fca1c2d0c1424b0/maintainability)](https://codeclimate.com/repos/5df84994a68cf2016300a610/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/e7671fca1c2d0c1424b0/test_coverage)](https://codeclimate.com/repos/5df84994a68cf2016300a610/test_coverage)

# Objective
The objective of my final project was to build a framework for storing, processing, and displaying geospatial data in a Django framework. The reason for choosing Django is ultimately this would be a user-facing application that could be interacted with and manipulated by the end-user. The specific use case that I chose to explore in this project is an example patient population existing in Austin, TX (all fake data!). These patients live throughout the city and are patients of a local hospital, and I am thinking of opening a new hospital in Round Rock, TX. I want to pick the best spot for this hospital, so I enlist the help of a data scientist to model the areas that my patients live in, so I can pick the location that would serve most potential patients. What the data scientist does is build a grid over the patients and find the demographic variables in these grid squares, then does a spatial lookup to find which squares have patients in them. Then, this binary yes/no of patient existence is predicted based on the demographic variables, and applied to a grid in Round Rock, TX - showing the probability that each square would have a patient in it. The data is very rough and obviously representative - I wanted to focus on the Python, not the data science!

My goal for this project (as stated in my proposal) was: "A working, minimum viable product GUI with data pipelining through Django application, with example predictive model."

In the time between submitting pset_6 and submission, I achieved:

- A working minimum viable product GUI using the Leaflet framework (https://leafletjs.com/)
- Although the phrasing is a bit awkward (data pipelining) - I achieved this through building models and processing geospatial data appropriately
  -You will note that I stored data directly in the repo - this was intentional. Although I learned in this course that GitHub is for code, not data, I figured it would be easier to handle the data directly, rather than deal with permissions on S3
- I built a (completely bogus) predictive model using a random forest framework that would be used to highlight predictive areas and deployed the trained model, assigning the resulting score to the original models

What I was unable to achieve:

- I was unable to display the grids on the GUI. After hours and hours of trying to figure it out, I decided to give up and just hardcode the GeoJSON into the HTML file, rather than wrestle with the JavaScript library.
  - It was interesting, however, to build a serializer to change the data from ESRI Shapefile format into GeoJSON (which should 100% have been readable by the Leaflet API commands)
- I was unable to color the grids based on the predictive model
- I did not have enough time to incorporate Luigi to handle the processing of the data
- I had immense trouble with getting pytest to work. I believe that GeoDjango complicated working with many things, one of them happening to be pytest.

## Initial setup
I used a Postgres database because it has the PostGIS extension that can store/handle geospatial data. To run this project, one would need to handle several things:

1. pipenv install
2. Create a spatial database:
```
$ createdb  <db name>
$ psql <db name>
> CREATE EXTENSION postgis;
```
3. Follow the download instructions found here (https://docs.djangoproject.com/en/3.0/ref/contrib/gis/install/geolibs/)
    4. Download GEOS (https://trac.osgeo.org/geos/)
    5. Download PROJ.4 (https://github.com/OSGeo/PROJ/wiki)
    6. Download GDAL (https://gdal.org/download.html)
4. Set your database variables in the .env file (NAME, USER, PASSWORD)

## Running the project
You need to run the standard commands to create the models in the database: 
```pipenv run python manage.py makemigrations``` 
```pipenv run python manage.py migrate```

You need to run the commands that I have made that load the data into the models: 
```pipenv run python manage.py load_patients```
```pipenv run python manage.py load_grid```
```pipenv run python manage.py load_RoundRockGrid```

At this point, you now have a fully populated database with patients, the grid they live on, and the grid you want to predict on. By running ```pipenv run python manage.py spatial_lookup``` you will run the predictive model. This works in 3 steps:

1. It does a spatial lookup to count which patients are in which squares of the initial grid
2. It then takes this count and assigns a true/false value to each square in the grid, using this as the predicted value in the model, which it then runs the model on
3. The trained model is then deployed to the RoundRock grid, and then the % chance of having a patient (based on the demographic factors) is saved to the RoundRockGrid model, called "color" as it was going to be used to color the squares

Finally, you can run ```pipenv run python manage.py runserver``` and navigate to http://127.0.0.1:8000/ to see the patients and the related grids. You'll notice that unfortunately, I was unable to color the grids based on their predicted values.
