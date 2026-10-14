from student import Student, usedStudentIDs
from subject import Subject, usedSubjectIDs
from studentBase import StudentBase
import random


class StudentManager:
    def __init__(self):
        self.students = StudentBase.loadStudentData()
        for student in self.students:
            usedStudentIDs.add(student.getStudentID())
            for sub in student.viewEnrolmentList():
                usedSubjectIDs.add(sub.getSubjectID())

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

        # Create new student
        student = Student(name, email, password)
        self.students.append(student)
        self.saveData()

        return student

    def loginStudent(self, studentID: str, password: str):
        for student in self.students:
            if student.getStudentID() == studentID and student._password == password:
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

                subject = Subject()

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

            avg_mark = student.getAverageMark()

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
                usedStudentIDs.discard(studentID)
                self.saveData()
                return True

        return False

    def clearAllStudents(self) -> None:
        self.students.clear()
        usedStudentIDs.clear()
        self.saveData()
