import os
import re

from setuptools import find_packages, setup

BASE_DIR = os.path.dirname(os.path.realpath(__file__))


def _refine_description(desc):
    desc = re.sub(r".. raw::.*", "", desc)
    desc = re.sub(r"<img .*", "", desc)
    return desc


def readme():
    long_description = ""
    with open(os.path.join(BASE_DIR, "README.rst")) as f:
        long_description += f.read()

    long_description += "\n\n"
    with open(os.path.join(BASE_DIR, "CHANGELOG.rst")) as f:
        long_description += f.read()

    long_description = _refine_description(long_description)
    return long_description


def get_version():
    version = {}
    with open("version.py") as fp:
        exec(fp.read(), version)
    return version["__version__"]


setup(
    name="dashamail",
    description="DashaMail API client for Python",
    long_description=readme(),
    long_description_content_type="text/x-rst",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Topic :: Office/Business",
    ],
    author="Vitaly Samigullin",
    author_email="vrs@pilosus.org",
    url="https://github.com/pilosus/python-dashamail/",
    version=get_version(),
    license="Apache License 2.0",
    python_requires=">=3.6,<4",
    zip_safe=False,
    include_package_data=True,
    packages=find_packages(exclude=["tests"]),
    install_requires=["requests>=2.0,<3"],
)
