from time import time
from random import randint


#Stack implementation
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
    def size(self):
        return len(self.items)

#Based on the Pseudo code
def InfPath(G, V):
    colors = {v : "white" for v in G}
    S = Stack()
    colors[V] = "grey"
    S.push(V)
    maxStackSize = 0
    while not S.is_empty():
        if (S.size() > maxStackSize): maxStackSize = S.size()
        u = S.top()
        neighbor = findNeighbor(G, u, colors)
        if neighbor[0] == "grey":
            # print "grey neighbor"
            return [True, maxStackSize]
        elif neighbor[0] == "white":
            # print "white neighbor"
            colors[neighbor[1]] = "grey"
            S.push(neighbor[1])
        else:
            colors[u] = "black"
            S.pop()
    return [False, maxStackSize]

#Finds neighbors of u which are "grey"
#If none "grey" then find "white" neighbor
#If none "white" then return ["black"] - done with u
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


#Function to print graph attributes and layout
def printGraph(G):
    node_count = len(G)
    incoming_arcs_count = [0] * node_count
    outgoing_arcs_count = [0] * node_count
    for node in G:
         outgoing_arcs_count[node-1] = len(G[node])
         for arc in G[node]:
             incoming_arcs_count[arc-1] += 1

    avg_incoming = sum(incoming_arcs_count)/float(len(outgoing_arcs_count))
    max_incoming = max(incoming_arcs_count)
    min_incoming = min(incoming_arcs_count)

    avg_outgoing = sum(outgoing_arcs_count)/float(len(outgoing_arcs_count))
    max_outgoing = max(outgoing_arcs_count)
    min_outgoing = min(outgoing_arcs_count)

    # the maximum, minimum and average number of outgoing and incoming arcs from and to a node
    print "Number of nodes: " + str(node_count)
    print "Number of arcs: " + str(sum(incoming_arcs_count))
    print "Average Number of Incoming Arcs: " + str(avg_incoming)
    print "Minimum Number of Incoming Arcs: " + str(min_incoming)
    print "Maximum Number of Incoming Arcs: " + str(max_incoming)
    print "Average Number of Outgoing Arcs: " + str(avg_outgoing)
    print "Minimum Number of Outgoing Arcs: " + str(min_outgoing)
    print "Maximum Number of Outgoing Arcs: " + str(max_outgoing)
    return [node_count, sum(incoming_arcs_count)]

#Tests graph for all nodes - if p print info on all nodes
def testGraph(G, p):
    print len(G)
    time_taken = [0.0] * len(G)
    stack_size = [0] * len(G)
    for i in range(1, len(G)+1):
        t0 = time()
        result = InfPath(G, i)
        t1 = time()
        timediff = t1-t0
        time_taken[i-1] = timediff
        stack_size[i-1] = result[1]
        if (p):
            print "For Node: " + str(i)
            print "Output: %s" % (result[0])
            print "Max Stack Size: " + str(result[1])
            print 'Time taken: %f' %(timediff)
    print "Results for all nodes: "
    print "Max Stack Size: " + str(max(stack_size))
    print "Avg Stack Size: " + str(sum(stack_size)/float(len(stack_size)))
    print "Max Time Taken: " + str(max(time_taken))
    print "Avg Time Taken: " + str(sum(time_taken)/float(len(time_taken)))
    return [sum(stack_size)/float(len(stack_size)), sum(time_taken)/float(len(time_taken))]

#generates a Graph with V nodes and A arcs, needs to be passed V > 1
def genGraph(V, A):
    G = {}
    for i in range (1, V+1):
        G[i] = []
    for j in range (0, A):
        rand_Start = randint(1,V)
        rand_End = randint(1,V)
        while (rand_End == rand_Start): rand_End = randint(1,V)
        if (not rand_End in G[rand_Start]): G[rand_Start].append(rand_End)
    return G

##Examples:
print "Examples from Assignment: "
print "Graph: A"
GA = {
    1: [2, 4],
    2: [5, 3],
    3: [6],
    4: [5, 7],
    5: [1, 3, 6, 9, 8],
    6: [9],
    7: [5, 8],
    8: [9],
    9: []
    }
