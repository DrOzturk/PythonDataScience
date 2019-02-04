# PythonDataScience with pipenv
Starter data science project using Python with common dependencies included...  
Pull requests welcome...
```bash
# clone this repo to local
git clone git@github.com:DrOzturk/PythonDataScience.git
# if you don't have python 3 as default, first do this
pipenv --three
# create virtual environment with dependencies defined in Pipenv file
pipenv install
# start shell in that virtual environment
pipenv shell
```

# Adding new dependencies
If you add the new dependency using pipenv, it will be automatically added to Pipfile.
ex:
```bash
pipenv install pandas
```
# Developer Tools
## Linting
- pycodestyle <filename>: use to check if code complies with code style guide
ex: 
```bash
pycodestyle example_package/example.py
```

## Setuptools
- Command to Create the package to distribute in dist folder <ProjectName>-<version>.tar.gz (like dist/example_package-0.0.1.tar.gz)
```bash
python setup.py sdist
```
- For More info type:
```bash
python setup.py --help-commands
```

- helps in module discovery using find_packages(), so we can refer to all modules without relative import

## Unit Test Running
- Running all unit tests in the command line:
```bash
python -m unittest -v example_package/tests/test_example.py`
```
- Running a specific test in a TestExample class in test_example test module:
```bash
python -m unittest example_package.tests.test_example.TestExample.test_greater_than
```

## Clean Compiled
find . -type f -name "*.py[co]" -delete -or -type d -name "__pycache__" -delete

.gitignore 
