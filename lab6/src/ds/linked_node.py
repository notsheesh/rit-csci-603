from typing import Any
class LinkedNode: 
    __slots__ = "value", "link"
    value: Any
    link: 'LinkedNode'

    def __init__(self, value, link = None):
        self.value = value
        self.link = link
    
    def set_link(self, link):
        self.link = link
    
    def get_link(self):
        return self.link

    def set_value(self, value):
        self.value = value
    
    def get_value(self):
        return self.value
    
    def __str__(self):
        # return "[{}, {}]".format(
        #     self.get_value(), self.get_link()
        # )
        return "{}".format(self.get_value())
    
def test():
    pass

def main():
    pass
if __name__ == '__main__':
    main()