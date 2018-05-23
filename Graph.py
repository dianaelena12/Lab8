import time
import copy

class Graph:
    def __init__(self, fileName):
        self.fileName = fileName
        # one node has the next form: 1:[2,3,4]
        self.nodes = {}
        self.readFromFile()

    def readFromFile(self):
        start = time.time()
        file = open(self.fileName, "r")
        firstLine = file.readline()[:-1].split(" ")
        nrOfNodes = int(firstLine[0])
        nrOfEdges = int(firstLine[1])
        for i in range(nrOfNodes):
            self.nodes[str(i)] = []
        for i in range(nrOfEdges):
            currentLine = file.readline()[:-1].split(" ")
            _from = currentLine[0]
            _to = currentLine[1]
            _cost = currentLine[2]
            self.nodes[_from].append(_to)
            self.nodes[_to].append(_from)
        stop = time.time()
        print("Loaded file {0} in {1} seconds".format(self.fileName, stop - start))

    def dfs(self, start):
        '''
        :param start: the starting node for the search
        :return: -the list of nodes that are connected
                 -an empty list
        I put in the list the first node. While the list q, containing the nodes to visit is not empty
        I pop it's first element, check if it was visited: - if yes, I get the next element, if not I add it to the
        path, in the same time, I add the nodes in it's inbound list.When there are no more nodes to visit, I return the
        path
        '''
        path = []
        q = [start]
        while q:
            v = q.pop(0)
            if v not in path:
                path = path + [v]
                q = self.nodes[v] + q
        return path

    def getNodes(self):
        return self.nodes

def checkIfEqual(lista1, lista2):
    for i in lista1:
        if i not in lista2:
            return 0
    return 1


if __name__ == '__main__':
    a = Graph("graph1k.txt")
    nodes = a.getNodes()
    prev = []
    for i in nodes:
        lista = a.dfs(i)
        if checkIfEqual(lista,prev) == 0:
            if len(lista) <= 0:
                print("The node does not exist")
            else:
                print("Component", lista)
        prev = copy.deepcopy(lista)