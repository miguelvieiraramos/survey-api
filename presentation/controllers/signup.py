from presentation.protocols.http import HttpResponse, HttpRequest


class SignUpController:

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        if not http_request['body'].get('name'):
            return HttpResponse(400, Exception('Missing param: name'))

        if not http_request['body'].get('email'):
            return HttpResponse(400, Exception('Missing param: email'))
