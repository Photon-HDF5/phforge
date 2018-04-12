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

A program wanting to create a Photon-HDF5 file, needs to first create a
temporary HDF5 file (with photon timestamps) and a text YAML file with the
metadata. With these two input files, `phforge` can save a Photon-HDF5 file.

The temporary HDF5 file needs to contain the
[photon-data arrays](http://photon-hdf5.readthedocs.org/en/latest/phdata.html#photon-data-group)
(timestamps, detectors, nanotimes). The metadata file contains all the
Photon-HDF5 fields except for the photon-data arrays.
Examples of both YAML and HDF5 files can be found in the [example_data](https://github.com/tritemio/phforge/tree/master/example_data)
folder.

Finally, to create a Photon-HDF5 file run `phforge` as follows:

```
phforge metadata_file hdf5_file out_file
```

The script creates an in-memory Photon-HDF5 representation (based on
nested dictionaries) joining the metadata structure from the
YAML file and the numeric arrays from the temporary HDF5 file.
Then, it uses phconvert's [`save_photon_hdf5()`](http://phconvert.readthedocs.org/en/latest/hdf5.html#phconvert.hdf5.save_photon_hdf5)
function to save a new Photon-HDF5 file.

Call `phforge -h` to print usage information.

## How to install phforge?

It is recommended to first instal a conda distribution (either [Anaconda](https://www.continuum.io/downloads)
or [Miniconda3](http://conda.pydata.org/miniconda.html)).
The installation adds the `phforge` script to the system path so that it
can be directly called from any shell.

### Installation from source (provisional)

You can install `phforge` from source as described here.

First install `phconvert` and `h5py` with:

```
conda install phconvert h5py -c conda-forge
```

Then download and extract `phforge` archive from GitHub, open the terminal,
`cd` into `phforge` source folder and type:

```
pip install .
```

### Installation from conda packages (not yet available)

Soon, it will be possible to install `phforge` and all the dependencies
(including `phconvert`) with a single command:

```
conda install phforge -c conda-forge  # not yet available
```


## Dependencies

- python 3.4 (or later, recommended) or 2.7 (legacy)
- pyyaml (tested on 3.11)
- h5py (tested on 2.5.0)
- phconvert 0.8 (or later)

These packages depends on yaml (C library), pytables, hdf5 (C library).
The installation through conda will automatically install the dependencies.

# Feedback

For questions or comments please:

- [Open an GitHub issue](https://github.com/Photon-HDF5/phforge/issues) or
- Ask a question on the [Photon-HDF5 Google Group](https://groups.google.com/forum/#!forum/photon-hdf5).

## License

*phforge* is released under the open source MIT license.

## Acknowledgements
This work was supported by NIH Grant R01-GM95904.
