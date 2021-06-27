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