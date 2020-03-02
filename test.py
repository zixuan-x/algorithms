def topological_sort(vertices, edges):
    # initialization
    sortedOrder = []
    g = {}  # adjacency list
    visited = set()

    # build adjacency list
    for src, des in edges:
        if src not in g:
            g[src] = []
        g[src].append(des)

        # pick starting points
    for s in g:
        if s not in visited:
            # dfs
            dfs(s, g, sortedOrder, visited)

    sortedOrder.reverse()
    return sortedOrder


def dfs(s, g, sortedOrder, visited):
    # mark current node as visited
    visited.add(s)
    # visit neighbors
    for neighbor in g[s]:
        if neighbor not in visited:
            dfs(neighbor, g, sortedOrder, visited)
    # add current node to sortedOrder
    sortedOrder.append(s)

def main():
  print("Topological sort: " +
        str(topological_sort(4, [[3, 2], [3, 0], [2, 0], [2, 1]])))
  print("Topological sort: " +
        str(topological_sort(5, [[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]])))
  print("Topological sort: " +
        str(topological_sort(7, [[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]])))


main()