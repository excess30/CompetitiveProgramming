class Node:
    #Constructor to create a new node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def findMinMax(node, min, max, hd):
#Base Case
    if node is None:
        return
    if hd < min:
        min = hd
    elif hd > max:
        max[0] = hd

def printVerticalLines(node, line_no, hd):
    if node is None:
        return
    if hd == line_no:
        print node.data,

    printVerticalLines(node.left, line_no, hd-1)
    printVerticalLines(node.right, line_no, hd+1) 
  
def verticalOrder(root): 
      
    # Find min and max distances with respect to root 
    minimum = [0] 
    maximum = [0] 
    findMinMax(root, minimum, maximum, 0) 
  
    # Iterate through all possible lines starting  
    # from the leftmost line and print nodes line by line 
    for line_no in range(minimum[0], maximum[0]+1): 
        printVerticalLines(root, line_no, 0) 
        print 
           
  
# Driver program to test above function 
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
root.right.left = Node(6) 
root.right.right = Node(7) 
root.right.left.right = Node(8) 
root.right.right.right = Node(9) 
  
print "Vertical order traversal is"
verticalOrder(root) 

    


