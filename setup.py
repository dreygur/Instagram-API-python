from setuptools import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='InstagramAPI',
    version='1.0.2',
    description='Unofficial instagram API, give you access to ALL instagram features (like, follow, upload photo and video and etc)! Write on python.',
    url='https://github.com/LevPasha/Instagram-API-python/',
    author='Pasha Lev',
    author_email='levpasha@gmail.com',
    license='GNU',
    packages=['InstagramAPI'],
    zip_safe=False,
    install_requires=requirements,
    python_requires='>=3.6'
)
