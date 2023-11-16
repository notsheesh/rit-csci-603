"""
QuadTree

This class represents a quadtree used for image compression and decompression. 
It includes methods for building an empty tree, decompressing data, converting 
between tree and image representations, and analyzing the quadtree structure. 
The class also handles reading image data from a file, displaying the image, and 
performing various operations on the quadtree nodes.

Author: Shreesh Tripathi, st4083
"""
from qtnode import QTNode
import math
from utils import *
from qtexception import QTException

class QuadTree:
    __slots__ = ('root', 
                 'compressed_data', 
                 'height', 
                 'meta', 
                 'total_px', 
                 'img', 
                 'row_px')

    def __init__(self, meta):
        """
        Initialize the QuadTree object with metadata and initial values.

        :param meta: Metadata containing information about the image.
        :type meta: dict
        """
        self.root = None
        self.meta = meta
        # self.row_px = self.meta['size']
        # self.total_px = meta['size'] ** 2
        # self.height = meta['height']
        self.row_px = None
        self.total_px = None
        self.compressed_data = None
        self.height = None
        self.img = None
    
    def init_img_arr(self):
        """
        Initialize a 2D array for representing the image.

        :return: Initialized 2D array.
        :rtype: list
        """
        arr = []
        for i in range(self.row_px):
            row = []
            for j in range(self.row_px):
                row.append(0)
            arr.append(row)
        return arr

    def oned2img(self, buffer1d):
        """
        Convert a 1D buffer to a 2D image array.

        :param buffer1d: 1D buffer representing image data.
        :type buffer1d: list
        """
        for i in range(self.row_px):
            for j in range(self.row_px):
                self.img[i][j] = buffer1d[i * self.row_px + j] 

    def tree2img(self, node = None, x = 0, y = 0, size = None):
        """
        Convert the quadtree structure to a 2D image array.

        :param node: Current quadtree node.
        :type node: QTNode
        :param x: X-coordinate of the current node.
        :type x: int
        :param y: Y-coordinate of the current node.
        :type y: int
        :param size: Size of the current node.
        :type size: int
        """
        if size is None: 
            node = self.root
            size = self.row_px

        if self.is_leaf_node(node):
            for i in range(y, y + size):
                for j in range(x, x + size):
                    self.img[i][j] = node._value

        else:
            size = size // 2
            self.tree2img(node.get_upper_left(),  x, y, size)
            self.tree2img(node.get_upper_right(), x + size, y, size)
            self.tree2img(node.get_lower_left(),  x, y + size, size)
            self.tree2img(node.get_lower_right(), x + size, y + size, size)

    def img2arr(self):
        """
        Convert the 2D image array to a 1D buffer.

        :return: 1D buffer representing image data.
        :rtype: list
        """
        img_arr = []
        for i in range(self.row_px):
            for j in range(self.row_px):
                img_arr.append(self.img[i][j])
        return img_arr
    
    def compressed_data_str(self, trunc = False):
        """
        Generate a string representation of compressed data.

        :param trunc: Flag to truncate the output for brevity.
        :type trunc: bool

        :return: String representation of compressed data.
        :rtype: str
        """
        result = ""
        data_len = len(self.compressed_data)

        if trunc: 

            if data_len < 15:
                for x in self.compressed_data:
                    result += f"{x} "

            else:
                for i in range(10):
                    result += f"{self.compressed_data[i]} "
                result += "... "
                result += "(truncated for brevity)"
        
        else: 
                
            for x in self.compressed_data:
                result += f"{x} "
        
        return result
    
    def build_empty_tree(self, height):
        """
        Build an empty quadtree of a given height.

        :param height: Height of the quadtree.
        :type height: int

        :return: Root node of the empty quadtree.
        :rtype: QTNode
        """
        if height == 0:
            # return QTNode(f"L{int(height)}")
            return QTNode(0)
        
        else:
            return QTNode(
                -1,
                ul=self.build_empty_tree(height-1),
                ur=self.build_empty_tree(height-1),
                ll=self.build_empty_tree(height-1),
                lr=self.build_empty_tree(height-1)
            )
    
    def decompress(self, node, data):
        """
        Decompress the quadtree structure from compressed data.

        :param node: Current quadtree node.
        :type node: QTNode
        :param data: Compressed data buffer.
        :type data: list
        """
        if data: 
            value = data.pop(0)

            # split the node into 4 
            if value == -1:
                self.decompress(node.get_upper_left(),  data)
                self.decompress(node.get_upper_right(), data)
                self.decompress(node.get_lower_left(),  data)
                self.decompress(node.get_lower_right(), data)

            else:
                if self.is_leaf_node(node):
                    node._value = value
                else: 

                    self.set_leaf_nodes(node, value)
    
    def print_img(self):
        """
        Print the 2D image array to the console.
        """
        print(f"\nimg arr: {self.img}\n")
        for i in range(self.row_px):
            for j in range(self.row_px):
                print(self.img[i][j], end=' ')
            print()

    def flatten_quad_tree(self, node = None, flat_arr = [], isNonLeaf = False):
        """
        Flatten the quadtree structure into a 1D array.

        :param node: Current quadtree node.
        :type node: QTNode
        :param flat_arr: Flattened array to store the values.
        :type flat_arr: list
        :param isNonLeaf: Flag indicating if non-leaf nodes should be included.
        :type isNonLeaf: bool

        :return: Flattened 1D array.
        :rtype: list
        """
        if node is None:
            node = self.root

        if self.is_leaf_node(node):
            flat_arr.append(node._value)

        else: 
            if isNonLeaf:
                flat_arr.append(node._value)
            self.flatten_quad_tree(node.get_upper_left(),  flat_arr, isNonLeaf)
            self.flatten_quad_tree(node.get_upper_right(), flat_arr, isNonLeaf)
            self.flatten_quad_tree(node.get_lower_left(),  flat_arr, isNonLeaf)
            self.flatten_quad_tree(node.get_lower_right(), flat_arr, isNonLeaf)
        
        return flat_arr

    def set_leaf_nodes(self, node, value):
        """
        Set the values of leaf nodes to a given value.

        :param node: Current quadtree node.
        :type node: QTNode
        :param value: Value to be set for leaf nodes.
        :type value: int
        """
        if self.is_leaf_node(node):
            node._value = value
            return
        else: 
            self.set_leaf_nodes(node.get_upper_left(),  value)
            self.set_leaf_nodes(node.get_upper_right(), value)
            self.set_leaf_nodes(node.get_lower_left(),  value)
            self.set_leaf_nodes(node.get_lower_right(), value)
        return

    def analyze(self, node, report = {}):
        """
        Analyze the quadtree structure and generate a report.

        :param node: Current quadtree node.
        :type node: QTNode
        :param report: Dictionary to store the analysis report.
        :type report: dict

        :return: Analysis report and a validity flag.
        :rtype: tuple
        """
        if self.is_leaf_node(node):
            report[node._value] = report.get(node._value, 0) + 1
        else: 
            self.analyze(node.get_upper_left(),  report)
            self.analyze(node.get_upper_right(), report)
            self.analyze(node.get_lower_left(),  report)
            self.analyze(node.get_lower_right(), report)
        
        valid = self.total_px == sum([report[key] for key in report])
        assert valid == True

        return report, valid  

    def is_leaf_node(self, node):
        """
        Check if a node is a leaf node (has no children).

        :param node: Quadtree node to be checked.
        :type node: QTNode

        :return: True if the node is a leaf, False otherwise.
        :rtype: bool
        """
        return (
            node.get_upper_left() == None and
            node.get_upper_right() == None and
            node.get_lower_left() == None and
            node.get_lower_right() == None
        )

    def pre_order_travel(self, node = -1):
        """
        Perform a pre-order traversal of the quadtree.

        :param node: Current quadtree node.
        :type node: QTNode or int
        """
        if node == -1:
            node = self.root

        if node != None:
            print(node, end=', ')
            self.pre_order_travel(node.get_upper_left())
            self.pre_order_travel(node.get_upper_right())
            self.pre_order_travel(node.get_lower_left())
            self.pre_order_travel(node.get_lower_right())

    def read_file(self):
        """
        Read image data from a file and perform error handling.

        :return: List containing the read image data.
        :rtype: list
        """
        filepath = self.meta['filepath']
            
        data = []

        try: 
            with open(filepath, 'r') as file:
                flag = False 
                for line in file:
                    value = line.strip()
                    
                    # error handling
                    if flag and not is_integer(value): 
                        raise QTException(f"Pixel value [{value}] is not an integer")
                    
                    if flag and not is_valid_pixel(int(value)): 
                        raise QTException(f"Pixel value [{value}] is not in the range [0, 255]")

                    flag = True

                    data.append(int(value))

        except FileNotFoundError:
            print("File not found")
            error_state()

        except QTException as qte:
            print(f"QTException: {qte}")
            sys.exit(1)

        except Exception as e:
            print(f"Error occured: {e}")
            sys.exit(1)

        # sanity check 
        if self.meta['mode'] == "compressed":
            self.total_px = data.pop(0)

        elif self.meta['mode'] == "uncompressed":
            self.total_px = len(data)
        
        else: 
            sys.exit(0)

        # set remaining class fields
        self.row_px = int(self.total_px ** 0.5)
        self.height = math.log2(self.row_px)

        self.meta['size'] = self.row_px
        self.meta['height'] = self.height
        self.img = self.init_img_arr()

        # error handling
        try:
            if not is_power_of_two(self.total_px):
                raise QTException("Image size isn't a power of 2")
    
            if not is_square(self.total_px):
                raise QTException("Image size isn't a square")
            
        except QTException as qte:
            print(f"QTException: {qte}")
            sys.exit(1)

        return data

    def display_image(self):
        """
        Display the image using a Tkinter window.
        """
        window = tk.Tk()
        window.title(self.meta['title'])
        photo = tk.PhotoImage(width=self.row_px, height=self.row_px)
        
        for i in range(self.row_px):
            for j in range(self.row_px):
                color_val = self.img[i][j]
                color = "#{:02x}{:02x}{:02x}".format(
                    color_val, color_val, color_val)
                photo.put(color, (j, i))  
                
        canvas = tk.Canvas(window, width=self.row_px, height=self.row_px)
        canvas.pack()
        canvas.create_image(0, 0, anchor=tk.NW, image=photo)
        window.mainloop()

