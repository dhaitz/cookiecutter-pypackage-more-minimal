#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    https://github.com/audreyr/cookiecutter/issues/723#issuecomment-350561930
"""

import os
import shutil
from pathlib import Path
import pypandoc

# ToDo is there a better way to check for truth?
TRUE_ANSWERS = ['True', True, 'y', 'true', 'yes']


def remove(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)
    else:
        print("Cannot remove", filepath)


if __name__ == '__main__':

    add_travis = '{{cookiecutter.add_travis}}' in TRUE_ANSWERS
    if not add_travis:
        filepath = '.travis.yml'
        remove(filepath)

    if '{{cookiecutter.add_extended_documentation}}' not in TRUE_ANSWERS:
        # convert README.rst to .md
        readme_md = pypandoc.convert_file('README.rst', 'md', format='rst')
        Path('README.md').open('w').write(readme_md)
        remove('README.rst')

        # remove docs folder
        remove('docs')
