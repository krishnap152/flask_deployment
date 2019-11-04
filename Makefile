.PHONY: clean system-packages python-packages install tests run 

clean:
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.log' -delete

system-packages:
	sudo apt install python-pip -y

python-packages:
	pip install -r requirements.txt

install: system-packages python-packages

tests:
	python manage.py test

run:
	python manage.py run

all: clean install tests run

docker_clean:
	docker rm -vf $(docker ps -a -q)

rebuild:
	docker build -t flask-docker .

run_docker:
	docker run -p 5000:5000 -v $(PWD):/app flask-docker

prune:
	docker system prune -af
