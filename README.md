# For EyeLet Take Home Challenge

## Author: Tanmay Dutta

## Technology Stack

### Backend

- Django
- Django Rest Framework
- pytest

### Frontend

- React

### Packaging and deployment

- Docker

## Instructions

## Easy way (Docker)

- User need to install Docker to run the application
- Use docker compose to spin up everything for you `docker-compose build`
- Migration `docker-compose run url-shortner-app python manage.py migrate`
- Start all containers `docker-compose up`
- Navigate to [react localhost](http:\\localhost:3000)  --> http:\\localhost:3000
- Django runs as 8000 port

## Manual way

Ensure that you do the following before starting to look at code

- Install npm
- Install python
- Install virtualenv


- Backend lives in "url_shortner" directory. cd in to the directory in terminal `cd url_shortner`

- Make sure you have virtualenv setup
- Activate it `source <path to venv>\bin\activate`
- Install requirements for the project `pip install -r requirements.txt`
- Run python migrations `python manage.py migrate`
- Run tests to ensure everything is oka `python manage.py test`
- Run django server `python manage.py runserver`


- frontend lives in "frontend" directory
  - Open frontend in terminal and fire command `npm run start`
  - This should get the frontend going
