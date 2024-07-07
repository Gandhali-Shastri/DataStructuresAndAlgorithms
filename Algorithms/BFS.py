from collections import deque


def bfs(node):
    visited = [node]
    queue = deque(node)

    while queue:
        n = queue.popleft()
        neighbors = graph[n]

        for nei in neighbors:
            if nei not in visited:
                visited.append(nei)
                queue.append(nei)

    return visited


if __name__ == "__main__":
    graph = {
        'f': ['g', 'i'],
        'g': ['h'],
        'h': [],
        'i': ['g', 'k'],
        'j': ['i'],
        'k': []
    }
    print(bfs('f'))

    # graph = {
    #     'a': ['b', 'd'],
    #     'b': ['c', 'f'],
    #     'c': ['e', 'g'],
    #     'g': ['e'],
    #     'e': ['b', 'f'],
    #     'f': ['a'],
    #     'd': ['f']
    # }
    # print(bfs('a'))


