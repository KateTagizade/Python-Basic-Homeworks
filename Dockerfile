FROM tiangolo/uwsgi-nginx-flask:python3.10

COPY requirements.txt /homework_06/requirements.txt

RUN pip install --upgrade pip

RUN pip install --no-cache-dir --upgrade -r /homework_06/requirements.txt

COPY ./homework_06 /homework_06