# Virtual Environments

Why use a virtual environment?

> To have a space where we can install packages specific to that project

## venv

`venv` is a built in package that comes with python that handles virtual environments

**Create a new virtual environment**:
`python -m venv name(name usually=venv)`

### To run the virtual environment:

`./project_env/Script/activate`

You can tell the environment is activated by looking at the project name in parenthesis before the current directory:
`(project_env) PS C:\Users\tsl\Desktop\project_env>`

### Deactivate

To disable the virtual environment, simply type `deactivate` into the terminal.

## Requirement.txt

### Freeze

If you need to capture the packages installed in an environment:
`pip freeze requirements.txt`

### Install

To install all packages from a `requirements.txt` file, use the following command:
`pip install -r requirements.txt`

## Creating files

-   When you add files to your project, you don't want to create them inside the venv folder.
-   Also don't commit the venv folder to git - add to gitignore
-   DO commit requirements.txt

## Using system packages inside a virtual environment

`python -m venv venv --system-site-packages`
