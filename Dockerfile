# syntax=docker/dockerfile:1
FROM python:3

ENV PYTHONDONTWRITEBYTECODE=1
#Prevents Python from writing pyc files to disc (equivalent to python -B option)

ENV PYTHONUNBUFFERED=1
#Prevents Python from buffering stdout and stderr (equivalent to python -u option)

# install psycopg2 dependencies
#RUN apt update && apt add postgresql-dev gcc python3-dev musl-dev

WORKDIR /usr/src/app

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy entrypoint.sh
#COPY ./entrypoint.sh .
#RUN sed -i 's/\r$//g' /usr/src/app/entrypoint.sh
#RUN chmod +x /usr/src/app/entrypoint.sh

RUN mkdir /usr/src/app/static

# copy project
COPY . .

# run entrypoint.sh
#ENTRYPOINT ["/usr/src/app/entrypoint.sh"]