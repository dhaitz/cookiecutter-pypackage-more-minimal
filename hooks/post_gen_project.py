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

    # convert README.rst to .md
    if '{{cookiecutter.readme_in_markdown}}' in TRUE_ANSWERS:
        readme_md = pypandoc.convert('README.rst', 'md', format='rst')
        Path('README.md').open('w').write(readme_md)
        remove('README.rst')
