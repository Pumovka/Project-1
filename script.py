from array import array
import string


class Student:
    def __init__(self, name, last_name, year, number_course, number_group, marks, srmarks ):
        self.name  = name
        self.last_name = last_name
        self.year = year 
        self.number_course = number_course 
        self.number_group = number_group 
        self.marks = marks
        self.srmarks = srmarks
       #print(name, last_name, year, number_course, number_group, marks)
    pass
    def printStudent(self):
        print(self.name, self.last_name, self.year, self.number_course, self.number_group, self.marks)
    pass
  
student1 = Student("Василий", "Васильев", 1995, 3, "ВПИ-20", [4,3,5,5,3], '')
student2 = Student("Иван", "Иванов", 1998, 1, "ВПИ-21", [4,5,5,5,5], '')
student3 = Student("Петр", "Петров", 1994, 3, "ВПИ-20", [4,3,5,4,4], '')
student4 = Student("Егоров", "Егор", 1999, 1, "ВПИ-21", [3,3,3,5,3], '')
student5 = Student("Максимов", "Максим", 1997, 1, "ВПИ-21", [4,4,5,5,3], '')

list = [student1,student2,student3,student4,student5] 

def SortCourse(list):#Сортировка по курсу
    for i in range(len(list)):
        for j in range(0, len(list)-i-1):
            if list[j].number_course > list[j+1].number_course:
                list[j], list[j+1] = list[j+1], list[j]
    pass

SortCourse(list)

print("1. Упорядочить студентов по курсу (без учета алфавитного порядка)")

def printList(list):
    for i in range(len(list)):
        list[i].printStudent()
    pass

printList(list)

def SortAge(list): #Сортировка по году рождения
        for i in range(len(list)):
            for j in range(0, len(list)-i-1):
                if list[j].year > list[j+1].year:
                    list[j], list[j+1] = list[j+1], list[j]
pass

SortAge(list)
print("3. Найти самого старшего и самого младшего")
print("Самый старший:", list[0].name , list[0].last_name , list[0].year)
print("Самый младший:", list[len(list)-1].name , list[len(list)-1].last_name , list[len(list)-1].year)
listmark = []
def SortMarks(list):
    mark = 0 #Найти средний балл для каждого студента
    for i in range(5):
        for j in range(5):
            # print(list[i].marks[j]) 
            mark = mark + list[i].marks[j]
        mark = mark/5
        list[i].srmark = mark
        mark = 0 
    # for i in range(5):
    #     maxmark = 0 
    #     print(list[i].srmark)
    #     if maxmark < list[i].srmark:
    #         maxmark = list[i].srmark
    for i in range(len(list)):
            for j in range(0, len(list)-i-1):
                if list[j].srmark > list[j+1].srmark:
                    list[j], list[j+1] = list[j+1], list[j]
    print("Cамый большой средний балл:", list[len(list)-1].srmark, list[len(list)-1].name)
    pass

SortMarks(list)
# def Gpa(list):
#     for i in range(len(list)):
#         if list[i].number_group == list[i+1].number_group:
# pass