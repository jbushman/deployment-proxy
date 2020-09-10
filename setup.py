# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="dproxy",
    version="0.0.1",
    author="Jacob Bushman",
    author_email="jacob.matthew.bushman@endurance.com",
    description="Deployment Proxy API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://stash.endurance.com/projects/DEVOPS/repos/deployment_client/browse",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: Apache 2.0",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "python-dotenv",
        "requests",
        "flask",
        "gunicorn"
    ],
    scripts=["dproxy/dproxy"],
    python_requires=">=2.7"
)