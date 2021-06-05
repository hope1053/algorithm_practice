import sys
sys.setrecursionlimit(10**6)

X, Y = 0, 1

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
class NodeMgmt:
    def __init__(self, head):
        self.head = head
        
    def insert(self, value):
        self.current_node = self.head
        
        while True:
            if value[X] < self.current_node.value[X]:
                if self.current_node.left != None:
                    self.current_node = self.current_node.left
                else:
                    self.current_node.left = Node(value)
                    break
            else:
                if self.current_node.right != None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(value)
                    break

def solution(nodeinfo):
    answer = list()
    # 그래프 그리기
    nodeinfo = sorted([value + [idx + 1] for idx, value in enumerate(nodeinfo)], key = lambda x:-x[1])
    tree = make_tree(nodeinfo)
    # 전위순환
    pre_arr, post_arr = list(), list()
    
    order_tree(tree, tree.head, pre_arr, post_arr)
    # # 후위순환
    # postorder(tree, tree.head, post_arr)
    
    return [pre_arr, post_arr]
    
def make_tree(nodeinfo):
    head_node = Node(nodeinfo[0])
    tree = NodeMgmt(head_node)
    for idx in range(1, len(nodeinfo)):
        tree.insert(nodeinfo[idx])
        
    return tree
    
def order_tree(tree, node, pre_arr, post_arr):
    if node == None:
        return
    pre_arr.append(node.value[-1])
    order_tree(tree, node.left, pre_arr, post_arr)
    order_tree(tree, node.right, pre_arr, post_arr)
    post_arr.append(node.value[-1])