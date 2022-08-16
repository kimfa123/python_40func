import requests
import json

slack_webhook_url = "https://hooks.slack.com/services/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"

def sendSlackWebhook(strText):
    headers = {
        "Content-type" : "application/json"
    }

    data = {
        "text" : strText
    }

    res = requests.post(slack_webhook_url, headers=headers, data=json.dumps(data))

    if res.status_code == 200:
        return "ok"
    else : 
        return "error"

print(sendSlackWebhook("지훈아 공부하자 돈벌자 ~!! "))