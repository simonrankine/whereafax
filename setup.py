from __future__ import print_function
from setuptools import setup
import os


def is_package(path):
    return (
        os.path.isdir(path) and
        os.path.isfile(os.path.join(path, '__init__.py'))
        )


def find_packages(path, base=""):
    """ Find all packages in path """
    packages = {}
    for item in os.listdir(path):
        dir = os.path.join(path, item)
        if is_package(dir):
            if base:
                module_name = "%(base)s.%(item)s" % vars()
            else:
                module_name = item
            packages[module_name] = dir
            packages.update(find_packages(dir, module_name))
    return packages


packages = find_packages(".")
package_names = packages.keys()

packages_required = [
    "six==1.10.0",
]

setup(name="whereafax",
      version="0.0.0",
      description="Whereafax tti file generator",
      url='https://github.com/simonrankine/whereafax',
      author='Simon Rankine',
      author_email='simon@rankine.me',
      license='NPOSL-3.0',
      packages=package_names,
      package_dir=packages,
      install_requires=packages_required,
      scripts=[],
      data_files=[],
      long_description="""
      This is a Python library that may be used to generate TTI
      files commonly used to store pages for the Teletext television
      information retreival service.
      """
      )
