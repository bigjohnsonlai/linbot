import requests


def lineNotifyMessage(token, msg):
    headers = {
        "Authorization": "Bearer " + token, 
        "Content-Type" : "application/x-www-form-urlencoded"
    }

    massage = {'message': msg}
    r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = massage)
    return r.status_code


if __name__ == '__main__':
  message = '[LINE Notify] Hello World'
  token = 'OlUhQv56lAZWRR9WGX7zcKP3AvgFpS4CJwvPr7ZLTlt'

  lineNotifyMessage(token, message)
