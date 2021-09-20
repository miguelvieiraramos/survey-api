class InvalidParamError(Exception):

    def __init__(self, param_name):
        super().__init__(f'Invalid param: {param_name}')
        self.name = 'InvalidParamError'
