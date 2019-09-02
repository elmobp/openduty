all: build compose

build:
	docker build -t elmobpopenduty . --no-cache

compose:
	docker-compose up --force-recreate

clean:
	docker-compose down --rmi all -v

stop:
	docker-compose stop
