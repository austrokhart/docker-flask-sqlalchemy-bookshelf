
# docker-flask-sqlalchemy-bookshelf

This project is a simple example of development, testing and deploying an application using Docker containers.

The application in the project implements a simple CRUD interface and is developed using Flask and SQLAlchemy. It uses external services such as MariaDB to store data (containerized using Docker volumes to persist data) and uWSGI and Nginx to host the Flask application.


## Interface

Work with data is performed using a restful API. List of routes:

* create book

    method: `POST`<br>
    url: `/book/`<br>
    data: 
    ```
    {
        title: string
    }
    ```

* read book

    method: `GET`<br>
    url: `/book/<id>/`<br>
    data: no

* update book

    method: `PUT`<br>
    url: `/book/<id>/`<br>
    data: 
    ```
    {
        title: string
    }
    ```
    
* delete book

    method: `DELETE`<br>
    url: `/book/<id>/`<br>
    data: no
    
* list books

    method: `GET`<br>
    url: `/book/list/`<br>
    data: no


## Services

The project uses several services:

* MariaDB service, available at `0.0.0.0`:`3306`.

* uWSGI service that hosts the Flask application, available through the socket with using the `uwsgi` protocol at `{host}`:`{port}`.

* Nginx service that reverse proxies the uWSGI service with using the `uwsgi` protocol at `{uwsgi_host}`:`{uwsgi_port}` on `0.0.0.0`:`{nginx_port}`.


## `docker-compose` configuration override

To override the values of one configuration with the values of another, use:<br>
`docker-compose -f docker-compose.base.yml -f docker-compose.additional.yml ...`


## Development

To start developing, use:

`docker-compose -f docker-compose.yml -f docker-compose.dev.yml up --build`

In the development configuration, the host directories are mounted in containers. This allows you to work with them using your IDE.


## Testing

To start testing, use:<br>
`docker-compose -f docker-compose.test.yml up --build`

In the test configuration, a separate volume mounted for data storage. This gives more opportunities for testing (clearing the tables, filling them with the necessary data).


## Deployment

To deploy, use:<br>
`docker-compose -f docker-compose.yml up --build --detach`

This is the easiest way to deploy. In complex projects, it may be better to use third-party solutions to orchestrate containers.