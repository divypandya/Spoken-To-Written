import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def open_file(fname):
    return open(os.path.join(os.path.dirname(__file__), fname))

setup(
	  name = 'spokentowritten',
      packages = ['spokentowritten'],
      version='0.1',
      description='Convert Spoken English given as text to Written English ',
      author='Divy Pandya',
      author_email='201751013@iiitvadodara.ac.in',
      url='https://github.com/divypandya/Spoken-To-Written',
	  long_description=open_file('README.rst').read()
)
