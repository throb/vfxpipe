"""
This script searches a given directory for image sequence files and returns a
string containing the list of sequences found. 

It searches for files with the following extensions: 
exr, jpeg, jpg, png, tif, tiff, mov

The file string may be of the form:
{filename}.{start}-{end}.{extension}
or
{filename}.{index}.{extension}

Usage:
python3 image_sequence_finder.py <dirname>

"""

import os
import re
import sys
from pprint import pprint

FILE_EXTS = [
    'exr',
    'jpeg',
    'jpg',
    'png',
    'tif',
    'tiff',
    'mov'
]

SEQUENCE_PATTERN = r'(.*)\.([0-9]+).(.{3,4})$'

def sequences_strigifier(sequences):
    """
    Generates a string representation of the image sequences found.
    Args:
        sequences (dict): Dictionary of sequences found.
    Returns:
        string: A string with the sequences found.
    """
    output_string = ''
    for key, seq_info in sequences.items():
        if not seq_info:
            output_string += '{}\n'.format(key)
            continue

        if seq_info['start_index'] == seq_info['end_index']:
            output_string += '{}.{}.{}\n'.format(key,
                                                 seq_info['start_index_str'],
                                                 seq_info['ext'])
            continue

        output_string += '{}.{}.{}, [{}-{}]\n'.format(key,
                                                      seq_info['start_index_str'],
                                                      seq_info['ext'],
                                                      seq_info['first_frame'],
                                                      seq_info['last_frame'])

    return output_string.strip()

SEQUENCE_PATTERN = r'(.*)\.([0-9]+).(.{3,4})$'

def find_image_sequences(directory):
    """
    Searches through a given directory for image sequences files
    with the extensions specified in the FILE_EXTS list.
    Args:
        directory (string): The directory to search.
    Returns:
        dict: A dictionary of image sequences found in the directory.
    """

    sequences = {}
    paddingSize = None

    for candidate_path in sorted(os.listdir(directory)):
        full_candidate_path = os.path.join(directory, candidate_path)
        matches = re.match(SEQUENCE_PATTERN, candidate_path)

        if not matches:
            if os.path.isfile(full_candidate_path) and any(substring in candidate_path.lower() for substring in FILE_EXTS):
                filename, ext = os.path.splitext(candidate_path)
                sequences[filename] = {
                    'filename': filename,
                    'dirname': directory,
                    'full_path': full_candidate_path,
                    'ext': ext[1:],
                    'padding': None,
                    'first_frame': None,
                    'last_frame': None
                }
            continue

        filename, sequence_index, ext = matches.groups()
        if ext not in FILE_EXTS:
            continue

        sequence_index = int(sequence_index)
        if paddingSize is None:
            paddingSize = len(sequence_index)
        else:
            paddingSize = min(paddingSize, len(sequence_index))

        if filename not in sequences:
            sequences[filename] = {
                'filename': filename,
                'dirname': directory,
                'ext': ext,
                'padding': paddingSize,
                'first_frame': sequence_index,
                'last_frame': sequence_index,
            }
        else:
            sequences[filename]['last_frame'] = sequence_index

    return sequences

def find_image_sequences_in_subdirectories(directory):
    """
    Recursively searches through a given directory and its subdirectories
    for image sequence files with the extensions specified in the FILE_EXTS list.
    Args:
        directory (string): The directory to search.
    Returns:
        list: A list of dictionaries of image sequences found in the directory
              and its subdirectories.
    """

    imgSeq = []
    allSequences= []
    currentSequence = {}
    for root, dirs, files in os.walk(directory):

        # look in current folder
        imgSeq.append(find_image_sequences(directory))

        # look in subdirs
        for dirname in dirs:
            tmp = find_image_sequences(os.path.join(root, dirname))
            if tmp != {}:
                imgSeq.append(tmp)

    for curSequences in imgSeq:
        for file in curSequences.items():
            curItem = file[1]
            if curItem['first_frame'] == None:

                currentSequence = {
                    'filename' : curItem['filename'],
                    'dirname' : curItem['dirname'],
                    'frame_range' : None,
                    'padding' : None,
                    'ext' : curItem['ext'],
                    'full_path' : os.path.join(curItem['dirname'], curItem['filename'] + '.' + curItem['ext'])
                }

            else :

                currentSequence = {
                    'filename' : curItem['filename'],
                    'dirname' : curItem['dirname'],
                    'frame_range' : "{start}-{end}".format (start = curItem['first_frame'], end=curItem['last_frame']),
                    'first_frame' : curItem['first_frame'],
                    'last_frame' : curItem['last_frame'],
                    'padding' : '#'*curItem['padding'],
                    'ext' : curItem['ext'],
                    'full_path' : os.path.join(curItem['dirname'], curItem['filename'] + '.' + '#'*curItem['padding'] + '.' + curItem['ext'])
                }
            allSequences.append(currentSequence)
    return (allSequences)
        

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: {} <dirname>'.format(sys.argv[0]))
        exit(1)
    else :
        pprint(find_image_sequences_in_subdirectories(sys.argv[1]))
        pass