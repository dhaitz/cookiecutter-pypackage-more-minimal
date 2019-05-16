#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    https://github.com/audreyr/cookiecutter/issues/723#issuecomment-350561930
"""

import os
import shutil


def remove(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)
    else:
        print("Cannot remove", filepath)


if __name__ == '__main__':

    create_travis_file = '{{cookiecutter.create_travis_file}}' == 'y'

    if not create_travis_file:
        filepath = '.travis.yml'
        remove(filepath)
