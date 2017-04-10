# ORNLProjectLustre
Requirements: Python 2.7, NS3 python bindings (for simulator)

At client side, the OST requester module (ostRequesterClient.py) handles the requests 
and sends them to the server (ostRequestHandler.py) as HTTP GET requests.

ostRequestHandler server should be running on MDS, where the lustreLoadBalancer package should be present.
ostRequestHandler calls the lustreLoadBalancer package to map the client requests to OSTs.
lustreLoadBalancer package has all the required functionality (stats gathering, request prediction, min cost flow optimization, etc).

For running simulation, open a NS3 shell, and run lustreSimulator.py.
