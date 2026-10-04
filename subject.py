import random


class Subject:
    def __init__(self, subjectID: str = None, mark: int = None):
        if subjectID is None:
            self._subjectID = self.generateSubjectID()
        else:
            self._subjectID = subjectID

        if mark is None:
            self._mark = self.generateRandomMark()
        else:
            self._mark = mark

        self._grade = self.calculateGrade(self._mark)

    def generateSubjectID(self) -> str:
        return f"{random.randint(1, 999):03d}"

    def generateRandomMark(self) -> int:
        return random.randint(0, 100)

    def calculateGrade(self, mark: int) -> str:
        if mark >= 85:
            return "HD"
        elif mark >= 75:
            return "D"
        elif mark >= 65:
            return "C"
        elif mark >= 50:
            return "P"
        elif mark < 50:
            return "Z"

    def getSubjectID(self) -> str:
        return self._subjectID

    def getMark(self) -> int:
        return self._mark

    def getGrade(self) -> str:
        return self._grade

    def __str__(self) -> str:
        return f"Subject ID: {self._subjectID} -- Mark = {self._mark} -- Grade = {self._grade}"
