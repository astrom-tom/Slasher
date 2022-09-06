.. VcatPy documentation master file, created by
   sphinx-quickstart on Fri Mar  9 22:59:43 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.
.. _usage:

|python| |Python39| |Licence|
|matplotlib| |PyQt5| |numpy| 

.. |Licence| image:: https://img.shields.io/badge/License-GPLv3-blue.svg
      :target: http://perso.crans.org/besson/LICENSE.html

.. |Opensource| image:: https://badges.frapsoft.com/os/v1/open-source.svg?v=103
      :target: https://github.com/ellerbrock/open-source-badges/

.. |python| image:: https://img.shields.io/badge/Made%20with-Python-1f425f.svg
    :target: https://www.python.org/downloads/release/python-360/

.. |PyQt5| image:: https://img.shields.io/badge/poweredby-PyQt5-orange.svg
   :target: https://pypi.python.org/pypi/PyQt5

.. |matplotlib| image:: https://img.shields.io/badge/poweredby-matplotlib-orange.svg
   :target: https://matplotlib.org/

.. |Python39| image:: https://img.shields.io/badge/python-3.9%20-blue.svg
.. _Python39: https://www.python.org/downloads/release/python-360/

.. |numpy| image:: https://img.shields.io/badge/poweredby-numpy-orange.svg
   :target: http://www.numpy.org/


Using slasher
=============



Installation
~~~~~~~~~~~~
For the moment, the only way to use slasher is to download the source code from the Github repository (https://github.com/astrom-tom/slasher - using the 'clone or download' button and download as zip). To make it work you have to use python 3.9 with the following library and versions:

* PyQt5 v5.15.4: The is for the graphical interface
* Matplotlib v3.4.3: This is for the plotting area. 
* catscii v19.8.1: catalog handling
* astropy v5.0.1: For fits image opening

Cutter is available in the pypi repository. To install it:

.. code-block:: shell
     :linenos:

     pip install slasher --user


The help
~~~~~~~~
You start slasher from a terminal. The program comes with a help that you can display in your terminal using the help command.
Use it like this::


           [user@machine]$ slasher --help

This will give you the following output::

        This command will display the help of the program::


        usage: slasher [-h] [-f FILE] [-d DIRE] [-w WIDTH] [--version]

        slasher, R. Thomas, 2022, This program comes with ABSOLUTELY NO WARRANTY; and is distributed under the
        GPLv3.0 Licence terms.See the version of this Licence distributed along this code for details. website:
        https://github.com/astrom-tom/Photon

        optional arguments:
          -h, --help            show this help message and exit
          -f FILE, --file FILE  Your catalog of data to visualize, this is mandatory, this is mandatory if you do
                                not use -p option
          -d DIRE, --dire DIRE  Directory where the original spectra are located
          -w WIDTH, --width WIDTH
                                Width of the GUI, default = 780
          --version             display version of slasher



In details it means:

* Cutter must run with a catalog. If you do not give slasher one, it will complain (you can see below for the format of the file you can provide slasher with).
* Few arguments can be used:
	
	* -f: this is a catalog of spectrum you want to display
	* -w: width of the window: The GUI is not resizable. Which means that the size of the plot is pre-fedined. By default the width of the window is sized at 780. Using this option, (e.g. -w 1080) will resize the GUI with a width of 1080.
	* -d: Path to the directory where the original spectra are located
	* --version: Display in terminal the current version of the software

Catalog format
~~~~~~~~~~~~~~

For the current version, slasher accepts only *ascii* catalogs of columns and *fits* files. Some precisions:

* The catalog must contain at least 3 columns and 2 lines.
* The first column must be the name of the spectrum in fits format (more on that below)
* The second column must be the name of the noise spectrum in fits format.
* The third column must be the redshift column (can be filled with -999 if you don't have redshifts).
* Each line must contain the same number of column.


The Graphical User Interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
When starting slasher, the graphical interface shows up in the screen (Screenshot below).

It is composed of five area:

1. The plotting Area, where the plot will be displayed.
2. The matplotlib toolbar. Allows you to zoom in/out, select specific part of the plot, etc...
3. The 'Add element in plot' button. It is the button you will use to add elements in the plot such as Line plot, Scatter plot, histograms, strips, text, etc...
4. Graphical Elements Panel. Then you click in the previous button, the widgets for the graphical elements you want to use will be displayed in that area. The widgets depend on the type of element  you want to add into the plot. (:doc:`graphics`)
5. Customization Panel. This Panel remains the same all the time and help you to customize graphical properties of the plot itself such as: background color, axis tickness or color, ticks label size, fontsizes, etc. (:doc:`custom`)

When clicking on 'Add element in plot' you have these different choices:

 * line
 * line / new file
 * scatter
 * scatter /new file
 * histogram
 * histogram /new file
 * Error
 * Error / new file
 * Straight line
 * Span
 * Text
 * Image
 * Image / new file

All the plotting elements are described here: :doc:`graphics`. As you can see some plotting elements are repeated (e.g. 'line' and 'line / new file'). As you start Photon with a particular file it can be useful to be able to load data from another file. If this is the case you can use 'XX / new file' and Photon will open dialog window to choose another file to use in photon. When loading a pre-existing plot configuration, if you want to add more data to your plot, you will only have the 'New file' choices.


.. figure:: GUI.png
    :width: 750px
    :align: center
    :alt: GUI

    GUI of slasher
