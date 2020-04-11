build:
	sudo docker-compose build

up:
	sudo docker-compose up

up-non-daemon:
	docker-compose up

start:
	docker-compose start

stop:
	docker-compose stop

restart:
	docker-compose stop && docker-compose start

restart-server:
	docker-compose stop web && docker-compose start web

shell-nginx:
	docker exec -ti nginx_app /bin/sh

shell-web:
	sudo docker exec -ti web_app /bin/sh

shell-db:
	docker exec -ti postgres_db /bin/sh

log-nginx:
	docker-compose logs nginx  

log-web:
	docker-compose logs web  

log-db:
	docker-compose logs db

collectstatic:
	docker exec web_app /bin/sh -c "python manage.py collectstatic --noinput"  