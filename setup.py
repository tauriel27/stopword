#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except (ImportError, IOError):
    long_description = open('README.md').read()

setup(
    name='stopword',
    version='0.0.2',
    description=(
        'Stopwords filter for Chinese'
    ),
    long_description=long_description,
    author='tauriel',
    author_email='taurieli27@outlook.com',
    license='MIT',
    packages=find_packages(),
    package_data={'stopword': ['*.txt']},
    #data_files=[('stopword', ['stopword/stopwords-cn.txt'])],
    platforms=["all"],
    url='https://github.com/tauriel27/stopword',
    classifiers=[
	'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Natural Language :: Chinese (Simplified)',
        'Natural Language :: Chinese (Traditional)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
	'Programming Language :: Python :: 3.6',
	'Programming Language :: Python :: 3.7',
        'Topic :: Text Processing',
        'Topic :: Text Processing :: Indexing',
        'Topic :: Text Processing :: Linguistic',
    ],
    zip_safe=True,
)
