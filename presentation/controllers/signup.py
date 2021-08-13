class SignUpController:

    def handle(self, http_request: any) -> any:
        if not http_request['body'].get('name'):
            return {
                'status_code': 400,
                'body': Exception('Missing param: name')
            }

        if not http_request['body'].get('email'):
            return {
                'status_code': 400,
                'body': Exception('Missing param: email')
            }
