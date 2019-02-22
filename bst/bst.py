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

    def __str__(self):
        # 中序遍历 bst
        s = ''
        if self.root is None:
            return ''
        stack = [(1, self.root)]

        while stack:
            type, node = stack.pop()
            if type == 0:
                s += str(node.key) + ','
            else:
                if node.right:
                    stack.append((1, node.right))
                stack.append((0, node))
                if node.left:
                    stack.append((1, node.left))
        return s[:-1]

    def size(self):
        return self.get_size(self.root)

    def get_size(self, node):
        if node is None:
            return 0
        else:
            return node.N

    def get(self, key):
        return self.__get(self.root, key)

    def __get(self, node, key):
        if node is None:
            return None
        if key < node.key:
            return self.__get(node.left, key)
        elif key > node.key:
            return self.__get(node.right, key)
        else:
            return node.val

    def put(self, key, val):
        # 注意：这里是赋值的关系
        self.root = self.__put(self.root, key, val)

    def __put(self, node, key, val):
        if node is None:
            # 注意：这里叶子结点要把 1 传进去
            return BST.Node(key, val, 1)
        # 此时 node 不为空
        if key < node.key:
            node.left = self.__put(node.left, key, val)
        elif key > node.key:
            node.right = self.__put(node.right, key, val)
        else:
            # 更新
            node.val = val

        # 注意这一行代码
        node.N = self.get_size(node.left) + self.get_size(node.right) + 1
        # 注意：最后都要将 node 返回回去
        return node

    def remove(self, val):
        """
        删除 bst 中等于 val 的结点
        :param val:
        :return:
        """
        if self.root:
            self.root = self.__remove(self.root, val)

    def __remove(self, node, val):
        if node is None:
            return None
        if val < node.val:
            node.left = self.__remove(node.left, val)
            return node
        if val > node.val:
            node.right = self.__remove(node.right, val)
            return node

        if node.left is None:
            new_root = node.right
            node.right = None
            return new_root

        if node.right is None:
            new_root = node.left
            node.left = None
            return new_root

        # 用前驱结点 precursor 代替被删除结点
        precursor = self.__maximum(node.left)
        precursor_copy = BST.Node(precursor.val)
        precursor_copy.left = self.__remove_max(node.left)
        precursor_copy.right = node.right
        node.left = None
        node.right = None
        return precursor_copy

    def __maximum(self, node):
        while node.right:
            node = node.right
        return node

    def __remove_max(self, node):
        if node.right is None:
            new_root = node.left
            node.left = None

            return new_root
        node.right = self.__remove_max(node.right)
        return node

    def ceiling(self, val):
        return self.__ceiling(self.root, val)

    def __ceiling(self, node, val):
        if node is None:
            return None
        if node.val == val:
            return node.val
        if val > node.val:
            return self.__ceiling(node.right, val)
        temp_val = self.__ceiling(node.left, val)
        if temp_val:
            return temp_val
        return node.val

    def floor(self, val):
        return self.__floor(self.root, val)

    def __floor(self, node, key):
        # floor, 地板，返回以 node 为根的二分搜索树中，小于等于 key 的最大值
        if node is None:
            return None
        if node.key == key:
            return node.val
        if key < node.key:
            return self.floor(node.left.key)

        assert key >= node.key
        temp_val = self.floor(node.right, key)
        if temp_val:
            return temp_val
        return node.val


if __name__ == '__main__':
    bst = BST()
    bst.put(1, 100)
    bst.put(2, 200)
    bst.put(3, 300)
    bst.put(4, 400)

    print(bst)
