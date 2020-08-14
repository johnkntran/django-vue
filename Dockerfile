FROM python:3.7

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt

ARG DEPENDENCIES="build-essential gcc libc-dev python3-dev default-libmysqlclient-dev nodejs vim"
RUN apt-get update && \
    curl -sL https://deb.nodesource.com/setup_12.x | bash - && \
    apt-get install -y $DEPENDENCIES
COPY package.json /code/
RUN npm install
ENV PATH /code/node_modules/.bin:${PATH}

EXPOSE 8000
COPY . /code/

ENTRYPOINT ["npm", "run", "docker"]
