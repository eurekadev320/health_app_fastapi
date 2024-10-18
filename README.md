## How to build
    docker-compose build
## How to run
    docker-compose up
## How to make migrations
    docker-compose run web alembic revision --autogenerate
## How to run migrations
    docker-compose run web alembic upgrade head
## How to run unit testing
    docker-compose run web pytest

## Documentation
    swagger - http://localhost:8000/docs
    redoc - http://localhost:8000/redoc


## Explanation
### /claim_process/ (POST)
- This will add `claim_process` request to the db 
- It will calculate the `net_fee` for `claim_process`
- It will add the `process_payment` job into queue

### /queue/ (POST)
- This is supposed to run periodically to handle the queue jobs
- It will handle different handler based on `queue_type`

