|Build Status| |codecov| |requirements| |PyPI|

Click Pathlib
=============

A Python ``click`` type which is similar to ``click.Path`` but returns a ``Pathlib.Path``.

.. contents::

Installation
------------

.. code:: console

   $ pip install click-pathlib

This supports Python 3.5+.

Usage
~~~~~

.. code:: python

   import click
   import click_pathlib
   
   @click.command('delete')
   @click.argument(
       'existing_file',
       type=click_pathlib.ClickPathlibPath(exitst=True),
   )
   def delete(existing_file):
       existing_file.unlink()

Credits
-------

Thanks to `@jeremyh`_ for describing this solution on GitHub at https://github.com/pallets/click/issues/405#issuecomment-470812067.

Contributing
------------

See `CONTRIBUTING.rst <./CONTRIBUTING.rst>`_.

.. |Build Status| image:: https://travis-ci.com/adamtheturtle/click-pathlib.svg?branch=master
    :target: https://travis-ci.com/adamtheturtle/sphinx-substitution-extensions
.. _@jeremyh: https://github.com/jeremyh
.. |codecov| image:: https://codecov.io/gh/adamtheturtle/click-pathlib/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/adamtheturtle/click-pathlib
.. |requirements| image:: https://requires.io/github/adamtheturtle/click-pathlib/requirements.svg?branch=master
     :target: https://requires.io/github/adamtheturtle/sphinx-substitution-extensions/requirements/?branch=master
     :alt: Requirements Status
.. |PyPI| image:: https://badge.fury.io/py/Sphinx-Substitution-Extensions.svg
    :target: https://badge.fury.io/py/Sphinx-Substitution-Extensions