import networkx as nx

class MinCostFlowOptimizer(object):
	def map_requests(self, requests, osts):
		totalDemand = sum([req.numStripes for req in requests])
		stripeSize = requests[0].stripeSize
		G = nx.DiGraph()
		G.add_node('source', demand=-totalDemand)
		G.add_node('sink', demand=totalDemand)
		for req in requests:
			G.add_edge('source', req.name, weight=0, capacity=req.numStripes)
			for ost in osts:
				G.add_edge(req.name, ost.name, weight=ost.cost_to_reach(), capacity=1)
		for ost in osts:
			G.add_edge(ost.name, 'sink', weight=ost.cost(), capacity=ost.capacity(stripeSize))
		flowCost, flowDict = nx.capacity_scaling(G)
		ostWeights = flowDict['req0']
		ostNames = []
		for ost, weight in ostWeights.iteritems():
			if weight > 0:
				ostNames.append(ost)
		return tuple([ostNames, flowCost])