# phforge

## What is it?

This is a script to create [Photon-HDF5](http://photon-hdf5.org/) files
starting from 2 files:

- a YAML file containing the metadata
- a HDF5 file containing only the photon_data arrays

The main purpose of this script is enabling programs (e.g. acquisition
software) in any programming languages to create valid Photon-HDF5 files
with minimal effort. Under the hood, phforge uses the [phconvert](http://photon-hdf5.github.io/phconvert/) library to
assure compliance with the Photon-HDF5 specs and simplify
creating the file.

## How to use?

A program using this script will first save a temporary HDF5 containing only
the photon-data arrays (timestamps, detectors, nanotimes, etc...) and
will create (or ask the user to crete) a YAML file with the metadata
(i.e. all the Photon-HDF5 fields except for the photon-data arrays).

Next, the program can invoke the script to create a Photon-HDF5 file.

```
phforge metadata_file hdf5_file out_file
```

The script creates an in-memory Photon-HDF5 representation (based on
nested dictionaries) by joining the metadata structure from the
YAML file and the numeric arrays from the temporary HDF5 file.

## How to install?

The script can be installed with PIP on any platform (Linux, OS X or Windows).
The installation adds the phforge to the system path so that it
can be directly called from a shell.

We recommend using `conda` (Anaconda or Miniconda) to install the dependencies.

## Dependencies

- pyyaml
- h5py
- phconvert

These packages depends on yaml (C library), pytables, hdf5 (C library).
