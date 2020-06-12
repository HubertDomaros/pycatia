Examples
========

The module pycatia must already be installed. CATIA sample files are available within the `github <https://github.com/evereux/pycatia/tree/master/tests>`_. repository.

Example 1
---------

Access the CATIA COM object with a .CATPart open and get the center of gravity for the part body 'PartBody'.

.. literalinclude:: ../example_1.py

Example 2
---------

Get all the points in the geometrical set 'Points' and print the co-ordinate.

.. literalinclude:: ../example_2.py

Example 3
---------

Find all points in the CATPart and print it's co-ordinate.

.. literalinclude:: ../example_3.py

Example 4
---------

Loop through a CATProduct and find if sub component is a CATPart or CATProduct.

.. literalinclude:: ../example_4.py

Example 5
---------

Reads a csv file containing point data and adds to the active catia part.

.. literalinclude:: ../example_5.py

Example 6
---------

Open a catia file and close a catia file.

.. literalinclude:: ../example_6.py


Example 7
---------

Using the context manager.

.. literalinclude:: ../example_7.py

Example 8
---------

Find all .CATParts in folder and export to IGS.

.. literalinclude:: ../example_8.py

Example 9
---------

Get the position matrix of products (CATPart or CATProduct) in product.

.. literalinclude:: ../example_9.py

Example 10
----------

Loop through a CATProduct and analyse children if CATPart.

.. literalinclude:: ../example_10.py

Example 11
----------

Move first child in product.

.. literalinclude:: ../example_11.py

Example 12
----------

Move first child in product.

.. literalinclude:: ../example_12.py

Example 13
----------

Move first child in product.

.. literalinclude:: ../example_13.py

