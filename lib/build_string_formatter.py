from .global_variables import PYTHON_LIBRARY_FORMAT_WITH_DEPENDENCIES, PYTHON_LIBRARY_FORMAT_WITHOUT_DEPENDENCIES


def get_pip_library_string(dependencies, package_name, package_version):
    """ 
    ARGS:
        - PARAMS1 : a list of required dependencies of a package
        - PARAMS2 : the name/key of the package
        - PARAMS3 : the version of the package
    RETURNS:
        A `pip_library()` string to append to the BUILD file
     """ 

    pip_library_string = ''
    # check if a package requires other dependencies
    if len(dependencies) != 0:
        dependencies_format = '":' + '", ":'.join(dependencies) + '"'
        pip_library_string = PYTHON_LIBRARY_FORMAT_WITH_DEPENDENCIES.format(package_name, package_version, dependencies_format)
    else:
        pip_library_string = PYTHON_LIBRARY_FORMAT_WITHOUT_DEPENDENCIES.format(package_name, package_version)
    return pip_library_string
