import subprocess, json

from lib.build_string_formatter import get_pip_library_string


""" 
Generate a BUILD file for please.build from a provided python packages and its dependencies
 """
# Provide package name here
PACKAGE_NAME = "flask"

# virtual environment
ENV_NAME = "venv"
PYTHON_PACKAGE = "python"
PYTHON_ENV_PATH = "./{0}/bin/{1}".format(ENV_NAME, PYTHON_PACKAGE)
# output file
FILE_NAME = "BUILD"
FILE_PATH = "./{}".format(FILE_NAME)
# temporary json file
TEMP_FILE = "./temporary.json"


def main():

    # writing output to a temporary json
    with open(TEMP_FILE, "w") as temp_json:
        try:
            command = [
                PYTHON_ENV_PATH,
                "-m",
                "pipdeptree",
                "-p",
                PACKAGE_NAME,
                "--json",
            ]
            subprocess.run(command, stdout=temp_json)
        except Exception:
            print(
                "Please check if the virtual environment name is the same as ENV_NAME or the python interpreter is the same as PYTHON_PACKAGE"
            )
            exit()
    # read pipdeptree output from json and generate BUILD file
    with open(TEMP_FILE, "r") as dep_json, open(FILE_PATH, "w") as build_file:
        try:
            packages = json.load(dep_json)
            if len(packages) == 0:
                print(
                    "Please check if package {} is installed in the virtual environment".format(
                        PYTHON_PACKAGE
                    )
                )
            for package in packages:
                package_name = package["package"]["key"]
                package_version = package["package"]["installed_version"]
                dependencies = [s["key"] for s in package["dependencies"]]
                # write the pip_library string to BUILD
                build_file.write(
                    get_pip_library_string(
                        dependencies, package_name, package_version
                    )
                )
        except Exception:
            print(
                "Please check if pipdeptree is installed in the virtual environment"
            )


if __name__ == "__main__":
    main()
