.. enviropy documentation master file, created by
   sphinx-quickstart on Thu Feb 23 01:53:38 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Enviropy: statistical methods and plotting tools for environmental data
=======================================================================

Right now this is a fun project to learn Python with the goal of having a 
convenient package for storing and analyzing environmental data.   

--------------------

A quick overview
----------------

Connect to external data sources
    >>> from enviropy.external import read_manages3, read_gint
    >>> read_manages3('C:\path\to\Site.mdb')
    >>> read_gint('C:\path\to\gint.gpj')

The User Guide
--------------

A user guide is planned...

.. toctree::
   :maxdepth: 2

   user/install
   user/quickstart
   user/advanced

The API Documentation
---------------------

Specifics on functions, classes, and methods will go here...

.. toctree::
   :maxdepth: 2

   enviropy 

The Contributor Guide
---------------------

Contributions are encouraged and welcomed...

.. toctree::
   :maxdepth: 2

   dev/contributing
