endpoint = 'http://f930af6a-8426-408a-b57e-9b049bce90c4.eastus.azurecontainer.io/score' #Replace with your endpoint
key = 'T2VfPUBb5CXfL14GUJaQdd9DLsKGCjyY' #Replace with your key

import urllib.request
import json
import os

data = {
    "Inputs": {
        "WebServiceInput0":
        [
            {
                    'CulmenLength': 49.1,
                    'CulmenDepth': 4.8,
                    'FlipperLength': 1220,
                    'BodyMass': 5150,
            },
        ],
    },
    "GlobalParameters":  {
    }
}

body = str.encode(json.dumps(data))


headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ key)}

req = urllib.request.Request(endpoint, body, headers)

try:
    response = urllib.request.urlopen(req)
    result = response.read()
    json_result = json.loads(result)
    output = json_result["Results"]["WebServiceOutput0"][0]
    print('Cluster: {}'.format(output["Assignments"]))

except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers to help debug
    print(error.info())
    print(json.loads(error.read().decode("utf8", 'ignore')))