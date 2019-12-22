FROM tiangolo/uwsgi-nginx-flask:python3.7

COPY requirements.txt /app

RUN pip install -r /app/requirements.txt

COPY ./app /app

CMD python3 /app/app/main.py
