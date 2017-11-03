Pretty logs for local development.

.. code-block:: python

        pip install readable-log-formatter

Provides the class ``readable_log_formatter.ReadableFormatter`` to be used
with Python's logging:

.. code-block:: python

        import logging
        from readable_log_formatter import ReadableFormatter

        log = logging.getLogger()
        log.setLevel(logging.INFO)
        hndl = logging.StreamHandler()
        hndl.setFormatter(ReadableFormatter())
        log.addHandler(hndl)

.. image:: https://raw.githubusercontent.com/ipmb/readable-log-formatter/master/.screenshot.png
    :alt: readable-log-formatter screenshot
