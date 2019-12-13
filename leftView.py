class Node:

    #Constructor for a new node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None
    
    #Recursive function to print left view of the tree
    def leftView(root, level, max_level):

        #Base case:
        if root is None:
            return
        
        #If this is the first node of it's level
        if(max_level[0] < level):
            print "% d\t" %(root.data), 
            max_level[0] = level 
        
        #Recur for left and right subtree
        leftView(root.left, level + 1, max_level)
        leftView(root.rightt, level + 1, max_level)

        #A wrapper 
    def leftViewUtil(root):
        max_level = [0]
        leftView(root, 1, max_level)
