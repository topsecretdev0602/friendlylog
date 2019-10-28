from setuptools import find_packages
from setuptools import setup


# Read repository information. This will be used as the package description.
long_description = None
with open("README.md", "r") as fh:
    long_description = fh.read()
assert(long_description is not None)


setup(
    name='friendlylog',
    version='1.0.2',
    description='Python logging for humans: colorful, clean interface, straightforward usage, simply friendly log.',
    author='sebisebi',
    author_email='gpirtoaca@gmail.com',
    url='https://github.com/SebiSebi/friendlylog',
    license='Apache 2.0',
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        'colored>=1.4.0',
        'six>=1.12.0',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Development Status :: 5 - Production/Stable",
        "Topic :: System :: Logging",
    ],
)
