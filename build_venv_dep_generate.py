import subprocess, json


# virtual environment
ENV_NAME = 'venv'
PYTHON_PACKAGE = 'python'
PYTHON_ENV_PATH = './{0}/bin/{1}'.format(ENV_NAME, PYTHON_PACKAGE)
# output file
FILE_NAME = 'BUILD'
FILE_PATH = './{}'.format(FILE_NAME)
# temporary json file 
TEMP_FILE = './temporary.json'
# BUILD file format
PYTHON_LIBRARY_FORMAT_WITH_DEPENDENCIES = """pip_library(
    name = "{0}",
    version = "{1}",
    deps = [{2}],
)

"""
PYTHON_LIBRARY_FORMAT_WITHOUT_DEPENDENCIES = """pip_library(
    name = "{0}",
    version = "{1}",
)

"""

# writing output to a temporary json
with open(TEMP_FILE, "w") as temp_json:
    command = [PYTHON_ENV_PATH, '-m', 'pipdeptree', '--json']
    subprocess.run(command, stdout=temp_json)
# read pipdeptree output from json and generate BUILD file
with open(TEMP_FILE, "r") as dep_json, open(FILE_PATH, "w") as build_file:
    packages = json.load(dep_json)
    for package in packages:
        package_name = package['package']['package_name']
        package_version = package['package']['installed_version']
        dependencies = [s['package_name'] for s in package['dependencies']]
        # 
        if dependencies:
            dependencies_format = '":' + '", ":'.join(dependencies) + '"'
            build_file.write(PYTHON_LIBRARY_FORMAT_WITH_DEPENDENCIES.format(package_name, package_version, dependencies_format))
        else:
            build_file.write(PYTHON_LIBRARY_FORMAT_WITHOUT_DEPENDENCIES.format(package_name, package_version))