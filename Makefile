build:
	docker-compose up -d --build api_pagination

build-prod:
	docker-compose up -d --build api_pagination_prod && docker-compose up -d --build nginx

up:
	docker-compose up -d api_pagination

bash:
	docker exec -it api_pagination bash

test:
	docker exec -i api_pagination python test_flask.py

run-dev:
	docker rm api_pagination & docker-compose run --name api_pagination --rm --service-ports api_pagination

stop:
	docker-compose down
