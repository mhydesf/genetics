from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name="genetic_programming_lib",
    version="1.0",
    description="Genetic Programming Python Lib",
    author="Mikhail Hyde",
    author_email="hyde.mikhail@gmail.com",
    packages=find_packages(),
    install_requires=requirements,
)

