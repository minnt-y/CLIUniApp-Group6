import sys
import os

cli_dir = os.path.dirname(os.path.abspath(__file__))
if cli_dir not in sys.path:
    sys.path.append(cli_dir)

from student import Student
from subject import Subject
from studentBase import StudentBase
import random


class StudentManager:
    def __init__(self):
        self.students = StudentBase.loadStudentData()

        self._existing_studentIDs = set()
        self._existing_subjectIDs = set()

        for student in self.students:
            self._existing_studentIDs.add(student.getStudentID())
            for sub in student.viewEnrolmentList():
                self._existing_subjectIDs.add(sub.getSubjectID())

    def saveData(self) -> None:
        StudentBase.saveStudentData(self.students)

    def validateEmail(self, email: str) -> bool:
        if not email or not email.endswith("@university.com"):
            return False
        return True

    def validatePassword(self, password: str) -> bool:
        if not password:
            return False

        if not password[0].isupper():
            return False

        letter_count = sum(1 for c in password if c.isalpha())
        if letter_count < 5:
            return False

        import re

        match = re.search(r"(\d+)$", password)
        if not match or len(match.group(1)) < 3:
            return False

        return True

    def registerStudent(self, name: str, email: str, password: str):
        if not self.validateEmail(email):
            return False

        if not self.validatePassword(password):
            return False

        for student in self.students:
            if student.getEmail() == email:
                return False

        student = Student(
            name=name,
            email=email,
            password=password,
            existingIDs=self._existing_studentIDs,
        )
        self._existing_studentIDs.add(student.getStudentID())

        self.students.append(student)
        self.saveData()

        return student

    def loginStudent(self, studentID: str, password: str):
        for student in self.students:
            if (
                student.getStudentID() == studentID
                and student.getPassword() == password
            ):
                return student

        return None

    def changePassword(self, studentID: str, newPassword: str) -> bool:
        if not self.validatePassword(newPassword):
            return False

        for student in self.students:
            if student.getStudentID() == studentID:
                student.setPassword(newPassword)
                self.saveData()
                return True

        return False

    def enrolSubject(self, studentID: str):
        for student in self.students:
            if student.getStudentID() == studentID:
                if len(student.viewEnrolmentList()) >= 4:
                    return False

                subject = Subject(existingIDs=self._existing_subjectIDs)
                self._existing_subjectIDs.add(subject.getSubjectID())

                student.enrolSubject(subject)
                self.saveData()

                return subject

        return False

    def removeSubject(self, studentID: str, subjectID: str) -> bool:
        for student in self.students:
            if student.getStudentID() == studentID:
                result = student.removeSubject(subjectID)

                if result:
                    self.saveData()

                return result

        return False

    def viewEnrolmentList(self, studentID: str):
        for student in self.students:
            if student.getStudentID() == studentID:
                return student.viewEnrolmentList()

        return []

    def getAllStudents(self) -> list:
        return self.students.copy()

    def getStudentsByGrade(self) -> dict:
        grades = {"HD": [], "D": [], "C": [], "P": [], "Z": []}

        for student in self.students:
            avg_mark = student.getAverageMark()
            if isinstance(avg_mark, str):
                continue

            if avg_mark >= 85:
                grade = "HD"
            elif avg_mark >= 75:
                grade = "D"
            elif avg_mark >= 65:
                grade = "C"
            elif avg_mark >= 50:
                grade = "P"
            else:
                grade = "Z"

            grades[grade].append((student, avg_mark))

        return grades

    def categorizePassFail(self) -> dict:
        result = {"PASS": [], "FAIL": []}

        for student in self.students:
            enrolled = student.viewEnrolmentList()
            if not enrolled:
                continue

            avg_mark = student.getAverageMark()
            if isinstance(avg_mark, str):
                continue

            if avg_mark >= 50:
                if student not in result["PASS"]:
                    result["PASS"].append(student)
            else:
                if student not in result["FAIL"]:
                    result["FAIL"].append(student)

        return result

    def removeStudent(self, studentID: str) -> bool:
        for student in self.students:
            if student.getStudentID() == studentID:
                self.students.remove(student)
                self._existing_studentIDs.discard(studentID)
                self.saveData()
                return True

        return False

    def clearAllStudents(self) -> None:
        self.students.clear()
        self._existing_studentIDs.clear()
        self._existing_subjectIDs.clear()
        self.saveData()
