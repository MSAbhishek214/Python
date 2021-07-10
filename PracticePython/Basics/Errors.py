class MyError(TypeError):
    def __init__(self, message, code):
        super().__init__(f'Error code {code}: {message}')
        self.code = code


raise MyError('Something went wrong!', 500)