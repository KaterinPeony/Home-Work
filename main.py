
class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
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

    def get_average_grade(self):
        grades_sum = 0
        grades_count = 0
        for grades_list in self.grades.values():
            grades_sum += sum(grades_list)
            grades_count += len(grades_list)
        if grades_count == 0:
            return 'Ошибка'
        average_grade = grades_sum / grades_count
        return round(average_grade, 1)

    def __str__(self):
        sep = ', '
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.get_average_grade()}\nКурсы в процессе изучения: {sep.join(self.courses_in_progress)}\nЗавершенные курсы: {sep.join(self.finished_courses)}'

    def __gt__(self, other):
        return first_student.get_average_grade() > other.get_average_grade()

    def __eq__(self, other):
        return first_student.get_average_grade() == other.get_average_grade()

    def __lt__(self, other):
        return first_student.get_average_grade() < other.get_average_grade()

    def __le__(self, other):
        return first_student.get_average_grade() <= other.get_average_grade()

    def __ge__(self, other):
        return first_student.get_average_grade() >= other.get_average_grade()

    def __ne__(self, other):
        return first_student.get_average_grade() != other.get_average_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Reviewer(Mentor):
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

    def get_average_grade(self):
        grades_sum = 0
        grades_count = 0
        for grades_list in self.grades.values():
            grades_sum += sum(grades_list)
            grades_count += len(grades_list)
        if grades_count == 0:
            return 'Ошибка'
        average_grade = grades_sum / grades_count
        return round(average_grade, 1)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.get_average_grade()}'

    def __gt__(self, other):
        return first_lecturer.get_average_grade() > other.get_average_grade()

    def __eq__(self, other):
        return first_lecturer.get_average_grade() == other.get_average_grade()

    def __lt__(self, other):
        return first_lecturer.get_average_grade() < other.get_average_grade()

    def __le__(self, other):
        return first_lecturer.get_average_grade() <= other.get_average_grade()

    def __ge__(self, other):
        return first_lecturer.get_average_grade() >= other.get_average_grade()

    def __ne__(self, other):
        return first_lecturer.get_average_grade() != other.get_average_grade()


first_lecturer = Lecturer('Никита', 'Андреев')
first_lecturer.courses_attached += ['Python', 'Java']

second_lecturer = Lecturer('Олег', 'Иванов')
second_lecturer.courses_attached += ['Java', 'C#']

first_student = Student('Роман', 'Авдеев')
first_student.courses_in_progress += ['Python', 'Java']
first_student.finished_courses += ['SQL', 'Git']

first_student.rate_lec_hw(first_lecturer, 'Python', 10)
first_student.rate_lec_hw(first_lecturer, 'Python', 7)
first_student.rate_lec_hw(first_lecturer, 'Java', 9)
first_student.rate_lec_hw(first_lecturer, 'Java', 6)

second_student = Student('Мария', 'Боева')
second_student.courses_in_progress += ['Java', 'C#']
second_student.finished_courses += ['React', 'Git']

second_student.rate_lec_hw(second_lecturer, 'Java', 8)
second_student.rate_lec_hw(second_lecturer, 'Java', 10)
second_student.rate_lec_hw(second_lecturer, 'C#', 7)
second_student.rate_lec_hw(second_lecturer, 'C#', 8)

first_reviewer = Reviewer('Антон', 'Васильев')
first_reviewer.courses_attached += ['Python', 'Java']

first_reviewer.rate_hw(first_student, 'Python', 8)
first_reviewer.rate_hw(first_student, 'Python', 10)
first_reviewer.rate_hw(first_student, 'Python', 10)
first_reviewer.rate_hw(first_student, 'Java', 9)
first_reviewer.rate_hw(first_student, 'Java', 10)
first_reviewer.rate_hw(first_student, 'Java', 9)

second_reviewer = Reviewer('Владимир', 'Афанасьев')
second_reviewer.courses_attached += ['Java']

second_reviewer.rate_hw(second_student, 'Java', 10)
second_reviewer.rate_hw(second_student, 'Java', 7)
second_reviewer.rate_hw(second_student, 'Java', 9)


print('Задание 2')
print('Оценки за лекции:')
print(first_lecturer.grades)
print()
print(second_lecturer.grades)
print()
print('Оценки студентов:')
print(first_student.grades)
print()
print(second_student.grades)
print()


print('Задание 3')
print('Информация о лекторах:')
print(first_lecturer)
print()
print(second_lecturer)
print()
print('Информация о проверяющих:')
print(first_reviewer)
print()
print(second_reviewer)
print()
print('Информация о студентах:')
print(first_student)
print()
print(second_student)
print()
print(first_student > second_student)
print(first_student < second_student)
print(first_student >= second_student)
print(first_student <= second_student)
print(first_student == second_student)
print(first_student != second_student)
print()
print(first_lecturer > second_lecturer)
print(first_lecturer < second_lecturer)
print(first_lecturer >= second_lecturer)
print(first_lecturer <= second_lecturer)
print(first_lecturer == second_lecturer)
print(first_lecturer != second_lecturer)
print()
print('Задание 4')
lecturer_list = [first_lecturer, second_lecturer]
students_list = [first_student, second_student]
course = ['Java']


def get_avg_grade_course(people, course):
    if not isinstance(people, list):
        return 'Списка нет'
    grades_list = []
    for person in people:
        grades_list.extend(person.grades.get(course))
    if not grades_list:
        return 'По такому курсу ни у кого нет оценок'
    return course, str(round(sum(grades_list) / len(grades_list), 2))


print(f"У студентов cредняя оценка за курс {get_avg_grade_course(students_list,'Java')}")
print(f"У лекторов cредняя оценка за курс {get_avg_grade_course(lecturer_list,'Java')}")





















