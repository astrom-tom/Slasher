from setuptools import setup  # Always prefer setuptools over distutils

__author__ = "Romain Thomas"
__credits__ = "Romain Thomas"
__license__ = "GNU GPL v3"
__version__ = "22.9.1"
__maintainer__ = "Romain Thomas"
__email__ = "the.spartan.proj@gmail.com"
__status__ = "Development"

setup(
   name = 'slasher',
   version = __version__,
   author = __author__,
   author_email = __email__,
   packages = ['slasher'],
   entry_points = {'gui_scripts': ['Slasher = slasher.__main__:main',],},
   license = __license__,
   description = 'Python tool for easy spectrum cutting',
   python_requires = '>=3.6',
   install_requires = [
      "PyQt5 >= v5.15.4",
      "catscii>=19.8",
      "matplotlib >= 3.4.3",
      "astropy >= 5.0.1",
   ],
   include_package_data=True,
)
