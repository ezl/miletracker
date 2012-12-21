.. 

miletracker
======================

Quickstart
----------

To bootstrap the project::

    virtualenv miletracker
    source miletracker/bin/activate
    cd path/to/miletracker/repository
    pip install -r requirements.pip
    pip install -e .
    cp miletracker/settings/local.py.example miletracker/settings/local.py
    manage.py syncdb --migrate

Documentation
-------------

Developer documentation is available in Sphinx format in the docs directory.

Initial installation instructions (including how to build the documentation as
HTML) can be found in docs/install.rst.
