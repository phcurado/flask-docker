# Flask with Docker Boilerplate

## Run

To run this project install docker and docker-compose in your machine and run the following command:

```
docker-compose up
```

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
flask db migrate
```