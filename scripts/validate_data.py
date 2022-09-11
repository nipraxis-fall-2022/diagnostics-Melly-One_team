""" Python script to validate data

Run as:

    python3 scripts/validata_data.py data
"""

from pathlib import Path
import sys
import hashlib

def file_hash(filename):
    """ Get byte contents of file `filename`, return SHA1 hash

    Parameters
    ----------
    filename : str
        Name of file to read

    Returns
    -------
    hash : str
        SHA1 hexadecimal hash string for contents of `filename`.
    """

    # Convert a string filename to a Path object.
    fpath = Path(filename)
    # Your code here.
    contents = fpath.read_bytes()
    hash_value = hashlib.sha1(contents).hexdigest()
    return hash_value
    


def validate_data(data_directory):
    """ Read ``data_hashes.txt`` file in `data_directory`, check hashes

    Parameters
    ----------
    data_directory : str
        Directory containing data and ``data_hashes.txt`` file.

    Returns
    -------
    None

    Raises
    ------
    ValueError:
        If hash value for any file is different from hash value recorded in
        ``data_hashes.txt`` file.
    """
    # Read lines from ``data_hashes.txt`` file.
    # Split into SHA1 hash and filename
    # Calculate actual hash for given filename.
    # If hash for filename is not the same as the one in the file, raise
    # ValueError
    hash_pth = Path(data_directory+'/data_hashes.txt')
    # Read in text for hash filename
    hashes_text = hash_pth.read_text()
    # Split into lines.
    hash_text = hashes_text.split("\n")[:-1]
    for lines in hash_text:
        line = lines.split(' ')
        expected_hash = line[0]
        fname = data_directory + '/' + line[1]
        calc_hash = file_hash(fname)
        if not calc_hash == expected_hash:
            raise ValueError


def main():
    # This function (main) called when this file run as a script.
    #
    # Get the data directory from the command line arguments
    if len(sys.argv) < 2:
        raise RuntimeError("Please give data directory on "
                           "command line")
    data_directory = sys.argv[1]
    # Call function to validate data in data directory
    validate_data(data_directory)


if __name__ == '__main__':
    # Python is running this file as a script, not importing it.
    main()
