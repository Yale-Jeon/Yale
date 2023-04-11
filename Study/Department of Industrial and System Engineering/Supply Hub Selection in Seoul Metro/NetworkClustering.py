import sys
import Prim
import Graph
import csv

class NewmanClustering:

    def __init__(self, edges = None):
        pass

    def performNewmanClustering(self, graph, K):
        lstVertexes = graph.vertexes

        while True:
            matBetweenness = self.calculateEdgeBetweenness(graph)
            maxBetweenness = 0.0
            idxSrcEdge = -1
            idxDstEdge = -1
			
            for itr1 in range(len(lstVertexes)):
                for itr2 in range(len(lstVertexes)):
                    if matBetweenness[lstVertexes[itr1]][lstVertexes[itr2]] > maxBetweenness:
                        maxBetweenness = matBetweenness[lstVertexes[itr1]][lstVertexes[itr2]]
                        idxSrcEdge = itr1
                        idxDstEdge = itr2
						
            graph.removeEdge(lstVertexes[idxSrcEdge],lstVertexes[idxDstEdge])
            graph.removeEdge(lstVertexes[idxDstEdge],lstVertexes[idxSrcEdge])
            components = graph.findComponent()
            if len(components) == K:
                break
        
        components = graph.findComponent()
        return components

    def calculateEdgeBetweenness(self, graph):
        lstVertexes = graph.vertexes
        matBetweenness = {}
        for itr1 in range(len(lstVertexes)):
            matBetweenness[lstVertexes[itr1]] = {}
            for itr2 in range(len(lstVertexes)):
                matBetweenness[lstVertexes[itr1]][lstVertexes[itr2]] = 0.0

        for itr1 in range(len(lstVertexes)):
            #sys.stdout.flush()
            vertexes, edges, routes = Prim.performPrim(graph, lstVertexes[itr1])
            for itr2 in range(len(lstVertexes)):
                if itr1 == itr2:
                    continue
            
                if routes[lstVertexes[itr2]] != None:
                    for itr3 in range(len(routes[lstVertexes[itr2]])-1):
                        srcIncludedEdge = routes[lstVertexes[itr2]][itr3]
                        dstIncludedEdge = routes[lstVertexes[itr2]][itr3+1]
                        matBetweenness[srcIncludedEdge][dstIncludedEdge] = matBetweenness[srcIncludedEdge][dstIncludedEdge] + 1
                        matBetweenness[dstIncludedEdge][srcIncludedEdge] = matBetweenness[dstIncludedEdge][srcIncludedEdge] + 1
        return matBetweenness
