from setuptools import setup, find_packages

with open ("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="test_t_uma_amostra",
    version="0",
    author="Zeygler",
    packages=find_packages(),
    install_requires=requirements,
)