class SignUpController:

    def handle(self, http_request: any) -> any:
        return {
            'status_code': 400,
            'body': Exception('Missing param: name')
        }
