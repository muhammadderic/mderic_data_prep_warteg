from setuptools import setup, find_packages

setup(
    name='mderic_data_prep_warteg',
    version='0.2.0',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
    ],
    author='muhammadderic',
    description='a Python library designed to simplify and automate the data preparation process',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
    ],
    python_requires='>=3.7',
)
