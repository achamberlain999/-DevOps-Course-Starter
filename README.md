# DevOps Apprenticeship: Project Exercise

Live site: https://alecha-softwire-tasko.azurewebsites.net/
Docker image: https://hub.docker.com/repository/docker/alechasoftwire/todo-app/general

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.7+ and install Poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Note if you are on Mac, you may need to execute `Install Certificates.command` in the Python folder before installing poetry. You may need to run this as `sudo`.

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

## Docker

Tasko uses Docker to containerise our web app for easy deployment to the cloud. For information on how Docker is set up in this project, see the dedicated [Docker page](docs/docker.md).

## Manual Release

For information on how to do a manual release to Azure Web App, see [Manual Release](docs/release_process.md).

## Security

For information of the security of the application, see [Security](docs/security.md).