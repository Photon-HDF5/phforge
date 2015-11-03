#!/usr/bin/env python
"""
Create Photon-HDF5 from YAML and and a temporary HDF5 file.
"""

import sys
import os
from textwrap import dedent
import yaml
import h5py
import phconvert as phc

__version__ = 0.1


def help():
    """Print help"""
    msg = """\
    Create a Photon-HDF5 file (www.photon-hdf5.org) from metadata in
    a YAML file and photon_data arrays in a (temporary) HDF5 file.

    Usage:

        phforge metadata_file hdf5_file output_file

        metadata_file:
            file name for the YAML file containing metadata

        hdf5_file:
            file name of the HDF5 file containing the photon_data arrays.

        output_file:
            file name for the Photon-HDF5 file to be created.
    """
    print(dedent(msg))

def error(msg):
    print('ERROR: %s \n' % msg)
    print('Type phforge with no arguments for help.\n')
    sys.exit(1)

def main():
    print("phforge {version} (phconvert {phc_version}\n"
          .format(version=__version__, phc_version=phc.__version__))

    ## Check arguments
    if len(sys.argv) == 1 or sys.argv[1] == '-h' or sys.argv[1] == '--help':
        help()
        sys.exit(0)
    num_args = 3
    if len(sys.argv) != num_args + 1:
        error('You need to pass %d arguments.' % num_args)

    ## Check that input files exists
    metadata_fname, hdf5_fname, out_fname = sys.argv[1:]
    if not os.path.isfile(metadata_fname):
        error('Metadata file "%s" not found.' % metadata_fname)
    if not os.path.isfile(hdf5_fname):
        error('HDF5 file "%s" not found.' % hdf5_fname)
    if os.path.isfile(out_fname):
        error('A file "%s" already exists.' % out_fname)

    ## Load data
    data = yaml.load(open(metadata_fname))
    with h5py.File(hdf5_fname) as h5file:
        for name in h5file:
            data['photon_data'][name] = h5file[name][:]

    ## Save Photon-HDF5 file
    phc.hdf5.save_photon_hdf5(data, h5_fname=out_fname)

if __name__ == '__main__':
    main()
