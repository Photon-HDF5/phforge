# phforge

## What is it?

This is a script to create [Photon-HDF5](http://photon-hdf5.org/) files
starting from two files:

- a YAML file containing the metadata
- a (temporary) HDF5 file containing only the photon_data arrays

The main purpose of this script is enabling programs (e.g. acquisition
software) in any programming languages to create valid Photon-HDF5 files
with minimal effort. Under the hood, phforge uses the [phconvert](http://photon-hdf5.github.io/phconvert/) library to
assure compliance with the Photon-HDF5 specs and to simplify
creating the file.

## How to use?

A program wanting to crate a Photon-HDF5 file, needs to save a temporary HDF5
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
Finally, it uses phconvert's [`save_photon_hdf5()`](http://phconvert.readthedocs.org/en/latest/hdf5.html#phconvert.hdf5.save_photon_hdf5)
to saves a new Photon-HDF5 file.

## How to install?

The script can be installed with PIP on any platform (Linux, OS X or Windows).
The installation adds the phforge to the system path so that it
can be directly called from a shell.

We recommend using `conda` (Anaconda or Miniconda) to install the dependencies.

## Dependencies

- python 2.7 (legacy), 3.4 (or later)
- pyyaml
- h5py
- phconvert 0.6.5 (or later)

These packages depends on yaml (C library), pytables 3.2, hdf5 1.8.15 (C library).
