import requests

TOKEN = ""

def set_token(token):
    global TOKEN
    TOKEN = token

def notify(*objects, sep=' ',token=None):
    """
    LINEに通知する
    """
    global TOKEN
    if not token:
        token = TOKEN
    text = sep.join(list(map(lambda x: str(x),objects)))
    line_notify_api = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': f'Bearer {token}'}
    data = {'message': f'message: {text}'}
    requests.post(line_notify_api, headers = headers, data = data)