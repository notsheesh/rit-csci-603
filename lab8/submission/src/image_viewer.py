"""
CSCI-603 Lab 08: Image Viewer

This script provides functions for compressing and decompressing images using a 
quadtree-based encoding. It includes a QuadTree class for managing the compression 
and decompression processes, as well as utility functions for handling image data 
and displaying images.

Author: Shreesh Tripathi, st4083
"""
import os
from utils import *
from quadtree import QuadTree

def decompress_image(meta):
    """
    Decompresses a quadtree-encoded image based on the provided metadata.

    :param meta: Metadata containing information about the compressed image.
    :type meta: dict

    :return: A 2D array representing the decompressed image.
    :rtype: list
    """
    # init quad tree
    qt = QuadTree(meta)

    # read compressed data
    qt.compressed_data = qt.read_file()

    # setup tree
    qt.root = qt.build_empty_tree(qt.height)

    print(f"Uncompressing: {meta['filename']}")
    print(f"Quadtree: {qt.compressed_data_str(trunc=True)}")

    option = input("Do you want to see the whole array? (y/n): ")
    if option == "y":
        print(f"Quadtree: {qt.compressed_data_str(trunc=False)}")
    else:
        pass

    # decompress
    qt.decompress(qt.root, qt.compressed_data)

    # unload tree to image
    qt.tree2img()

    # display image
    qt.display_image()

    # for debugging
    # dump_data(qt.img2arr(), qt.meta['filename'])

    return qt.img2arr()

def show_image(meta):
    """
    Displays an image based on the provided metadata.

    :param meta: Metadata containing information about the image.
    :type meta: dict
    """
    # init quad tree
    qt = QuadTree(meta)

    # read image data 
    buffer1d = qt.read_file()

    # unload array to image
    qt.oned2img(buffer1d)

    # display image
    qt.display_image()

def main():
    """
    Main function for decompressing or showing an image based on user input.

    :return: None
    """
    meta = parse_args()
    decompress_image(meta) if meta['mode'] == "compressed" else show_image(meta)
    return

if __name__ == "__main__":
    main()



