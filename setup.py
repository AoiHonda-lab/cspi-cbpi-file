from setuptools import setup, find_packages

setup(
    name='neural-coalition-index',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'scikit-learn',
        'matplotlib',
    ],
)
