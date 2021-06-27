# Generate BUILD from pipdeptree

## Table of Content

1. Generate [plz.build](http://plz.build) BUILD file of all packages in a virtual environment
2. Generate [plz.build](http://plz.build) BUILD file of a package and its dependencies
- Other Procedure

## Pre-requisite

1. Activate virtual environment into the project
2. Package `pipdeptree` installed inside the virtual environment

## Generate [plz.build](http://plz.build) BUILD file of all packages in a virtual environment

Generating a BUILD file from all packages inside a virtual environment.
This can be used for :

- When you have all required packages of a project (for example, inside a `requirements.txt`) and you want to generate `pip_library()` of all the packages and its dependencies into a BUILD file for [please.build](http://please.build) or [plz.build](http://plz.build).

### Usage

- Variables
    - `ENV_NAME` : the name of the virtual environment containing the dependencies. By default is `venv`.
    - `PYTHON_PACKAGE` : the name of the python interpreter inside the virtual environment. By default is `python`.
- **Note**: To generate `pip_library()` for the packages into the BUILD file, make sure that
    1. You have virtual environment activated with the same name as the `ENV_NAME`
    2. Have `pipdeptree` installed inside the virtual environment
- Generating the BUILD file
    1. Running the python file and it will generate a BUILD file 

        ```bash
        (venv)$ python build_dep_venv_generator.py
        ```

## Generate [plz.build](http://plz.build) BUILD file of a package and its dependencies

Generating a BUILD file for only one package inside a virtual environment.
This can be used for :

- When you want to generate `pip_library()` for only one specific package and its dependencies into a BUILD file for [please.build](http://please.build) or [plz.build](http://plz.build).

### Usage

- Required Variables
    - `PACKAGE_NAME` : the name of the package that
- **Note**: To generate `pip_library()` for the packages into the BUILD file, make sure that
    1. You have virtual environment activated with the same name as the `ENV_NAME`
    2. Have `pipdeptree` installed inside the virtual environment
    3. Have the package specified in `PACKAGE_NAME` variable installed inside the virtual environment
- Generating the BUILD file
    1. Install the specified package in the virtual environment

        ```bash
        # Example
        pip install flask 
        ```

    2. Provide the package name in `build_package_venv_generator.py`

        ```python
        # Example
        PACKAGE_NAME = 'flask'
        ```

    3. Running the python file and it will generate a BUILD file 

        ```bash
        (venv)$ python build_package_venv_generator.py
        ```

## Other Procedure

### Activate a virtual environment

```bash
python3 -m virtualenv venv
source venv/bin/activate
```

### Install `pipdeptree`

```jsx
(venv)$ pip install pipdeptree
```

### Install pip-autoremove

```bash
pip install pip-autoremove
```