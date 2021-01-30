Description
-----------

This is an experimental library which tries to expose hyperspace RPC from Python.

Build
-----

Dependencies: Python 3.6 (or greater), poetry, make.

::

    make

Usage (draft)
-------------

::

    >>> import hyperspace_rpc as h
    >>> import grpc
    >>> channel = grpc.insecure_channel('unix:///tmp/hyperspace.sock')
