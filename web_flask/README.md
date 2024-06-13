# 0x04. AirBnB clone - Web framework

## Overview

This project marks the fifth phase of developing an AirBnB clone, with the primary focus on creating a Flask web application for displaying and interacting with AirBnB data. The web flask project ties the static HTML front end with the dynamic database back end, displaying database data in a static HTML page.

The overall project now incorporates Python, Object-Oriented Programming (OOP), SQL, and the SQLAlchemy ORM, integrates a static web page, populates it with data from the database using the Flask web framework. This is accomplished by creating routes in Flask that render HTML templates and use data fetched from the database (via SQLAlchemy and the storage system) to dynamically generate content displayed on the web page using Jinja templates. The project also utilizes bash and puppet scripts to automate the deployment of static content.

## Project structure

- `0-hello_route.py`: Flask route for displaying "Hello HBNB!" message.
- `1-hbnb_route.py`: Flask route for displaying "HBNB" message.
- `2-c_route.py`: Flask route for displaying "C" followed by the value of the text variable.
- `3-python_route.py`: Flask route for displaying "Python" followed by the value of the text variable.
- `4-number_route.py`: Flask route for displaying if a number is a number.
- `5-number_template.py`: Flask route for displaying a number using a template.
- `6-number_odd_or_even.py`: Flask route for displaying if a number is odd or even.
- `7-states_list.py`: Flask route for displaying a list of states.
- `8-cities_by_states.py`: Flask route for displaying cities grouped by state.
- `9-states.py`: Flask route for displaying information about a state.
- `10-hbnb_filters.py`: Flask route for displaying filters for Airbnb.
- `100-hbnb.py`: Flask route for main page of Airbnb.


- `templates/`: Directory for HTML templates.
  - `100-hbnb.html`: HTML template for main page of Airbnb.
  - `10-hbnb_filters.html`: HTML template for filters page of Airbnb.
  - `5-number.html`: HTML template for displaying a number.
  - `6-number_odd_or_even.html`: HTML template for displaying if a number is odd or even.
  - `7-states_list.html`: HTML template for displaying a list of states.
  - `8-cities_by_states.html`: HTML template for displaying cities grouped by state.
  - `9-states.html`: HTML template for displaying information about a state.


- `static/`: Directory for static files.

