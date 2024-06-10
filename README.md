
# EPB

  

## Setup

  

The first thing to do is to clone the repository:

  

```sh

$  git  clone  https://github.com/ajxv/EPB.git

$  cd  epb

```

  

Create a virtual environment to install dependencies in and activate it:

  

```sh

$  python3  -m  venv  .env

//  activate  env  in  linux

$  source  env/bin/activate

//  or  for  windows:

$  .env/Scripts/activate

```

  

Then install the dependencies:

  

```sh

(.env)$  pip  install  -r  requirements.txt

```

Note the `(.env)` in front of the prompt. This indicates that this terminal

session operates in a virtual environment set up by `virtualenv`.

  

Once `pip` has finished downloading the dependencies:

```sh

(.env)$  cd  project

(.env)$  python  manage.py  runserver

```

And navigate to `http://127.0.0.1:8000/`.
