FROM python:3.6-slim
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

WORKDIR /app
CMD ["python", "manage.py", "run"]