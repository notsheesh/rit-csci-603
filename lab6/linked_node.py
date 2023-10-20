from typing import Any

class LinkedNode: 
    __slots__ = "_value", "_link"
    _value: Any
    _link: 'LinkedNode'

    def __init__(self: 'LinkedNode', value: Any, link: 'LinkedNode' = None) -> None:
        self._value = value
        self._link = link
    
    def set_link(self: 'LinkedNode', link: 'LinkedNode') -> None:
        self._link = link
    
    def get_link(self: 'LinkedNode') -> 'LinkedNode':
        return self._link

    def set_value(self: 'LinkedNode', value: Any) -> None:
        self._value = value
    
    def get_value(self: 'LinkedNode') -> Any:
        return self._value

def test():
    # test LinkedNode
    pass

def main():
    test()

if __name__ == '__main__':
    main()