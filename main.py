

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lec_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course not in lecturer.grades:
                lecturer.grades[course] = []
            lecturer.grades[course] += [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        grades_sum = 0
        grades_count = 0
        for grades_list in self.grades.values():
            grades_sum += sum(grades_list)
            grades_count += len(grades_list)
        if grades_count == 0:
            return 'Ошибка'
        average_grade = grades_sum / grades_count
        sep = ', '
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {round(average_grade, 1)}\nКурсы в процессе изучения: {sep.join(self.courses_in_progress)}\nЗавершенные курсы: {sep.join(self.finished_courses)}'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        grades_sum = 0
        grades_count = 0
        for grades_list in self.grades.values():
            grades_sum += sum(grades_list)
            grades_count += len(grades_list)
        if grades_count == 0:
            return 'Ошибка'
        average_grade = grades_sum / grades_count
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {round(average_grade, 1)}'

#def task_3():
#    reviewer = Reviewer('Vasya', 'Petrov')
#    print(reviewer)


#task_3()

#reviewer = Reviewer('Vasya', 'Petrov')
lecturer = Lecturer('James', 'Gray')
lecturer.courses_attached += ['Python', 'Java']
#print(lecturer)




#print(best_student.grades)

student = Student('Ruoy', 'Eman', 'male_gender')
student.courses_in_progress += ['Python', 'Java']

student.rate_lec_hw(lecturer, 'Python', 10)
student.rate_lec_hw(lecturer, 'Python', 8)
student.rate_lec_hw(lecturer, 'Java', 9)
student.rate_lec_hw(lecturer, 'Java', 10)

print(lecturer.grades)


print('Задача 3')
reviewer = Reviewer('Vasya', 'Petrov')
print(reviewer)
print()
print(lecturer)
print()

best_student = Student('Ruoy', 'Eman', 'male_gender')
best_student.courses_in_progress += ['Python', 'C++']
best_student.finished_courses += ['Java']

reviewer = Reviewer('Some', 'Buddy')
reviewer.courses_attached += ['Python']

reviewer.rate_hw(best_student, 'Python', 10)
reviewer.rate_hw(best_student, 'Python', 10)
reviewer.rate_hw(best_student, 'Python', 10)

print(best_student)









# S PyCharm help at https://www.jetbrains.com/help/pycharm/
