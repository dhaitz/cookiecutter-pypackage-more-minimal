{{ cookiecutter.package_name }}
{{ cookiecutter.package_name|count * "=" }}

{% if cookiecutter.readme_pypi_badge -%}
.. image:: https://img.shields.io/pypi/v/{{ cookiecutter.package_name }}.svg
    :target: https://pypi.python.org/pypi/{{ cookiecutter.package_name }}
    :alt: Latest PyPI version
{%- endif %}

{% if cookiecutter.add_travis -%}

""
.. image:: https://travis-ci.org/{{ cookiecutter.username }}/{{ cookiecutter.package_name.replace('_', '-') }}.png
   :target: https://travis-ci.org/{{ cookiecutter.username }}/{{ cookiecutter.package_name.replace('_', '-') }}
   :alt: Latest Travis CI build status
{%- endif %}

{{ cookiecutter.package_description }}

Usage
-----



testpypi:
    twine upload --repository-url https://test.pypi.org/legacy/ dist/*
travis:
    check
readthedocs
 # connect



Installation
------------

Requirements
^^^^^^^^^^^^

Compatibility
-------------

Licence
-------

Authors
-------

`{{ cookiecutter.package_name }}` was written by `{{ cookiecutter.author_name }} <{{ cookiecutter.author_email }}>`_.
