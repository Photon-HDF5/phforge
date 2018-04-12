#!/usr/bin/env python
"""
Create Photon-HDF5 from YAML and and a temporary HDF5 file.
"""

import sys
import os
import argparse
import yaml
import h5py
import phconvert as phc

__version__ = '0.2.1'


def error(msg):
    print('ERROR: %s \n' % msg)
    print('Type `phforge -h` for help.\n')
    sys.exit(1)


def run(metadata_fname, hdf5_fname, out_fname):
    # Load data
    data = yaml.load(open(metadata_fname))
    with h5py.File(hdf5_fname) as h5file:
        for name in h5file:
            data['photon_data'][name] = h5file[name][:]
    # Save Photon-HDF5 file
    phc.hdf5.save_photon_hdf5(data, h5_fname=out_fname)


def run_tests():
    import pkg_resources as pkg
    import os
    import subprocess

    basedir = pkg.resource_filename('phforge', 'example_data')
    hdf5_fname = pkg.resource_filename('phforge',
                                       'example_data/photon_data_arrays.h5')
    assert os.path.isfile(hdf5_fname)
    for meta in pkg.resource_listdir('phforge', 'example_data'):
        if meta.endswith('yaml'):
            meta_fname = '/'.join((basedir, meta))
            os.path.exists(meta_fname)
            out_fname = 'photon_hdf5_%s.h5' % meta[:-5].split('_')[1]
            cmd = ('phforge "{meta}" "{hdf5}" "{out}"'
                   .format(meta=meta_fname, hdf5=hdf5_fname, out=out_fname))
            print('\n- Executing: %s' % cmd)
            assert os.path.isfile(meta_fname)
            subprocess.check_call(cmd, shell=True)


def main():
    print("\nphforge {version} (phconvert {phc_version})\n"
          .format(version=__version__, phc_version=phc.__version__))
    descr = """\
        Create a Photon-HDF5 file (www.photon-hdf5.org) from metadata in
        a YAML file and photon_data arrays in a (temporary) HDF5 file
        """
    parser = argparse.ArgumentParser(description=descr, epilog='\n')
    help = 'file name for the YAML file containing metadata.'
    parser.add_argument('metadata_file', help=help)
    help = 'file name of the HDF5 file containing the photon_data arrays.'
    parser.add_argument('hdf5_file', help=help)
    help = 'file name for the Photon-HDF5 file to be created.'
    parser.add_argument('output_file', help=help)
    args = parser.parse_args()

    if not os.path.isfile(args.metadata_file):
        error('Metadata file "%s" not found.' % args.metadata_file)
    if not os.path.isfile(args.hdf5_file):
        error('HDF5 file "%s" not found.' % args.hdf5_file)
    if os.path.isfile(args.output_file):
        error('A file "%s" already exists.' % args.output_file)
    run(args.metadata_file, args.hdf5_file, args.output_file)


if __name__ == '__main__':
    main()
