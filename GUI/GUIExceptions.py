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
        
class InvalidStudentCredentialsException(Exception):
    """Exception that can be thrown when student credential is not valid"""
    def __init__(self, message="Invalid student credential: Student does not exist."):
        self.message = message
        super().__init__(self.message)