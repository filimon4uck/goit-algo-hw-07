class AVLNode:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None

    def __str__(self, level=0, prefix="Root: "):
        ret = "\\t" * level + prefix + str(self.key) + "\\n"
        if self.left:
            ret += self.left.__str__(level + 1, "L--- ")
        if self.right:
            ret += self.right.__str__(level + 1, "R--- ")
        return ret


def get_height(node):
    if not node:
        return 0
    return node.height


def get_balance(node):
    if not node:
        return 0
    return get_height(node.left) - get_height(node.right)


def left_rotate(z):
    y = z.right
    T2 = y.left

    y.left = z
    z.right = T2

    z.height = 1 + max(get_height(z.left), get_height(z.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))

    return y


def right_rotate(y):
    x = y.left
    T3 = x.right

    x.right = y
    y.left = T3

    y.height = 1 + max(get_height(y.left), get_height(y.right))
    x.height = 1 + max(get_height(x.left), get_height(x.right))

    return x


def insert(root, key):
    if not root:
        return AVLNode(key)

    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    else:
        return root

    root.height = 1 + max(get_height(root.left), get_height(root.right))

    balance = get_balance(root)

    if balance > 1:
        if key < root.left.key:
            return right_rotate(root)
        else:
            root.left = left_rotate(root.left)
            return right_rotate(root)

    if balance < -1:
        if key > root.right.key:
            return left_rotate(root)
        else:
            root.right = right_rotate(root.right)
            return left_rotate(root)

    return root


def max_el(node: AVLNode):
    if node.right is None:
        return node.key
    return max_el(node.right)


def min_el(node: AVLNode):
    if node.left is None:
        return node.key
    return min_el(node.left)


def sum_elements(node: AVLNode):
    if node:
        return node.key + sum_elements(node.left) + sum_elements(node.right)
    return 0


print("Minimun =  ")


def main():
    root = AVLNode(6)
    root = insert(root, 5)
    root = insert(root, 4)
    root = insert(root, 3)
    root = insert(root, 2)
    root = insert(root, 1)

    print(root)
    print("Maximum = ", max_el(root))
    print("Minimum = ", min_el(root))
    print("Sum = ", sum_elements(root))


if __name__ == "__main__":
    main()
