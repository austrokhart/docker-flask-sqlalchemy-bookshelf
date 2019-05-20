
# docker-flask-sqlalchemy-bookshelf

This project is a simple example of development, testing and deploying an application using Docker containers.

The application in the project implements a simple CRUD interface and is developed using Flask and SQLAlchemy. It uses external services such as MariaDB to store data (containerized using Docker volumes to persist data) and uWSGI and Nginx to host the Flask application.

## `docker-compose` configuration override

To override the values of one configuration with the values of another, use:<br>
`docker-compose -f docker-compose.base.yml -f docker-compose.additional.yml ...`

## Development

To start developing, use:

`docker-compose -f docker-compose.yml -f docker-compose.dev.yml up --build`

In the developer's configuration, the host directories are mounted in containers. This allows you to work with them using your IDE.

## Testing

To start testing, use:<br>
`docker-compose -f docker-compose.test.yml up --build`

## Deployment

To deploy, use:<br>
`docker-compose -f docker-compose.yml up`