from qtnode import QTNode
import math
from utils import *

class QuadTree:
    __slots__ = ('root', 
                 'compressed_data', 
                 'height', 
                 'meta', 
                 'total_px', 
                 'img', 
                 'row_px')

    def __init__(self, meta):
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
        arr = []
        for i in range(self.row_px):
            row = []
            for j in range(self.row_px):
                row.append(0)
            arr.append(row)
        return arr

    def oned2img(self, buffer1d):
        for i in range(self.row_px):
            for j in range(self.row_px):
                self.img[i][j] = buffer1d[i * self.row_px + j] 

    def tree2img(self, node = None, x = 0, y = 0, size = None):
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
        img_arr = []
        for i in range(self.row_px):
            for j in range(self.row_px):
                img_arr.append(self.img[i][j])
        return img_arr
    
    def compressed_data_str(self):
        result = ""
        data_len = len(self.compressed_data)

        if data_len < 15:
            for x in self.compressed_data:
                result += f"{x} "

        else:
            for i in range(10):
                result += f"{self.compressed_data[i]} "
            result += "... "
            result += "(truncated for brevity)"
        
        return result
    
    def build_empty_tree(self, height):
        
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
        print(f"\nimg arr: {self.img}\n")
        for i in range(self.row_px):
            for j in range(self.row_px):
                print(self.img[i][j], end=' ')
            print()

    def flatten_quad_tree(self, node = None, flat_arr = [], isNonLeaf = False):
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
        return (
            node.get_upper_left() == None and
            node.get_upper_right() == None and
            node.get_lower_left() == None and
            node.get_lower_right() == None
        )

    def pre_order_travel(self, node = -1):
        if node == -1:
            node = self.root

        if node != None:
            print(node, end=', ')
            self.pre_order_travel(node.get_upper_left())
            self.pre_order_travel(node.get_upper_right())
            self.pre_order_travel(node.get_lower_left())
            self.pre_order_travel(node.get_lower_right())

    def read_file(self):
        filepath = self.meta['filepath']
            
        data = []

        try: 
            with open(filepath, 'r') as file:
                for line in file:
                    data.append(int(line.strip()))

        except FileNotFoundError:
            print("File not found.")
            error_state()

        except Exception as e:
            print(f"Error occurred: {e}")

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

        return data

    def display_image(self):
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

