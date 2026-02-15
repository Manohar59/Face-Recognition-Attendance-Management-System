import sys
print("Python executable:", sys.executable)
print("Sys path:", sys.path)
try:
    import setuptools
    print("setuptools version:", setuptools.__version__)
    print("setuptools file:", setuptools.__file__)
except ImportError:
    print("Could not import setuptools")

try:
    import pkg_resources
    print("pkg_resources imported successfully")
except ImportError:
    print("Could not import pkg_resources")
