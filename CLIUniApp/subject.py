import random


class Subject:
    def __init__(
        self, subjectID: str = None, mark: int = None, existingIDs: set = None
    ):
        self._subjectID = (
            subjectID if subjectID else self.generateSubjectID(existingIDs or set())
        )
        self._mark = mark if mark is not None else random.randint(25, 100)
        self._grade = self.calculateGrade(self._mark)

    def generateSubjectID(self, existingIDs=None) -> str:
        existingIDs = existingIDs or set()
        while True:
            subjectID = f"{random.randint(1, 999):03d}"

            if subjectID not in existingIDs:
                existingIDs.add(subjectID)
                return subjectID

    def calculateGrade(self, mark: int) -> str:
        if mark >= 85:
            return "HD"
        elif mark >= 75:
            return "D"
        elif mark >= 65:
            return "C"
        elif mark >= 50:
            return "P"
        else:
            return "Z"

    def getSubjectID(self) -> str:
        return self._subjectID

    def getMark(self) -> int:
        return self._mark

    def getGrade(self) -> str:
        return self._grade

    def __str__(self) -> str:
        return f"[ Subject::{self._subjectID} -- mark = {self._mark} -- grade = {self._grade:>2} ]"
