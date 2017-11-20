FROM python:3

ENV PYTHONUNBUFFERED 1

WORKDIR /code

RUN apt-get update && apt-get install -y \
    build-essential \
    gfortran \
    libblas-dev \
    liblapack-dev \
    libxft-dev \
    npm\
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /code/
COPY package.json /code/

RUN pip install -r requirements.txt
RUN npm install -g gulp
RUN npm install gulp
RUN npm install -g n
RUN n stable
RUN npm install

COPY . /code/

EXPOSE 8000

CMD python manage.py runserver 0.0.0.0:$PORT
