# Flask with Docker Boilerplate

## Run

To run this project install docker and docker-compose in your machine and run the following command:

```
docker-compose up
```

You can test a endpoint to make sure server is running: Make a get request to `localhost:5000/api/users` to receive a empty list.

## Database

This project use Postgres as the main database. To run migrations or create a new one you must enter in the container:

```
docker-compose exec api bash
```

Create Migration:
```
flask db migrate
```

Apply Migration:
```
flask db upgrade
```
## Testing

This application has unit tests! In order to run and verify then you must enter in the container:
```
docker-compose exec api bash
```

and then run the tests:
```
pytest
```
if you want to create more tests just add a new file inside the `tests` folder with a prefix `test_*`. Pytest will automatically test all files with this prefix.

## Production
To build the production image with nginx you can run the following command:

```
docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d
```

To access the production endpoint just make requests to `localhost:8000/api/*`.