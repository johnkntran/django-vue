# Introduction

This is a template for how to integrate [Vue.js](https://v3.vuejs.org/) into [Django](https://docs.djangoproject.com/).
- For the frontend, it uses [Vite](https://vitejs.dev/) as the compiler and is written with the Composition API. It includes frontend routing via [Vue Router](https://next.router.vuejs.org/) and state management via [Vuex](https://next.vuex.vuejs.org/).
- For the backend, it uses [Django Rest Framework](https://www.django-rest-framework.org/).


## Getting Started (Docker)
Download [Docker Desktop](https://www.docker.com/products/docker-desktop). Then,
clone this repository down to your local computer.

Run these commands to build the Docker image and start a container serving at http://127.0.0.1:8000/:
```bash
docker build --file Dockerfile --tag django-vue . # Note: This will take a while...
docker run --volume /Users/john.tran/Development/django-vue:/code --publish 8000:8000 --name django_vue django-vue # Point volume to your local repo directory
```

If you want to SSH into the running container, issue:
```bash
docker exec -ti django_vue bash # CTRL + D to exit
```
You can run commands such as `python manage.py showmigrations`, `python manage.py shell`, etc.

When you are finished, stop the container and remove the image by typing in a separate terminal tab or
window:
```bash
docker container rm --force django_vue
docker rmi django-vue
```

### First Time Project Load Errors
When you first run the project, if you get an error like:
```
sh: 1: watch: not found
...
...
...
BrokenPipeError: [Errno 32] Broken pipe
```
then this is due to a volume syncing error. Basically your local directory (which does not have `/node_modules`) is overwriting the container directory, which has `/node_modules` installed from the [Dockerfile](./Dockerfile).

To fix this:
- Edit the last line of the [Dockerfile](./Dockerfile) to `ENTRYPOINT ["sleep", "infinity"]`.
- Remove the existing container and image using the commands above: `docker container rm ...` and `docker rmi ...`.
- Rebuild the container again using the command above: `docker build ...`
- Rerun the container again using the command above: `docker run ...`.
- Open a separate terminal and shell into the running container using the command above: `docker exec ...`.
- Run `npm install` inside the container.

The volume ("bind") mount should pick up `/node_modules` and dump it back in your local directory.
- Change the [Dockerfile](./Dockerfile) back to `ENTRYPOINT ["npm", "run", "localhost"]`.
- Remove, rebuild, and rerun the container using the commands above.
