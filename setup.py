from setuptools import setup
 
setup(
    name="newz",
    version="0.0.1",  # look up bumpversion when you start increasing this.
    author='Michael Leone',
    author_email='msleone90@gmail.com',
    packages=['newz'],
    entry_points={
        # you need a function with the name after ":" in your script:
        'console_scripts': ['newz = newz.newz:run'],
    }
)