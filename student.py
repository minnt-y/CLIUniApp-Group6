import random

usedStudentIDs = set()


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
        while True:
            num = random.randint(1, 999999)
            studentID = f"{num:06d}"

            if studentID not in usedStudentIDs:
                usedStudentIDs.add(studentID)
                return studentID

    def getName(self) -> str:
        return self._name

    def getStudentID(self) -> str:
        return self._studentID

    def getEmail(self) -> str:
        return self._email

    def setPassword(self, new_password: str) -> None:
        self._password = new_password
    
    def getPassword(self) -> str:
        return self._password

    def viewEnrolmentList(self) -> list:
        return self._enrolledSubjects.copy()

    def enrolSubject(self, subject) -> bool:
        if len(self._enrolledSubjects) >= 4:
            return False

        self._enrolledSubjects.append(subject)
        return True

    def removeSubject(self, subjectID: str) -> bool:
        for subject in self._enrolledSubjects:
            if subject.getSubjectID() == subjectID:
                self._enrolledSubjects.remove(subject)
                return True
        return False

    def getAverageMark(self) -> float:
        enrolled = self.viewEnrolmentList()
        if not enrolled:
            return "No enrolled subjects"
        total_mark = sum(sub.getMark() for sub in enrolled)
        return total_mark / len(enrolled)

    def __str__(self) -> str:
        return f"{self._name} :: {self._studentID} --> Email: {self._email}"
