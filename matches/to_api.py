import requests


def api_response(host_loc, gust_loc):
    url = "https://ofir-distance-api.xwildeyes.now.sh/distance"
    pay = "{\n\t\"from\": \","+str(gust_loc)+"\",\n\t\"to\": \""+str(host_loc)+"\"\n}"
    payload = pay.encode('utf-8')
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.reason
    # print(response.text.encode('utf8'))
