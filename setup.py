import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="paramarg",
    version="0.1.0",
    description="Get Parameters from Argumen",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/Malykz/paramarg",
    author="Luthfi Malik",
    author_email="kaplingtumbal@gmail.com",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.11",
    ],
    packages=["param"],
    include_package_data=False,
)