print GA
printGraph(GA)
testGraph(GA, True)

print "Graph: B"
GB = {
        1: [2, 4],
        2: [5, 3],
        3: [5, 6],
        4: [5, 7, 8],
        5: [6, 8],
        6: [9],
        7: [8],
        8: [9],
        9: []
    }
print GB
printGraph(GB)
testGraph(GA, True)
#
# print "Graph: C"
# GC = {
#     1: [2, 3, 4],
#     2: [5],
#     3: [6],
#     4: [6],
#     5: [7],
#     6: [],
#     7: []
#     }
# print GC
# printGraph(GC)
# testGraph(GC, True)
#
# print "Graph: D"
# GD = {
#     1: [2],
#     2: [3, 4],
#     3: [5],
#     4: [5],
#     5: [2]
#     }
# print GD
# printGraph(GD)
# testGraph(GD, True)

## Testing Impact With Large Graphs:
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

NCount = []
SSizesNCount = []
TimesNCount = []
ACount = []
SSizesACount = []
TimesACount = []

for i in range (21800, 21850, 5):
    tempG = genGraph(i, 100000)
    tempPrint = printGraph(tempG)
    NCount.append(tempPrint[0])
    tempResult = testGraph(tempG, False)
    SSizesNCount.append(tempResult[0])
    TimesNCount.append(tempResult[1])
    print "i: " + str(i)
    print "NCOUNT: "
    print NCount
    print "SSizesNCount"
    print SSizesNCount
    print "TimesNCount"
    print TimesNCount


# for j in range (10000, 500000, 1000):
#     tempG = genGraph(10000, j)
#     tempPrint = printGraph(tempG)
#     ACount.append(tempPrint[1])
#     tempResult = testGraph(tempG, False)
#     SSizesACount.append(tempResult[0])
#     TimesACount.append(tempResult[1])
#     print "j: " + str(j)

######NODE # EFFECT
print "Effect of varying Node count on Stack Size: "
x = np.asarray(NCount)
y = np.asarray(SSizesNCount)
slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
print "Slope: " + str(slope)
print "Intercept: " + str(slope)
print "std_err: " + str(std_err)

plt.plot(NCount, SSizesNCount, 'ro')
plt.axis([0, 50000, 0, max(SSizesNCount)+10])
plt.xlabel('Node Count')
plt.ylabel('Avg Stack Size')
plt.title('Space Complexity ')
plt.show()

print "Effect of varying Node count on Time: "
x = np.asarray(NCount)
y = np.asarray(TimesNCount)
slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
print "Slope: " + str(slope)
print "Intercept: " + str(slope)
print "std_err: " + str(std_err)

plt.plot(NCount, TimesNCount, 'bo')
plt.axis([0, 50000, 0, max(TimesNCount)+0.001])
plt.xlabel('Node Count')
plt.ylabel('Avg Time')
plt.title('Time Complexity')
plt.show()

##### ARC # EFFECT
# print "Effect of varying Arc count on Stack Size: "
# x = np.asarray(ACount)
# y = np.asarray(SSizesACount)
# slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
# print "Slope: " + str(slope)
# print "Intercept: " + str(slope)
# print "std_err: " + str(std_err)
#
# plt.plot(ACount, SSizesACount, 'ro')
# plt.axis([0, 501000, 0, max(SSizesACount)+10])
# plt.ylabel('Avg Stack Size')
# plt.xlabel('Arc Count')
# plt.title('Space Complexity ')
# plt.show()
#
# print "Effect of varying Arc count on Time: "
# x = np.asarray(ACount)
# y = np.asarray(TimesACount)
# slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
# print "Slope: " + str(slope)
# print "Intercept: " + str(slope)
# print "std_err: " + str(std_err)
#
# plt.plot(ACount, TimesACount, 'bo')
# plt.axis([0, 501000, 0, max(TimesACount)+0.001])
# plt.ylabel('Avg Time')
# plt.xlabel('Arc Count')
# plt.title('Time Complexity')
# plt.show()
