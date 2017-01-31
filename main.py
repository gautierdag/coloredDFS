

class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def top(self):
        return self.items[len(self.items)-1]
    def is_empty(self):
        return (self.items == [])


def InfPath(G, V):
    colors = {v : "white" for v in G}
    S = Stack()
    colors[V] = "grey"
    S.push(V)
    while not S.is_empty():
        u = S.top()
        temp = findNeighbor(G, u, colors)
        if temp[0] == "grey":
            print "grey neighbor"
            return True
        elif temp[0] == "white":
            print "white neighbor"
            colors[temp[1]] = "grey"
            S.push(temp[1])
        else:
            colors[u] = "black"
            S.pop()
    return False

def findNeighbor(G, u, colors):
    color = "grey"
    for m in G[u]:
        if colors[m] == color:
            return ["grey", m]
    color = "white"
    for m in G[u]:
        if colors[m] == color:
            return ["white", m]
    return ["black"]

#vertex u = top of S //access top item without removing it from S
#         if u has neighbor with color = grey:
#             return TRUE
#         else if u has a neighbor m with color = white:
#             Set m.color = grey
#             S.push(m)


G = {
    0 : [1],
    1 : [2],
    2 : [3],
    3 : [4],
    4 : []
    }

V = 1

print InfPath(G, V)





#     for u in G:
#         if color[u] == "white":
#             dfs_visit(G, u, color, found_cycle)
#         if found_cycle:
#             break
#     return found_cycle
#
# def dfs_visit(G, u, color, found_cycle):
#     if found_cycle:
#         return
#     color[u] = "gray"
#     for v in G[u]:
#         if color[v] == "gray":
#             found_cycle = True
#         if color[v] == "white":
#             dfs_visit(G, v, color, found_cycle)
#     color[u] = "black"

# print(cycle_exists(G))
