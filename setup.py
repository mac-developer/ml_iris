"""Project setup."""
from pathlib import Path
from setuptools import setup
from setuptools import find_packages

from pip.req import parse_requirements
from pip.download import PipSession


def requirements(filename):
    """Parse requirements from requirements.txt."""
    path = str(Path(filename))
    reqs = parse_requirements(path, session=PipSession())
    return [str(req.req) for req in reqs]


setup(
    name='iris',

    version=Path('VERSION').read_text().strip(),

    description='Machine Learning - Iris',
    long_description=Path('README.md').read_text(),

    author='Alejandro Castaño Gonzalez',
    author_email='acgonzalez@sipay.es',

    url='https://github.es',

    classifiers=[
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ],

    package_dir={'': 'src'},
    packages=find_packages('src', exclude=('tests',)),

    entry_points={'console_scripts': ['iris=iris:main']},

    setup_requires=['pytest-runner'],
    tests_require=requirements('test-requirements.txt'),
    install_requires=requirements('requirements.txt'),
    dependency_links=[],

    data_files=[],
    include_package_data=True,
    zip_safe=False
)
