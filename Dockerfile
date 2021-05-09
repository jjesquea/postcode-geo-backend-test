FROM python:3.8
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
COPY . /code

COPY requirements.txt /requirements/
RUN pip install -r /requirements/requirements.txt

COPY ./start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

WORKDIR /code