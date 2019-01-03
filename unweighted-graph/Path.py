class Path:
    def __init__(self, graph, source):
        self.graph = graph
        assert 0 <= source < self.graph.V()
        self.visited = [False] * self.graph.V()
        self.from_ = [-1] * self.graph.V()
        self.source = source
        self.__dfs(source)

    def __dfs(self, v):
        self.visited[v] = True
        for v_neighbour in self.graph.iterator(v):
            if not self.visited[v_neighbour]:
                self.from_[v_neighbour] = v
                self.__dfs(v_neighbour)

    def has_path(self, w):
        assert 0 <= w < self.graph.V()
        return self.visited[w]

    def path(self, w):
        assert self.has_path(w)
        stack = []

        p = w
        while p != -1:
            stack.append(p)
            p = self.from_[p]

        path = []
        while stack:
            path.append(stack.pop())
        return path

    def show_path(self, w):
        assert self.has_path(w)
        path = self.path(w)
        # print('路径',path)
        print(" -> ".join(map(lambda x: str(x), path)))
