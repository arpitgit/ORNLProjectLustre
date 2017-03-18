from gatherer import SimStatsGatherer, RealStatsGatherer
from predictor import RequestPredictor
from optimizer import MinCostFlowOptimizer

class RequestMapper(object):
	def __init__(self, simulator=None):
		if simulator:
			self.statsGatherer = SimStatsGatherer(simulator)
		else:
			self.statsGatherer = RealStatsGatherer()
		self.requestPredictor = RequestPredictor()
		self.flowOptimizer = MinCostFlowOptimizer()

	def get_osts_for_request(self, appID, stripeSize, numStripes):
		requests = self.requestPredictor.get_requests(appID, stripeSize, numStripes)
		self.statsGatherer.gather_and_update()
		ostList = self.statsGatherer.model.ostDict.values()
		ostNames, cost = self.flowOptimizer.map_requests(requests, ostList)
		print "stripeCount = {0}, cost = {1}, osts = {2}".format(numStripes, cost, ostNames)
		return tuple([ostNames, cost])