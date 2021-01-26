# All Paths From Source to Target

# Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1, and return them in any order.

# The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []
        
        def recurse(path):
            if not path:
                return
            if len(path)>0 and path[-1]==len(graph)-1:
                result.append(path)
                return
            for i in graph[path[-1]]:
                print('a')
                recurse(path+[i])
        recurse([0])
        return result