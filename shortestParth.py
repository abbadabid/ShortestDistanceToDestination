import heapq
class Node:
    def __init__(self, name = None , distance=float('inf')):
        self.distance = distance
        self.name = name
        self.parent = []
    
    def printNode(self):
        print(self.name, self.parent, self.distance)

class Graph:

    def __init__(self):
        self.Nodes = {}
        self.adjList = {}
    
    def addEdge(self, from_node, to_node, weight):
        if from_node not in self.Nodes:
            self.Nodes[from_node] = Node(from_node)
            self.adjList[from_node] = []

        if to_node not in self.Nodes:
            self.Nodes[to_node] = Node(to_node)
            self.adjList[to_node] = []
        
        self.adjList[from_node].append([to_node, weight])
        self.adjList[to_node].append([from_node, weight])
    

class Solution:

    def calculateShortestPath(self, obj: Graph) -> Graph:
        pq = []
        heapq.heappush(pq, (0, 0)) 

        obj.Nodes[0].distance = 0  

        while pq:
            currentDistance, currentNodeName = heapq.heappop(pq)
            currentNode = obj.Nodes[currentNodeName] 

            if currentDistance > currentNode.distance:
                continue

            for neighbor, weight in obj.adjList[currentNode.name]:
                newDistance = currentDistance + weight

                if newDistance < obj.Nodes[neighbor].distance:
                    obj.Nodes[neighbor].distance = newDistance
                    obj.Nodes[neighbor].parent = [currentNode]
                    heapq.heappush(pq, (newDistance, neighbor))  

                elif newDistance == obj.Nodes[neighbor].distance:
                    if currentNode not in obj.Nodes[neighbor].parent:
                        obj.Nodes[neighbor].parent.append(currentNode)

        return obj

    
    def findPaths(self, node, all_paths) -> int:
        if node.name == 0:  
            return 1  

        count = 0
        for parent in node.parent:
            count += self.findPaths(parent, all_paths) 

        return count




    def countPaths(self, n: int, roads: list[list[int]]) -> int:
        MOD = 10**9 + 7  
        
        graph = {i: [] for i in range(n)}
        for u, v, w in roads:
            graph[u].append((v, w))
            graph[v].append((u, w))

        pq = [(0, 0)]  
        distances = [float('inf')] * n
        distances[0] = 0
        ways = [0] * n  
        ways[0] = 1  

        while pq:
            currDist, node = heapq.heappop(pq)

            if currDist > distances[node]:  
                continue
            
            for neighbor, weight in graph[node]:
                newDist = currDist + weight

                if newDist < distances[neighbor]:  
                    distances[neighbor] = newDist
                    ways[neighbor] = ways[node]  
                    heapq.heappush(pq, (newDist, neighbor))

                elif newDist == distances[neighbor]:  
                    ways[neighbor] = (ways[neighbor] + ways[node]) % MOD

        return ways[n-1] 
 
obj = Solution()    
print(obj.countPaths( 7 , [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]] ))
