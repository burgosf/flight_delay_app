test:
	docker-compose run web py.test
test-cov:
	docker-compose run web py.test --cov=. --cov-report html:docs/tests/cov_html --cov-report term
test-docs:
	docker-compose run --service-ports web pytest tests --html=docs/tests/test_report.html
test-watch:
	docker-compose run web ptw
test-all:
	docker-compose run web py.test -s
	docker-compose run web bandit -r .
	docker-compose run web flake8 .
swagger-docs:
	docker-compose run docs