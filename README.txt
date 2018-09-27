skeleton
========

Getting Started
---------------

- Change directory into your newly created project.

    cd skeleton

- Create a Python virtual environment.

    python3 -m venv env

- Upgrade packaging tools.

    env/bin/pip install --upgrade pip setuptools

- Install the project in editable mode with its testing requirements.

    env/bin/pip install -e ".[testing]"

- Configure the database.

    env/bin/initialize_skeleton_db development.ini

- Run your project's tests.

    env/bin/pytest

- Run your project.

    env/bin/pserve development.ini

For Setting up Postgres DB
---------------

- Install Postgres.

    sudo apt-get update
    sudo apt-get install postgresql postgresql-contrib

- Ingresar a la cuenta con el usuario

    sudo -i -u {username}  # example postgres
    psql # para conectarse a la base de datos por defecto, (una vez ingresado en la cuenta)
    sudo -u {username} psql # para conectarse directamente (sin haber ingresado a la cuenta)


- Crear base de datos

    createdb skeleton

- Crear usuario

    createuser --interactive # logged
    sudo adduser skeleton

- Utilidades

    \l # para listar las bd
    \q # para salir de la base de datos
