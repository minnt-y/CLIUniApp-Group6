import random


class Student:
    def __init__(
        self,
        name: str = None,
        email: str = None,
        password: str = None,
        studentID: str = None,
    ):
        if studentID is None:
            self._studentID = self.generateStudentID()
        else:
            self._studentID = studentID

        self._name = name
        self._email = email
        self._password = password
        self._enrolledSubjects = []

    def generateStudentID(self) -> str:
        num = random.randint(1, 999999)
        return f"{num:06d}"

    def getStudentID(self) -> str:
        return self._studentID

    def getEmail(self) -> str:
        return self._email

    def setPassword(self, new_password: str) -> None:
        self._password = new_password

    def viewEnrolmentList(self) -> list:
        return self._enrolledSubjects

    def enrolSubject(self, subject) -> bool:
        if len(self._enrolledSubjects) >= 4:
            return False
        else:
            self._enrolledSubjects.append(subject)
            return True

    def removeSubject(self, subjectID: str) -> bool:
        for subject in self._enrolledSubjects:
            if subject.getSubjectID() == subjectID:
                self._enrolledSubjects.remove(subject)
                return True
        return False

    def __str__(self) -> str:
        return f"Name: {self._name} -- Student ID: {self._studentID} -- Email: {self._email}"
