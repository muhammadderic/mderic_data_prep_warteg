from setuptools import setup, find_packages

setup(
    name='mderic_data_prep_warteg',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'kaggle',
        'matplotlib',
        'seaborn',
        'ydata-profiling'  # optional, for profiling
    ],
    author='muhammadderic',
    description='Modular tools for data collection, understanding, and preparation',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
    ],
    python_requires='>=3.7',
)
