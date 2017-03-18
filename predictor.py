
NUM_OF_PREDICTED_REQUESTS = 0

class RequestPredictor(object):
	def __init__(self):
		self.appIDtoModelDict = {}
		self.numPredictedRequests = NUM_OF_PREDICTED_REQUESTS

	def get_requests(self, appID, stripeSize, numStripes):
		currRequest = Request("req0", stripeSize, numStripes)
		reqList = [currRequest]
		for i in range(self.numPredictedRequests):
			reqName = "req{0}".format(i+1)
			req = Request(reqName, stripeSize, numStripes)
			reqList.append(req)
		return reqList

class Request(object):
	def __init__(self, name, stripeSize, numStripes):
		self.name = name
		self.numStripes = numStripes
		self.stripeSize = stripeSize
		self.size = stripeSize * numStripes