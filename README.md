# flight_delay_app
Serving the flight_delay_model through a flask app

## To change:

adjust: docs/swagger.yml to configure swagger documentation


## Build image
Build the container using `docker-compose build`

## Run app locally
Run the container using `docker-compose up`

## Find running containers
Find the container's id using `docker-compose ps`

## Entry container
Enter the container using `docker-compose run --entrypoint=sh web`

## Tests
Run the tests using `docker-compose run web pytest` or shortcut `make test`
Run the tests watch using `docker-compose run web ptw` or shortcut `make test-watch`

## Coverage
To render HTML coverage just do `make test-cov` and it will produce folder `docs/tests/cov_html` open there `index.html` in Your browser to see actual coverage. `make test-cov` run tests + produce coverage.

## Tests cases docs
To render HTML report with test cases and test names just do `make test-docs` and it will produce file `docs/tests/test_report.html`. Open it in Your browser to see test case list.

## Build documentation
To build documentation locally just do `docker-compose run docs` or `make swagger-docs`
