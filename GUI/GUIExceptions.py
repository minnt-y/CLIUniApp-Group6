class EmptyFieldException(Exception):
    """Exception that can be thrown when login field is empty"""
    def __init__(self, message="Email or Password cannot be empty!"):
        self.message = message
        super().__init__(self.message)

class InvalidEmailFormatException(Exception):
    """Exception that can be thrown when email format is not correct"""
    def __init__(self, message="Invalid email format: Must end with @university.com"):
        self.message = message
        super().__init__(self.message)