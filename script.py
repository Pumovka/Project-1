from array import array
import string


class Student:
    def SetStudent(self, name, last_name, year, number_course, number_group, marks ):
        self.name  = name
        self.last_name = last_name
        self.year = year 
        self.number_course = number_course 
        self.number_group = number_group 
        self.marks = marks
        print(name, last_name, year, number_course, number_group, marks)
    pass
    def printStudent(self):
        print(self.name, self.last_name, self.year, self.number_course, self.number_group, self.marks)
    pass
  
student1 = Student()
student2 = Student()
student3 = Student()
student4 = Student()
student5 = Student()

student1.SetStudent("Василий", "Васильев", 1995, 3, "ВПИ-20", [4,3,5,5,3])
student2.SetStudent("Иван", "Иванов", 1998, 1, "ВПИ-21", [4,5,5,5,5])
student3.SetStudent("Петр", "Петров", 1994, 3, "ВПИ-20", [4,3,5,4,4])
student4.SetStudent("Егоров", "Егор", 1999, 1, "ВПИ-21", [3,3,3,5,3])
student5.SetStudent("Максимов", "Максим", 1997, 1, "ВПИ-21", [4,4,5,5,3])

list = [student1,student2,student3,student4,student5]


def SortCourse(list):#Сортировка по году рождения
    i = 0
    for i in range(len(list)):
        for j in range(0, len(list)-i-1):
            if list[j].number_course > list[j+1].number_course:
                list[j], list[j+1] = list[j+1], list[j]
pass

SortCourse(list)

print("1. Упорядочить студентов по курсу (без учета алфавитного порядка)")

def printList(list):
    i=0
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
