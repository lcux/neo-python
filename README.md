# neo-python: Python SDK for NEO platform

In progress, please reach out in order to contribute

## Getting started

make a python 3 virtual environment, and activate it
```
python3 -m venv venv
source venv/bin/activate
```

then install requirements
```
pip install -r requirements.txt
```


### Installing on OSX

if you're having an issue similar to this:

```
    from ._plyvel import (  # noqa
    ImportError: dlopen(neo-python/venv/lib/python3.5/site-packages/plyvel/_plyvel.cpython-35m-darwin.so, 2): Symbol not found: __ZN7leveldb2DB4OpenERKNS_7Options
    ERKSsPPS0_
    Referenced from: neo-python/venv/lib/python3.5/site-packages/plyvel/_plyvel.cpython-35m-darwin.so
    Expected in: flat namespace
```

You may need to uninstall plyvel (python libleveldb library), and reinstall with the following cflags

```
pip uninstall plyvel
CFLAGS='-mmacosx-version-min=10.7 -stdlib=libc++' pip install --no-use-wheel plyvel --no-cache-dir
```

## Running

After installing requirements and activating your environment, there is an easy to use `cli.py` file for you to run

```
python cli.py 
```

That should do some stuff.  Not fully functional yet

## Tests

Tests are important.  Currently there are not enough, but we are working on that.  You can start them by running this command

```
python -m unittest discover neo 
```

To run tests with `coverage`, use the following 
```
coverage run -m unittest discover neo
```

After that, you can generate a command line coverage report use the following:
```
coverage report -m --omit=venv/*
```
