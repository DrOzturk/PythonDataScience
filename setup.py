from setuptools import setup, find_packages


def readme():
    with open('README.md') as f:
        return f.read()

# USAGE: to Create the file to distribute: dist/example_package-0.0.1.tar.gz (dist/<ProjectName>-<version>.tar.gz)
#     python setup.py sdist
#
# For More info type:
#     python setup.py --help-commands
setup(name='example_package',
      version='0.0.1',
      description='A sample package to show how libraries are packaged in python',
      url='http://tinyurl.com/PythonStarter',
      author='Ozgur Ozturk',
      author_email='',
      license='MIT',
      packages = find_packages(),
      install_requires=[
          'numpy',
      ],
      zip_safe=True)