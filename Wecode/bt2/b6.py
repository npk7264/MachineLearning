from sys import stdin

class node:
    def __init__(self, data):
        self.data = data
        self.left, self.right = None, None

def insert_node(root, data):
    if root == None:
        root = node(data)
        return root
    prev = None
    temp = root
    while temp != None:
        prev = temp
        if temp.data == data:
            return root
        if data < temp.data:
            temp = temp.left
        else:
            temp = temp.right
    if data < prev.data:
        prev.left = node(data)
    else:
        prev.right = node(data)
    return root

def countUnbalanceNode(root, ans):
    if root:
        left_hight_tree = countUnbalanceNode(root.left, ans)
        right_hight_tree = countUnbalanceNode(root.right, ans)
        if abs(left_hight_tree-right_hight_tree) >= 2:
            ans[0] += 1
        return 1+max(left_hight_tree,right_hight_tree)
    return 0

root = None
ans = [0]
while True:
    x = stdin.readline().strip()
    if x:
        root = insert_node(root, int(x))
    else:
        break

k = countUnbalanceNode(root, ans)
print("So node bi mat can bang la " + str(ans[0]))