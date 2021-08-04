# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

def findTarget(tree, target):
    if tree == None:
        return False

    if tree.val == target:
        return True
    
    if tree.val < target:
        return findTarget(tree.right, target)
    else:
        return findTarget(tree.left, target)


# if __name__ == "__main__":

#     tree = {2, 3 ,5, 7, 9, 11, 33}
#     target = 7
#     ans = findTarget(tree, target)
#     print(ans)




