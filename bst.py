class BST:
    class Node:
        def __init__(self, key, val, N):
            self.key = key
            self.val = val
            # 以该结点为根的子树中的结点总数
            self.N = N
            # 指向子树的链接
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def size(self):
        return self.get_size(self.root)

    def get_size(self, node):
        if node is None:
            return 0
        else:
            return node.N

    def get(self, key):
        return self.__get_from_node(self.root, key)

    def __get_from_node(self, node, key):
        if node is None:
            return None
        if key < node.key:
            return self.__get_from_node(node.left, key)
        elif key > node.key:
            return self.__get_from_node(node.right, key)
        else:
            return node.val

    def put(self, key, val):
        # 注意：这里是赋值的关系
        self.root = self.__put_to_bst(self.root, key, val)

    def __put_to_bst(self, node, key, val):
        if node is None:
            # 注意：这里叶子结点要把 1 传进去
            return BST.Node(key, val, 1)
        # 此时 node 不为空
        if key < node.key:
            node.left = self.__put_to_bst(node.left, key, val)
        elif key > node.key:
            node.right = self.__put_to_bst(node.right, key, val)
        else:
            # 更新
            node.val = val

        # 注意这一行代码
        node.N = self.get_size(node.left) + self.get_size(node.right) + 1
        # 注意：最后都要将 node 返回回去
        return node


if __name__ == '__main__':
    bst = BST()
    bst.put(1, 100)
    bst.put(2, 200)
    bst.put(3, 300)
    bst.put(4, 400)

    print(bst.size())
