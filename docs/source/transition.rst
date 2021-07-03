Transition to ``pydoctor``
==========================


From ``epydoc``
---------------

If you are looking for a successor to ``epydoc`` after moving to Python 3, ``pydoctor`` is the right tool for your project!

- ``pydoctor`` dropped support for the ``X{}`` tag. All other epytext markup syntax should be fully supported.

From ``pdoc3``
--------------

- ``pydoctor`` do not support Markdown docstrings. The easiest is to use *restructuredtext* docstring format as they are sharing numerous markup syntax.

- ``pydoctor`` can only generate HTML, if you are using Markdown output, consider using ``pdocs``.

- All references to ``__pdoc__`` module variable should be deleted as they are not supported. If you dynamically generated documentation, you should create a separate script and include it's output with an ``.. include::`` directive.
