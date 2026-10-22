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

class EnrolmentExceedLimitException(Exception):
    """Exception that can be thrown when student attempts to enrol more than four courses"""
    def __init__(self, message="Enrolment Error: Exceed the maximum limit of 4 courses."):
        self.message = message
        super().__init__(self.message)
 
class CourseDeletionException(Exception):
    """Exception that can be thrown when student attempts to drop a course improperly"""
    def __init__(self, message="Course Deletion Error: Course does not exist in enrolment."):
        self.message = message
        super().__init__(self.message)