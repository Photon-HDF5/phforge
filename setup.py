from setuptools import setup

project_name = 'phforge'
__version__ = 0.1.1

long_description = """
phforge
=======

phforge is a script to ease creating `Photon-HDF5 <http://photon-hdf5.org/>`_
files.

The main purpose of this script is enabling programs (e.g. data acquisition
software) in any programming languages to create valid Photon-HDF5 files
with minimal effort. Under the hood, phforge uses the phconvert library
which assures compliance with the Photon-HDF5 specifications and simplifies
saving the file.
"""

setup(
    name = project_name,
    version=__version__,
    author = 'Antonino Ingargiola',
    author_email = 'tritemio@gmail.com',
    url = 'https://github.com/Photon-HDF5/phforge',
    download_url = 'https://github.com/Photon-HDF5/phforge',
    install_requires = ['pyyaml', 'phconvert'],  # removed h5py for conda issue
    license = 'MIT',
    description = ("Script for easy creation of Photon-HDF5 files."),
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
    package_data = {'phforge': ['example_data/*']},
    entry_points={'console_scripts': ['phforge = phforge:main']},
    keywords = ('single-molecule FRET smFRET biophysics file-format HDF5 '
                'Photon-HDF5')
)
