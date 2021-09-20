class HttpRequest:

    def __init__(self, status_code: int, body: any):
        self.status_code = status_code
        self.body = body


class HttpResponse:

    def __init__(self, status_code: int, body: any = None):
        self.status_code = status_code
        self.body = body
