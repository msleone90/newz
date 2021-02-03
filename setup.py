import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "docs/README.md").read_text()
 
setup(
    name="newz",
    version="1.0.2",  # look up bumpversion when you start increasing this.
    description="Local news delivered straight to your terminal",
    long_description=README,
    long_description_content_type="text/markdown",
    author='Michael Leone',
    author_email='msleone90@gmail.com',
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=['newz'],
    include_package_data=True,
    entry_points={
        # you need a function with the name after ":" in your script:
        'console_scripts': ['newz = newz.newz:run'],
    }
)