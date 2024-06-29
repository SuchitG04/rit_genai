FROM ubuntu
FROM python:3

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt
COPY ./app/wiki-news-300d-1M.vec /code/app/wiki-news-300d-1M.vec

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

CMD ["fastapi", "run", "app/main.py", "--port", "80"]
