# Count number of nodes in a complete tree. The solution is of Order log^2 N
# I am defining a function to define a TreeNode from the list

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return f"TreeNode({self.value})"


def build_complete_binary_tree(elements):
    """
    Builds a complete binary tree from a list of elements.
    The first element is the root, the second is the left child,
    the third is the right child, and so on.
    """
    if not elements:
        return None

    # Create a list of TreeNode objects
    nodes = [TreeNode(value) for value in elements]

    # Link parent and children
    for i in range(len(nodes)):
        left_index = 2 * i + 1
        right_index = 2 * i + 2

        if left_index < len(nodes):  # Set the left child
            nodes[i].left = nodes[left_index]
        if right_index < len(nodes):  # Set the right child
            nodes[i].right = nodes[right_index]

    return nodes[0]  # Return the root node


# Function to display the tree structure
def print_tree(node, level=0):
    if node is not None:
        print(" " * (level * 4) + f"- {node.value}")
        print_tree(node.left, level + 1)
        print_tree(node.right, level + 1)





class Solution:
    def countNodes(self, root) -> int:
        if not root:
            return 0
        node = root
        l, r = 1, 1
        while node.left:
            l += 1
            node = node.left
        node = root
        while node.right:
            r += 1
            node = node.right

        if l == r:
            return 2 ** l - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)

if __name__ == '__main__':
    # Example usage
    elements = [1, 2, 3, 4, 5, 6, 7, 8, 12]
    root = build_complete_binary_tree(elements)

    print_tree(root)

    S = Solution()
    res = S.countNodes(root)
    print(res)