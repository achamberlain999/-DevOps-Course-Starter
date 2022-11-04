# DevOps Apprenticeship: Project Exercise

> If you are using GitPod for the project exercise (i.e. you cannot use your local machine) then you'll want to launch a VM using the [following link](https://gitpod.io/#https://github.com/CorndelWithSoftwire/DevOps-Course-Starter). Note this VM comes pre-setup with Python & Poetry pre-installed.

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.7+ and install Poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py -UseBasicParsing).Content | python -
```

## Dependencies

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:

```bash
$ poetry install
```

You'll also need to clone a new `.env` file from the `.env.template` to store local configuration options. This is a one-time operation on first setup:

```bash
$ cp .env.template .env  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change). There's also a [SECRET_KEY](https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY) variable which is used to encrypt the flask session cookie. You should update the secret key in `.env` to a random guid.

## Trello

The app uses Trello as a 'database' to store cards.

1. [Sign up](https://trello.com/signup) for Trello if you don't already have an account
1. Get your [API_KEY](https://trello.com/app-key) and set it in `.env` as `TRELLO_API_KEY`
1. On the same page, generate an API_TOKEN and set it in `.env` as `TRELLO_API_TOKEN`
1. Run `python3 trello-set-up.py` which will create a Trello board with the correct lists
1. Use the output of this job to set` TRELLO_BOARD_ID` in `.env`

## Running the App

Once the all dependencies have been installed, start the Flask app in development mode within the Poetry environment by running:
```bash
$ poetry run flask run
```

You should see output similar to the following:
```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 226-556-590
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

## Tests

Testing framework: [pytest](https://docs.pytest.org/)

### Running the tests

Run `poetry run pytest`. To run a specific test suite, run `poetry run pytest -k "TestClassName"`.

### Adding tests

1. Tests are found in `todo_app/tests/`
1. If you are testing a new class
    - Add a new file with name `test_CLASS_FILE_NAME.py`, e.g. `test_homepage_view_model.py`.
    - Add a new class within the file called `Test{ClassName}`
1. Add test methods to the test class, prefixing each with `test_` so they are picked up by pytest

## SSH

### SSH config

To make it easier to ssh into the boxes, copy the following into your `.ssh/config` file:
```
Host devops-c
    HostName CONTROL_NODE_IP_ADDRESS
    User ec2-user
    IdentityFile ~/.ssh/KEY_NAME

Host devops-m
    HostName MANAGED_NODE_IP_ADDRESS
    User ec2-user
    IdentityFile ~/.ssh/KEY_NAME
```
replacing the IP_ADDRESSes and KEY_NAME with those relevant to you.

Then run: `ssh-copy-id ec2-user@devops-c` and `ssh-copy-id ec2-user@devops-m`

You'll be instructed to enter the password for `ec2-user`, after which you'll be able to ssh in using just `ssh devops-c` and `ssh-devops-m`.

### SSH config in the control node

Copy the step above while ssh-ed into the control node (you'll only need the managed node ssh config).
This will allow you to ssh from the managed node into the control node easily.

## Ansible

Ansible files are found in `/ansible`.

### Copying ansible files to the control node

Run
```
scp ansible/file_name devops-c:file_name
```
This will copy the file to the home directory of `ec2-user`. If you need to move it within the server then you can use `mv`.

### Run the playbook

To run the ansible playbook to configure the webservers, ssh into the control node and run
```
ansible-playbook configure-webservers.yaml
```