.. highlight:: shell

============
Installation
============


Stable release
--------------

To install {{ cookiecutter.package_name }}, run this command in your terminal:

.. code-block:: console

    $ pip install {{ cookiecutter.package_name }}

This is the preferred method to install {{ cookiecutter.package_name }}, as it will always install the most recent stable release.

If you don't have `pip`_ installed, this `Python installation guide`_ can guide
you through the process.

.. _pip: https://pip.pypa.io
.. _Python installation guide: http://docs.python-guide.org/en/latest/starting/installation/


From sources
------------

The sources for {{ cookiecutter.package_name }} can be downloaded from the `Github repo`_.

You can either clone the public repository:

.. code-block:: console

    $ git clone git://{{ cookiecutter.package_url }}

Or download the `tarball`_:

.. code-block:: console

    $ curl  -OL {{ cookiecutter.package_url }}/tarball/master

Once you have a copy of the source, you can install it with:

.. code-block:: console

    $ python setup.py install


.. _Github repo: {{ cookiecutter.package_url }}
.. _tarball: {{ cookiecutter.package_url }}/tarball/master
