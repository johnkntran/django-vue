FROM python:3.10-slim-bullseye

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONDEVMODE 1
ENV PYTHONFAULTHANDLER 1

WORKDIR /code

ARG DEPENDENCIES="build-essential gcc libc-dev python3-dev vim nodejs"
RUN set -ex && \
    apt-get update && apt-get --yes upgrade && \
    curl -sL https://deb.nodesource.com/setup_16.x | bash - && \
    apt-get install --yes $DEPENDENCIES

COPY requirements.txt /code/
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY package.json /code
RUN npm install
ENV PATH /code/node_modules/.bin:${PATH}

EXPOSE 8000
COPY . /code

ENTRYPOINT ["npm", "run", "docker"]
