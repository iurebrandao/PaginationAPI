build:
	docker-compose up -d --build

build-prod:
	docker-compose up -d --build

up:
	docker-compose up -d

bash:
	docker exec -it api_pagination bash

test:
	docker exec -i api_pagination pytest

run-dev:
	docker rm api_pagination & docker-compose run --name api_pagination --rm --service-ports api_pagination
