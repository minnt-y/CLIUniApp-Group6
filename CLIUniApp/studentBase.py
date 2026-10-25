import os
import pickle


class StudentBase:
    FILE_NAME = "students.data"

    @staticmethod
    def saveStudentData(students: list) -> None:
        with open(StudentBase.FILE_NAME, "wb") as file:
            pickle.dump(students, file)

    @staticmethod
    def loadStudentData() -> list:
        try:
            with open(StudentBase.FILE_NAME, "rb") as file:
                if os.path.getsize(StudentBase.FILE_NAME) == 0:
                    return []
                return pickle.load(file)

        except FileNotFoundError:
            return []
        except EOFError:
            return []
        except pickle.UnpicklingError:
            return []
