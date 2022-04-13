# gudlift-registration

## 1. Why

   This is a proof of concept (POC) project to show a light-weight version of our competition booking platform. The aim is the keep things as light as possible, and use feedback from the users to iterate.

## 2. Getting Started

This project uses the following technologies:

* Python v3.x+

* [Flask](https://flask.palletsprojects.com/en/1.1.x/)  
Whereas Django does a lot of things for us out of the box, Flask allows us to add only what we need. 
     
* [Virtual environment](https://virtualenv.pypa.io/en/stable/installation.html)  
This ensures you'll be able to install the correct packages without interfering with Python on your machine.
Before you begin, please ensure you have this installed globally.

## 3. Installation

* After cloning, change into the directory and type ```virtualenv .```. This will then set up a a virtual python environment within that directory.

* Next, type ```source bin/activate```. You should see that your command prompt has changed to the name of the folder. This means that you can install packages in here without affecting affecting files outside. To deactivate, type <code>deactivate</code>

* Rather than hunting around for the packages you need, you can install in one step. Type ```pip install -r requirements.txt```. This will install all the packages listed in the respective file. If you install a package, make sure others know by updating the requirements.txt file. An easy way to do this is ```pip freeze > requirements.txt```

* Flask requires that you set an environmental variable to the python file. However you do that, you'll want to set the file to be <code>server.py</code>. ```export FLASK_APP=server.py```. Check [here](https://flask.palletsprojects.com/en/1.1.x/quickstart/#a-minimal-application) for more details  

* You should now be ready to test the application. In the directory, type either ```flask run``` or ```python -m flask run```. The app should respond with an address you should be able to go to using your browser.

## 4. Current Setup

The app is powered by [JSON files](https://www.tutorialspoint.com/json/json_quick_guide.htm). This is to get around having a DB until we actually need one. The main ones are:
* competitions.json - list of competitions
* clubs.json - list of clubs with relevant information. You can look here to see what email addresses the app will accept for login.

## 5. Testing

### The modules used for testing :  
* [pytest](https://docs.pytest.org/en/latest/) for unitests or integration tests.
* [selenium](https://selenium-python.readthedocs.io/) for functional tests.  
  The framework also requires the installation of a driver to interface with a web browser such as Chrome, Firefox, Edge or Safari. Each browser will have its own driver. Here are the links to download the driver according to your browser:
  * [chrome driver](https://sites.google.com/a/chromium.org/chromedriver/downloads)
  * [firefox driver](https://github.com/mozilla/geckodriver/releases)
  * [safari driver](https://webkit.org/blog/6900/webdriver-support-in-safari-10/)
  * [edge driver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)  
  
  __Copy the downloading driver in the tests directory__
* [locust](https://docs.locust.io/en/stable/index.html) for the performance tests

### Run the tests
You need to run the flask server before running the functionnal tests and performance tests  
```flask run```  
Run the test in a terminal with ```pytest``` to run all the tests or ```pytest <path/file/test>```  

### Covering test
To measuring the coverage of the test, we use the library [coverage](https://coverage.readthedocs.io/en/coverage-5.1/) you should add to your project.
To see the results in the terminal use ```pytest --cov```
To create an html report use ```pytest --cov-report -html``` and open index.html in the directory htmlcov

