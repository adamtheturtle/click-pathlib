|Build Status| |codecov| |PyPI|

Deprecation Notice
==================

   **DEPRECATED**

   This package is no longer needed with Click >= 8.0.0.
   In those versions of Click, The ``Path`` param type can be passed:
   ``path_type=pathlib.Path`` to return a path object instead of a string.


Click Pathlib
=============

A Python ``click`` type which is similar to ``click.Path`` but returns a ``Pathlib.Path``.

.. contents::

Installation
------------

.. code:: console

   $ pip install click-pathlib

This supports Python 3.7+.

Usage
~~~~~

Use the ``click_pathlib.Path`` just like a click.Path_ type and your function will receive a ``pathlib.Path``.

.. code:: python

   import click
   import click_pathlib

   @click.command('delete')
   @click.argument(
       'existing_file',
       type=click_pathlib.Path(exists=True),
   )
   def delete(existing_file):
       existing_file.unlink()

.. _click.Path: https://click.palletsprojects.com/en/7.x/api/#click.Path

Credits
-------

Thanks to `@jeremyh`_ for describing this solution on GitHub at https://github.com/pallets/click/issues/405#issuecomment-470812067.

Contributing
------------

See `CONTRIBUTING.rst <./CONTRIBUTING.rst>`_.

.. |Build Status| image:: https://github.com/adamtheturtle/click-pathlib/workflows/CI/badge.svg
   :target: https://github.com/adamtheturtle/click-pathlib/actions
.. _@jeremyh: https://github.com/jeremyh
.. |codecov| image:: https://codecov.io/gh/adamtheturtle/click-pathlib/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/adamtheturtle/click-pathlib
.. |PyPI| image:: https://badge.fury.io/py/click-pathlib.svg
   :target: https://badge.fury.io/py/click-pathlib
