class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached \
                and course in self.courses_in_progress and 0 < grade < 11:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def aver_grade_hw(self):
        sum_gr = 0
        count_gr = 0
        for grade in self.grades.values():
            sum_gr += sum(grade)
            count_gr += len(grade)
        return round(sum_gr / count_gr, 1)

    def __str__(self):
        res = f'Имя: {self.name} \n' \
              f'Фамилия: {self.surname} \n' \
              f'Средняя оценка за домашние задания: {self.aver_grade_hw()} \n' \
              f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)} \n" \
              f"Завершенные курсы: {', '.join(self.finished_courses)} \n"
        return res

    def __lt__(self, other_student):
        if not isinstance(other_student, Student):
            print(f' {other_student} отсутствует в списке студентов')
            return
        else:
            if self.aver_grade_hw() < other_student.aver_grade_hw():
                print(f'{self.name} {self.surname} (ср.оценка: {self.aver_grade_hw()}) учится хуже, '
                      f'чем {other_student.name} {other_student.surname} (ср.оценка: {other_student.aver_grade_hw()})')
            else:
                print(f'{self.name} {self.surname} (ср.оценка: {self.aver_grade_hw()}) учится лучше, '
                      f'чем {other_student.name} {other_student.surname} (ср.оценка: {other_student.aver_grade_hw()})')


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []



class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def aver_grade_lec(self):
        sum_gr = 0
        count_gr = 0
        for grade in self.grades.values():
            sum_gr += sum(grade)
            count_gr += len(grade)
        return round(sum_gr/count_gr, 1)

    def __str__(self):
        res = f'Имя: {self.name} \n' \
              f'Фамилия: {self.surname} \n' \
              f'Средняя оценка за лекции: {self.aver_grade_lec()} \n'
        return res

    def __lt__(self, other_lecturer):
        if not isinstance(other_lecturer, Lecturer):
            print(f' {other_lecturer} отсутствует в списке лекторов')
            return
        else:
            if self.aver_grade_lec() < other_lecturer.aver_grade_lec():
                print(f'{self.name} {self.surname} (ср.оценка: {self.aver_grade_lec()}) хуже, чем '
                      f'{other_lecturer.name} {other_lecturer.surname} (ср.оценка: {other_lecturer.aver_grade_lec()})')
            else:
                print(f'{self.name} {self.surname} (ср.оценка: {self.aver_grade_lec()}) лучше, чем '
                      f'{other_lecturer.name} {other_lecturer.surname} (ср.оценка: {other_lecturer.aver_grade_lec()})')

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached \
                and course in student.courses_in_progress and 0 < grade < 11:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} \n' \
              f'Фамилия: {self.surname} \n'
        return res


best_student = Student('Оля', 'Иванова', 'Ж')
best_student.finished_courses += ['Git']
best_student.courses_in_progress += ['Python', 'Java']
best_student.grades['Java'] = [10, 9, 8, 10]
best_student.grades['Python'] = [8, 10, 9, 10]

bad_student = Student('Коля', 'Иваньков', 'М')
bad_student.finished_courses += ['Git']
bad_student.courses_in_progress += ['Python', 'Java']
bad_student.grades['Java'] = [5, 9, 8, 10]
bad_student.grades['Python'] = [7, 7, 9, 10]



first_reviwer = Reviewer('Маша', 'Сидоренко')
first_reviwer.courses_attached += ['Python']
first_reviwer.courses_attached += ['Java']

second_reviwer = Reviewer('Павел', 'Невольный')
second_reviwer.courses_attached += ['Python']
second_reviwer.courses_attached += ['Java']

first_reviwer.rate_hw(best_student, 'Python', 7)
first_reviwer.rate_hw(best_student, 'Java', 7)
first_reviwer.rate_hw(bad_student, 'Python', 7)
first_reviwer.rate_hw(bad_student, 'Java', 7)

second_reviwer.rate_hw(best_student, 'Python', 8)
second_reviwer.rate_hw(best_student, 'Java', 8)
second_reviwer.rate_hw(bad_student, 'Python', 8)
second_reviwer.rate_hw(bad_student, 'Java', 8)



best_lecturer = Lecturer('Владимир', 'Всехвалов')
best_lecturer.courses_attached += ['Python']
best_lecturer.courses_attached += ['Java']

bad_lecturer = Lecturer('Михаил', 'Ленивцев')
bad_lecturer.courses_attached += ['Python']
bad_lecturer.courses_attached += ['Java']

best_student.rate_lecture(best_lecturer, 'Python', 10)
best_student.rate_lecture(best_lecturer, 'Java', 9)
best_student.rate_lecture(bad_lecturer, 'Python', 7)
best_student.rate_lecture(bad_lecturer, 'Java', 6)

bad_student.rate_lecture(best_lecturer, 'Python', 9)
bad_student.rate_lecture(best_lecturer,  'Java', 9)
bad_student.rate_lecture(bad_lecturer, 'Python', 6)
bad_student.rate_lecture(bad_lecturer,  'Java', 6)



print(best_student)
print(best_student.grades)
print()
print(bad_student)
print(bad_student.grades)
print()
print(best_student > bad_student)

print(first_reviwer)
print(second_reviwer)

print(best_lecturer)
print(best_lecturer.grades)
print()
print(bad_lecturer)
print(bad_lecturer.grades)
print()
print(best_lecturer > bad_lecturer)



def aver_gr_stud_hw(student_list, course):
    sum_gr = 0
    for student in student_list:
        for courses, grades in student.grades.items():
            if courses == course:
                sum_gr += sum(grades) / len(grades)
    return print(f' Средняя оценка студентов по курсу {course}: {sum_gr / len(student_list) :.1f}')


def aver_gr_lec(lecturers_list, course):
    sum_gr = 0
    for lecturer in lecturers_list:
        for courses, grades in lecturer.grades.items():
            if courses == course:
                sum_gr += sum(grades) / len(grades)
    return print(f' Средняя оценка лекторов по курсу {course}: {sum_gr / len(lecturers_list) :.1f}')

aver_gr_stud_hw([best_student, bad_student], 'Java')

aver_gr_stud_hw([best_student, bad_student], 'Python')

aver_gr_lec([best_lecturer, bad_lecturer], 'Java')

aver_gr_lec([best_lecturer, bad_lecturer], 'Python')