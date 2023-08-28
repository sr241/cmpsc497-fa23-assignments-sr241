class _StackNode:
    def __init__( self, item, link ):
        self.item = item
        self.next = link

class Stack :
    def __init__( self ):
        self._top = None
        self._size = 0

    def peek( self ):
        assert not self.__is_empty__(), "Cannot peek at an empty stack"
        return (self._top.item)

    def push( self, item ):
        ''' Method to push an item to the top of a Stack
        '''
        pushNode = _StackNode(item, self._top)
        self._top = pushNode
        self._size += 1
	
    def pop(self):
        ''' Method to pop an item from the top of a Stack
		'''
        assert not self.__is_empty__(), "Cannot pop at an empty stack"
        popNode = self._top
        self._top = self._top.next
        self._size -= 1
        return popNode.item

    def __len__(self):
        ''' Overrides the Python len() method for Stack objects
        '''
        return self._size
		
    def __is_empty__(self):
        ''' Used to tell us whether the Stack is empty (returns a True or False)
        '''
        if self._size == 0:
            return True
        else:
            return False
        
s = Stack()
print(s.__is_empty__())
s.push(10)
s.push(20)
s.push(1)
s.push(-7)
s.push(200)
print(s.peek())
print(s.pop())
print(s.__is_empty__())
print(s.__len__())
print(s.peek())