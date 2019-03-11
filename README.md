![PyPI](https://img.shields.io/pypi/v/zipit.svg)

# zipit

Very thin wrapper around zipapp that let's you package a python module and dependencies.

### Example
We'll use our demo "app" to showcase zipit.

First, let's take a look at what our app contains:
```
$ cd demo
$ ls app
__main__.py  requirements.txt
```

Our "app" contains two files:
1. `__main__.py`: This is the entrypoint to our app.
2. `requirements.txt`: This is a classic requirements file as consumed by pip.

#### Getting things set up
First we need to install the dependencies for our app. zipit doesn't much care how dependencies are installed. We just need to keep track of where they're installed.

Let's use pip:
```
mkdir deps
$ python3 -m pip install -r app/requirements.txt --target deps
```

#### zipit
Once the dependencies are installed, we can let zipit do it's work:
```
cd ..
$ python3 -m zipit demo/app -d demo/deps
```

This will produce `.pyz` file runable with python.
```
$ python3 app.pyz
Hello, World!
```
