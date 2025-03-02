import numpy as np

from Abiturient import abiturient

if __name__ == '__main__':
    print('Hello world')
    studentOne = abiturient()
    studentTwo = abiturient()
    studentThree = abiturient()
    studentFour = abiturient()
    meanGrades = int(input("Введите среднюю оценко по которой смотреть (от 1 до 10)"))

    listStudents = [studentOne, studentTwo, studentThree, studentFour]
    for student in listStudents:
        for grade in student.grades:
            if grade<4:
                print(f'{student.name} имеет неудовлетворительную оценку {student.grades}')
    for student in listStudents:
        if np.mean(student.grades)>meanGrades:
            print(f"{student.name} имеет среднюю оценку {np.mean(student.grades)}")
