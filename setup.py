from setuptools import setup

project_name = 'phforge'
__version__ = 0.1

long_description = """
phforge
=======

This is a script to create `Photon-HDF5 <http://photon-hdf5.org/>`_ files
from a YAML file containing metadata and an HDF5 file containing
the photon_data arrays.

"""

setup(
    name = project_name,
    version=__version__,
    author = 'Antonino Ingargiola',
    author_email = 'tritemio@gmail.com',
    # url          = 'http://photon-hdf5.github.io/phconvert/',
    # download_url = 'http://photon-hdf5.github.io/phconvert/',
    install_requires = ['pyyaml', 'phconvert'],
    license = 'MIT',
    description = ("Create Photon-HDF5 files."),
    long_description = long_description,
    platforms = ('Windows', 'Linux', 'Mac OS X'),
    classifiers=['Intended Audience :: Science/Research',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3.4',
                 'Topic :: Scientific/Engineering',
                 ],
    py_modules = ['phforge'],
    entry_points={'console_scripts': ['phforge = phforge:main']},
    keywords = ('single-molecule FRET smFRET biophysics file-format HDF5 '
                'Photon-HDF5')
)
