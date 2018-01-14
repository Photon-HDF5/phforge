# phforge

## What is it?

**phforge** is a script to create [Photon-HDF5](http://photon-hdf5.org/) files
starting from two files:

- a [YAML](https://en.wikipedia.org/wiki/YAML) file containing the metadata
- a (temporary) HDF5 file containing only the photon_data arrays

The main purpose of this script is enabling programs (e.g. acquisition
software) in any programming languages to create valid Photon-HDF5 files
with minimal effort. Under the hood, phforge uses the [phconvert](http://photon-hdf5.github.io/phconvert/) library to
assure compliance with the Photon-HDF5 specs and to simplify
creating the file.

## How to use?

A program wanting to create a Photon-HDF5 file, needs to save a temporary HDF5
containing only the
[photon-data arrays](http://photon-hdf5.readthedocs.org/en/latest/phdata.html#photon-data-group)
(timestamps, detectors, nanotimes, etc...) and to generate (or ask the user
to write) a YAML file with the metadata (i.e. all the Photon-HDF5 fields
except for the photon-data arrays). Examples of both YAML and HDF5 files
can be found in the [example_data](https://github.com/tritemio/phforge/tree/master/example_data)
folder.

Next, the program can invoke `phforge` script to create a Photon-HDF5 file:

```
phforge metadata_file hdf5_file out_file
```

The script creates an in-memory Photon-HDF5 representation (based on
nested dictionaries) by joining the metadata structure from the
YAML file and the numeric arrays from the temporary HDF5 file.
Then, it uses phconvert's [`save_photon_hdf5()`](http://phconvert.readthedocs.org/en/latest/hdf5.html#phconvert.hdf5.save_photon_hdf5)
function to save a new Photon-HDF5 file.

## How to install?

We provided `conda` packages for Windows x64 and OS X for both python 3.4 and legacy python 2.7.
To install the conda package type:

```
conda install phforge -c tritemio
```

A conda installation is required (use either [Anaconda](https://www.continuum.io/downloads)
or [Miniconda3](http://conda.pydata.org/miniconda.html)).
The installation adds the phforge to the system path so that it
can be directly called from any shell.

Alternatively the script can be installed with PIP on any platform.

## Dependencies

- python 3.4 (or later, recommended) or 2.7 (legacy)
- pyyaml (tested on 3.11)
- h5py (tested on 2.5.0)
- phconvert 0.8 (or later)

These packages depends on yaml (C library), pytables 3.2, hdf5 (C library).

# Feedback

For questions or comments please:

- [Open an GitHub issue](https://github.com/Photon-HDF5/phforge/issues) or
- Ask a question on the [Photon-HDF5 Google Group](https://groups.google.com/forum/#!forum/photon-hdf5).

## License

*phforge* is released under the open source MIT license.

## Acknowledgements
This work was supported by NIH Grant R01-GM95904.
