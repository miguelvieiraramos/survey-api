class ServerError(Exception):

    def __init__(self):
        super().__init__(f'Internal server error')
        self.name = 'ServerError'
