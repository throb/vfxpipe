from setuptools import setup, find_packages

setup(
    name='image_sequence_finder',
    version='0.1',
    author='Robert Nederhorst',
    author_email='throb@throb.net',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    #url='https://github.com/throb/image_sequence_finder',
    description='A python module that searches a given directory for image sequence files and returns an array of dicts containing the list of sequences found.',
    keywords='image sequence finder',
    classifiers=[],
)