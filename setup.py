from setuptools import setup, find_packages


package_name = 'aiostorage'
long_description = (
    'Interface for performing common object storage operations '
    'asynchronously. The aim is to support multiple object storage '
    'providers, e.g. Google Cloud, Backblaze, etc.'
)
version = '0.1.2'
classifiers = [
    'Development Status :: 1 - Planning',

    'Intended Audience :: Developers',

    'Programming Language :: Python :: 3.6',
]
requirements = (
    'aiohttp>=2.0,<3.0',
)
project_urls = {
    'Wiki': 'https://family-guy.github.io/aiostorage-wiki/',
    'Source': 'https://github.com/family-guy/aiostorage.git',
    'Tracker': 'https://github.com/family-guy/aiostorage/issues',
}

setup(
    name=package_name,
    description='Asynchronous object storage',
    long_description=long_description,

    version=version,
    packages=find_packages(exclude=('tests', )),

    install_requires=requirements,
    classifiers=classifiers,

    author='Guy King',
    author_email='guy@zorncapital.com',
    license='MIT',
    url='https://github.com/family-guy/aiostorage.git',
    project_urls=project_urls,
)
