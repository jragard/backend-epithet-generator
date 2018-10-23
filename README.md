# Epithet Generator

Create a Flask API to serve random epithets from the [Shakespeare Insult Kit]

In this sprint, we have defined a function named configure_app in the __init__.py file, imported os, dotenv, and flask within this function, defined environment variables, and instantiated an instance of Flask.  

Then, in the app.py file, we have imported that app instance from the __init__ file and defined a '/' and '/vocabulary' route to serve data (which will be further fleshed out in future sprints)

In sprint B, I added an EpithetGenerator class with methods to get data for a single epithet, to display that single epithet, to get a user-specified quantity of epithets, and to display the entire vocab dataset contained in the data.json file in this project's 'resources' directory.  Going to '/' displays a single epithet, '/vocabulary' displays the vocab dataset, and '/epithets/<quantity>' displays the specified quantity of epithets.

In sprint C, I have added a method to the EpithetGenerator class that returns a random quantity of epithets.  I have also added a route to serve this random quantity.  I will be writing integration tests for each route using the Flask test client to verify that all the components created are working together as expected.