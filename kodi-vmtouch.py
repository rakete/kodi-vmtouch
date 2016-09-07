import requests
import json


def main():
    url = "http://skynet:8080/jsonrpc"
    headers = {'content-type': 'application/json'}

    # Example echo method
    payload = {
        "method": "JSONRPC.Ping",
        "jsonrpc": "2.0",
        "id": 0,
    }
    response = requests.post(
        url, data=json.dumps(payload), headers=headers).json()

    print response
    assert response["result"] == "pong"

if __name__ == "__main__":
    main()
