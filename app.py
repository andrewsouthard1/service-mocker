import json
import logging
import mocks

from flask import Flask
from flask import request
from mocks.rabbitmq import mock_rmq
from mocks.mesos_slave import mock_mesos_slv
from mocks.mesos_slave import state, stats
#from flask import Response
from ddtrace import tracer
from ddtrace.contrib.flask import TraceMiddleware

app = Flask(__name__)
traced_app = TraceMiddleware(app, tracer, service="mocker", distributed_tracing=False)
logger = logging.getLogger('werkzeug')
handler = logging.FileHandler('logs/access.log')
logger.addHandler(handler)

@app.route("/mesos_slave/state.json", methods=["GET"])
def mock_mesos_slave():
    #return mock_mesos_slv()
    return state()

@app.route("/mesos_slave/metrics/snapshot", methods=["GET"])
def mock_mesos_slave_stats():
    return stats()

@app.route("/whatsmyip", methods=["GET"])
def get_my_ip():
    return request.environ['REMOTE_ADDR'], 200

@app.route("/rabbitmq/queues", methods=["GET"])
def mock_rabbitmq():
     return mock_rmq()

@app.route("/redisdb/cluster_nodes", methods=["GET"])
def mock_redisdb_cluster_nodes():
     str = """07c37dfeb235213a872192d90877d0cd55635b91 127.0.0.1:30004 slave e7d1eecce10fd6bb5eb35b9f99a514335d9ba9ca 0 1426238317239 4 connected
67ed2db8d677e59ec4a4cefb06858cf2a1a89fa1 127.0.0.1:30002 master - 0 1426238316232 2 connected 5461-10922
292f8b365bb7edb5e285caf0b7e6ddc7265d2f4f 127.0.0.1:30003 master - 0 1426238318243 3 connected 10923-16383
6ec23923021cf3ffec47632106199cb7f496ce01 127.0.0.1:30005 slave 67ed2db8d677e59ec4a4cefb06858cf2a1a89fa1 0 1426238316232 5 connected
824fe116063bc5fcf9f4ffd895bc17aee7731ac3 127.0.0.1:30006 slave 292f8b365bb7edb5e285caf0b7e6ddc7265d2f4f 0 1426238317741 6 connected
e7d1eecce10fd6bb5eb35b9f99a514335d9ba9ca 127.0.0.1:30001 myself,master - 0 0 1 connected 0-5460"""
     return str

app.run(host='0.0.0.0', port=6969, debug=False)
