import unittest
import BinarySearchTree as BST

class BinarySearchTreeUnitTests(unittest.TestCase):
    def setUp(self) -> None:
        self.bst = BST.Tree()
        
    def test_empty_tree_has_size_zero(self):
        self.assertEqual(self.bst.size(), 0, 'Empty BTS must have size equal to zero!')
        
    def test_root_node_has_size_equal_to_one(self):
        self.bst.put('A', 1)
        self.assertEqual(self.bst.size(), 1, 'One node in the tree must have size equal to 1!')
        
    def test_root_node_has_size_equal_to_two_if_two_nodes_added(self):
        self.bst.put('A', 1)
        self.bst.put('B', 2)
        self.assertEqual(self.bst.size(), 2, 'Two nodes in the tree make the size of the tree equal to two!')
        
    def test_min_returns_none_if_tree_is_empty(self):        
        self.assertEqual(self.bst.min(), None, 'Minimum does not exist in empty tree!')
        
    def test_if_only_one_node_then_it_is_the_minimum(self):        
        self.bst.put('Z', 100)
        self.assertEqual(self.bst.min().key, 'Z', 'If only root present then minimum equals this node!')
        self.assertEqual(self.bst.min().val, 100, 'If only root present then minimum equals this node!')
        
    def test_minimum_is_found_correctly(self):        
        self.bst.put('r', 5)
        self.bst.put('m', 10)
        self.bst.put('o', 15)
        self.bst.put('p', 20)
        self.bst.put('z', 25)
        self.bst.put('a', 30)
        self.bst.put('b', 35)
        
        self.assertEqual(self.bst.min().key, 'a', 'Minimum key should be a')
        
    def test_max_returns_none_if_tree_is_empty(self):        
        self.assertEqual(self.bst.max(), None, 'Maximum does not exist if tree is empty!')
        
    def test_if_only_one_node_then_it_is_the_maximum(self):        
        self.bst.put('A', 100)
        self.assertEqual(self.bst.max().key, 'A', 'If only root present then maximum equals this node!')
        self.assertEqual(self.bst.max().val, 100, 'If only root present then maximum equals this node!')
        
    def test_maximum_is_found_correctly(self):        
        self.bst.put('r', 5)
        self.bst.put('m', 10)
        self.bst.put('o', 15)
        self.bst.put('p', 20)
        self.bst.put('z', 25)
        self.bst.put('a', 30)
        self.bst.put('b', 35)
        
        self.assertEqual(self.bst.max().key, 'z', 'Maximum key should be z')
        
    def test_floor_return_none_if_tree_is_empty(self):
        self.assertEqual(self.bst.floor('a'), None, 'If tree is empty then floor equals None!')
        
    def test_floor_is_on_the_left_found_correctly(self):
        self.bst.put('d', 5)
        self.bst.put('r', 10)
        self.bst.put('b', 15)
        self.bst.put('a', 20)
        
        self.assertEqual(self.bst.floor('c').key, 'b', 'The floor should be b!')
    
    def test_floor_is_on_the_right_found_correctly(self):
        self.bst.put('c', 5)
        self.bst.put('p', 15)
        self.bst.put('r', 20)
        self.bst.put('a', 25)
        self.bst.put('b', 30)        
        self.bst.put('o', 15)
        
        self.assertEqual(self.bst.floor('s').key, 'r', 'The floor should be r!')
        self.assertEqual(self.bst.floor('q').key, 'p', 'The floor should be o!')

if __name__ == '__main__':
    unittest.main()   