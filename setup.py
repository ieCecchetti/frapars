from setuptools import setup, find_packages
import frapars

setup(
    name='frapars',
    version=frapars.__version__,
    packages=find_packages(),
    install_requires=[
        # List of dependencies required for your package
    ],
    entry_points={
        'console_scripts': [
            'frapars_test = frapars.script:main'
        ]
    },
    # Metadata
    author='cikossz',
    author_email='ienricocecchetti@gmail.com',
    description='Simple lib for parsing france addresses',
    long_description='Simple lib for parsing france addresses',
    url='https://github.com/ieCecchetti',
    classifiers=[
        'Programming Language :: Python :: 3',
        # Add more classifiers as needed
    ],
)
