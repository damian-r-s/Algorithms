class TreeNode:
    def __init__(self, key=None, val=any, size=0, left=None, right=None) -> None:
        self.key = key
        self.val = val
        self.left = left
        self.right = right
        self.size = size
        
class Tree:
    def __init__(self) -> None:
        self.root = None
    
    def put(self, key, value) -> None:
        self.root = self.__put(self.root, key, value)
    
    def __put(self, root: TreeNode, key, value) -> TreeNode:
        if root is None:
            return TreeNode(key, value, 1)
        
        if root.key == key:
            root.val = value
        elif key < root.key:
            root.left = self.__put(root.left, key, value)
        else:
            root.right = self.__put(root.right, key, value)            
        
        root.size = self.__size(root.left) + self.__size(root.right) + 1
                
        return root   
        
    def get(self, key) -> TreeNode:
        return self.__get(self.root, key) 
    
    def __get(self, root: TreeNode, key) -> any:
        if root is None:
            return None
        
        if key == root.key:
            return root.val
        
        if key < root.key:
            return self.__get(root.left, key)
        else:
            return self.__get(root.right, key)
        
    def size(self) -> int:
        return self.__size(self.root)
        
    def __size(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        return root.size
    
    def max(self) -> TreeNode:
        if self.root is None:
            return None
        return self.__max(self.root)
    
    def __max(self, root: TreeNode) -> TreeNode:
        if root.right is None:
            return root
        return self.__max(root.right)
    
    def min(self) -> TreeNode:
        if self.root is None:
            return None
        return self.__min(self.root)
    
    def __min(self, root: TreeNode) -> TreeNode:
        if root.left is None:
            return root        
        return self.__min(root.left)
    
    def ceil(self, key:any) -> TreeNode:
        if self.root is None:
            return None
        
        return self.__ceil(self.root, key)
    
    def __ceil(self, root: TreeNode, key: any):
        if root is None:
            return None        
        if root.key == key:
            return root
        elif key > root.key:
            return self.__ceil(root.right, key)
        node = self.__ceil(root.left, key)
        if node is not None:
            return node
        else:
            return root
    
    def floor(self, key:any) -> TreeNode:
        if self.root is None:
            return None
        return self.__floor(self.root, key)
    
    def __floor(self, root: TreeNode, key: any) -> TreeNode:
        if root is None:
            return None
        if root.key == key:
            return root
        elif key < root.key:
            return self.__floor(root.left, key)
        node = self.__floor(root.right, key)
        if node is not None:
            return node
        else:
            return root    
        
    def select(self, k) -> TreeNode:
        if self.root is None:
            return None
        
        return self.__select(self.root, k)
    
    def __select(self, root: TreeNode, k):
        if root is None:
            return None
        size = self.__size(root.left)
                    
        if size > k:
            return self.__select(root.left, k)
        elif size < k:
            return self.__select(root.right, k - size - 1)
        else:
            return root
    
    def rank(self, key: any) -> int:
        if self.root is None:
            return 0
        
        return self.__rank(self.root, key)
    
    def __rank(self, root: TreeNode, key: any):
        if root is None:
            return 0
        
        if root.key > key:
            return self.__rank(root.left, key)
        elif root.key < key:
            return 1 + self.__size(root.left) + self.__rank(root.right, key)
        else:            
            return self.__size(root.left)     
        
    def deleteMin(self):
        if self.root is None:
            return None        
        self.root = self.__deleteMin(self.root)
        return self.root
    
    def __deleteMin(self, root: TreeNode):
        if root.left is None:
            return root.right        
        root.left = self.__deleteMin(root.left)
        root.size = 1 + self.__size(root.left) + self.__size(root.right)                
        return root
        
    def delete(self, key):
        if self.root is None:
            return None        
        self.root = self.__delete(self.root, key)
        return self.root
    
    def __delete(self, root: TreeNode, key):
        if root is None:
            return None
        elif root.key > key:
            root.left = self.__delete(root.left, key)
        elif root.key < key:
            root.right = self.__delete(root.right, key)
        else: # found
            if root.right is None:
                return root.left
            if root.left is None:
                return root.right
            
            temporary:TreeNode = root
            root = self.__min(temporary.right)
            root.right = self.__deleteMin(temporary.right)
            root.left = temporary.left
            
        root.size = 1 + self.__size(root.left) + self.__size(root.right)
        return root