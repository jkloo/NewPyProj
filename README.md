NewPyProj
======

[![Build Status](https://travis-ci.org/jkloo/NewPyProj.png?branch=master)](https://travis-ci.org/jkloo/NewPyProj)
[![Coverage Status](https://coveralls.io/repos/jkloo/NewPyProj/badge.png?branch=master)](https://coveralls.io/r/jkloo/NewPyProj?branch=master)


Installation
------------

Create a virtualenv:

    make env

Run the tests:

    make test
    make tests  # includes integration tests

Build the documentation:

    make doc

Run static analysis:

    make pep8
    make pylint
    make check  # pep8 and pylint

Prepare a release:

    make dist  # dry run
    make upload
