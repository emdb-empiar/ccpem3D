ccpem3D
============

Showcase of 3D viewing webcomponent for VTP files

How to use this demo
--------------------------------------------

1. Clone source

.. code:: bash

	git clone https://github.com/emdb-empiar/ccpem3D.git

2. Enter ccpe3D directory then start webserver

.. code:: bash

	cd ccpem3D
	python manage.py runserver
	
Navigate to http://localhost:8000 (or whatever host:port combination specified)

3. Generate a VTP file using ``meshmaker``

.. code:: bash

	meshmaker -c 12.3 file.map --vtp -o file

4. From your browser find a *VTP* file then click *View*. 