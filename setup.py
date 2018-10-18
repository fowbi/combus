import re
from setuptools import setup, find_packages


def read(file_location: str) -> str:
    with open(file_location, 'r') as handle:
        return handle.read()


def find_version() -> str:
    version_file = read('combus/__init__.py')
    result = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    return result.group(1)


setup(
    name='combus',
    version=find_version(),
    description='Command & Handle',
    long_description=read('README'),
    license='MIT',
    author='Fowbi',
    author_email='tobi@magier.be',
    url="https://github.com/fowbi/combus",
    packages=find_packages(),
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
    ]
)
