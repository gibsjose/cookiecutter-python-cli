## What is this?

A default template for a new CLI project, written in Python.  Deals with all
the boilerplate involved in the setuptools setup, etc.


## How do I use this?

Here's my preferred path to bliss:

1. Start by installing `pipsi`.  It's awesome.
   [Instructions here.](https://github.com/mitsuhiko/pipsi#readme)
2. Now install Cookiecutter:
   `$ pipsi install cookiecutter`.
3. Now use Cookiecutter to create your brand new project:
   `$ cd ~/Desktop && cookiecutter https://github.com/gibsjose/cookiecutter-python-cli.git`


## How to answer these questions?

When running Cookiecutter, you'll need to provide some values.
Here's what they're for:

* `project_name` -- "Some Project"      (Used for marketing.  Keep it short and capitalize accordingly.)
* `repo_name` -- "some-project"         (Name of the GitHub repo.)
* `pypi_name` -- "some-project"         (Name on PyPI, i.e. what people type to `pipsi install`.)
* `script_name` -- "some-project"       (Binary of the script, i.e. what people will run on the command line.)
* `package_name` -- "some_project"      (Name of the Python module/package used internally.)


## License

Liberally licensed under BSD terms.
