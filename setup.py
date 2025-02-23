#!/usr/bin/env python
from setuptools import find_packages, setup


def get_install_requires():
    """
    parse requirements.txt, ignore links, exclude comments
    """
    requirements = []
    for line in open('requirements.txt').readlines():
        # skip to next iteration if comment or empty line
        skip = (
            line.startswith('#')
            or line == ''
            or line.startswith('http')
            or line.startswith('git')
        )
        if skip:
            continue
        # add line to requirements
        requirements.append(line)
    return requirements


setup(
    name="django-filemanager",
    version="0.0.3",
    author="Information Management Group; Talana",
    author_email="img.iitr.img@gmail.com",
    description="A file manager for Django",
    license="MIT",
    packages=["filemanager"],
    install_requires=get_install_requires(),
    zip_safe=False,
    include_package_data=True,
    package_data = {
      "filemanager":["static/*", "templates/*","*.html", "*.css", "*.js", "*.png"]
    },
    test_suite='tests.main',
)
