# Introduction

**[Vue.js](https://vuejs.org/)** is a progressive reactive framework that allows
developers to move away from manipulating the document-object model (DOM) in
their browser and more towards controlling the data on their page and letting
the DOM naturally react as that data changes.

**[Django](https://www.djangoproject.com/)** is a wonderful, all-purpose web
framework that allows developers to harness a robust templating language on top
of a powerful backend framework and object-relation model (ORM) for managing
data, with support for REST API development and other third-party functionality.
However, Django typically relies on JavaScript libraries such as jQuery to add
interactivity to a web page, involving non-straightforward manipulations of the
DOM which becomes increasingly hard to maintain at scale.

This repository is an example of how to go from a traditional *Django* and
*jQuery*-centered ecosystem and progressively add interactivity using Vue.js.

The **first example** (http://127.0.0.1:8000/example1) shows a typical web page
constructed solely using Django and jQuery, with Ajax methods to fetch and
interact with data from the server.

The **second example** (http://127.0.0.1:8000/example2) shows how to sprinkle in
Vue.js to such a web page as an inline script to manage the data (or "state") on
the page. This frees us up from modifying the DOM and instead allows us to
modify the data (e.g. push a stock onto the array of portfolios) and have the
DOM naturally "react" to those changes and re-render itself.

The **third example** (http://127.0.0.1:8000/example3) demonstrates how to
utilize the full Vue.js single-file component ecosystem. The page uses NPM to
build an *app.js* file gets rendered as a Django static asset. This JS file
contains the entire Vue.js compiled bundle, containing all Vue components,
CSS, and JS logic.

# Getting Started

The code is written in the latest
[Python 3.7](https://www.python.org/downloads/) and
[Django 2.2](https://www.djangoproject.com/download/) available during
development. It also uses
[Node.js 8.11 with NPM 6.4](https://nodejs.org/en/download/) to compile the
Vue.js code. We assume you have all of these installed on your local computer.

To get started, clone this repository down to your local computer.

After that, set up a Python virtual environment and install all Python 3rd-party
packages by issuing these commands:
```bash
cd mm_demo
python3 -m venv .venv
source .venv/bin/activate # For MacOS/Linux
source .venv\Scripts\activate.bat # For Windows
pip install -r requirements.txt
```

We must also install the NPM package dependencies by issuing this command:
```bash
npm install
```

After that, run the Django database migrations to set up a local SQLite database
populated with sample data:
```bash
python manage.py migrate
```

To get the site up and running, issue this npm script:
```bash
npm start # Hit CTRL + C to kill the Django server when finished
```

Finally, navigate to:
- [localhost:8000/example1](http://127.0.0.1:8000/example1)
    **Django and jQuery Only**
- [localhost:8000/example2](http://127.0.0.1:8000/example2)
    **Inline Vue.js Instance Inside Django Template**
- [localhost:8000/example3](http://127.0.0.1:8000/example3)
    **Vue.js Single-File Components with NPM Build**

The web app is a simple CRUD app demonstrating a "Portfolio Management Tool"
allowing the user to add and remove stocks from specific portfolios. All three
pages work exactly the same, but the underlying architectures are completely
different - demonstrating how Vue.js can be integrated progressively into
existing Django projects.

# For More Information

For more information about incorporating Vue.js into Django projects, check out
[the slides](https://docs.google.com/presentation/d/1Fdu0_J8EYyKft2xUqiHe3P9DIMMX17DEHYDAqPxqzaI/view?usp=sharing),
which go into depth about the setup demonstrated here.

Also, [this repository](https://github.com/themotleyfool/django-vue-starter-template)
is the official TMF Django Vue.js starter pack, describing a more complicated
setup with testing, routing, state management, and other features baked in.
