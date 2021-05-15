from requests import Request, Session, ConnectionError
import json

MAX_RETRY_ATTEMPTS = 5
MAX_TIMEOUT = 5

class HttpClient:
    def __init__(self, api_key):
        self.headers = {
            "x-api-key": api_key,
            "Content-Type": "application/json",
        }
  
    def send(self, request):
        while request.attempt <= MAX_RETRY_ATTEMPTS:
            try:
                session = Session()
                url = f"{request.base_url}{request.path}"
                if bool(request.data):
                    request.data = json.dumps(request.data)
                req = Request(request.method,  url, data=request.data, headers=self.headers)
                prepped = session.prepare_request(req)
                response = session.send(prepped, timeout=MAX_TIMEOUT)
                return response.text
            except ConnectionError as e:
                print(e)

            request.attempt += 1
