# Team 34 project

## Working with the repo

### Setting up

Clone the repo and deal with authorisations 

```bash
git clone https://github.com/SyroQT/ncl-team34-project.git
```

Install dependencies (make sure to create a personal env before)

```bash
pip install -r requirements.tx
```

Make sure you have the correct `.env` and `firebase_key.json` files

Run the app. We recommend running it through the CLI

```bash
python app.py
# or 
set FLASK_APP=app.py
flask run
# or use your way
```

### Updating 

Each user should create his own branch. And merge/create pull requests from there. 
Remember to commit more rather than less.

## Important information

### Running the app
There seems to be issues trying to run the web app using Pycharms' tool. So we suggest to use CLI

### Coding conventions

#### Python 
- pep8 conventions [link](https://www.python.org/dev/peps/pep-0008/)
- Black formatter to enforce this [link](https://black.readthedocs.io/en/stable/)

#### HTML, CSS, and JS

- Formatted using [this](https://webformatter.com/html) online tool

### Testing documentation

Testing documentation is provided in [here](TestingDocumentation.md)

Our team decided to test most of the web application by hand. This decision was reached because the app wasn't deemed to be complex enough. 


## Team members

Titas Janusonis,
Andreas E. Andreadis,
Bartlomiej Buba,
Areesh Imran,
Aidan Walton

## Licence 

[LICENSE](LICENSE)

