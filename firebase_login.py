import requests

_verify_password_url = 'https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword'

api_key = "AIzaSyBCFDRnroUEK_pPWYziYUEgqRuRB_iu5OU"

def sign_in_with_password(email, password):
    body = {'email': email, 'password': password}
    params = {'key': api_key}
    try:
        resp = requests.request('post', _verify_password_url, params=params, json=body)
        resp.raise_for_status()
        return True
    except:
        return False