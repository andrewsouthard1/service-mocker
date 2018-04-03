import json

def mock_mesos_slv():
	with open('mocks/fixtures/state.json') as json_data:
		data = json.load(json_data)
		json_data.close()

	return json.dumps(data)

def state():
        with open('mocks/fixtures/state.json') as json_data:
                data = json.load(json_data)
                json_data.close()

        return json.dumps(data)

def stats():
	with open('mocks/fixtures/stats.json') as json_data:
                data = json.load(json_data)
                json_data.close()

        return json.dumps(data)
