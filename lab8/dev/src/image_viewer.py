import os
from utils import *
from quadtree import QuadTree

def decompress_image(meta):
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

    dump_data(qt.img2arr(), qt.meta['filename'])

    return qt.img2arr()

def show_image(meta):
    # init quad tree
    qt = QuadTree(meta)

    # read image data 
    buffer1d = qt.read_file()

    # unload array to image
    qt.oned2img(buffer1d)

    # display image
    qt.display_image()

def main():
    meta = parse_args()
    decompress_image(meta) if meta['mode'] == "compressed" else show_image(meta)
    return

if __name__ == "__main__":
    main()



