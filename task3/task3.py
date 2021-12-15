import json
from abc import abstractmethod, ABC


class ICourse(ABC):
    @property
    @abstractmethod
    def name(self):
        pass

    @name.setter
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def teacher(self):
        pass

    @teacher.setter
    @abstractmethod
    def teacher(self, value):
        pass

    @property
    @abstractmethod
    def programm(self):
        pass

    @programm.setter
    @abstractmethod
    def programm(self, value):
        pass

    @abstractmethod
    def create_course(self):
        pass


    def __str__(self):
        pass


class Course(ICourse):
    def __init__(self, name, programm, teacher):
        self.name = name
        self.teacher = teacher
        self.programm = programm

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not value:
            raise TypeError("Name must be a string!")
        self.__name = value

    @property
    def teacher(self):
        return self.__teacher

    @teacher.setter
    def teacher(self, value):
        if not isinstance(value, Teacher):
            raise TypeError("Teacher must be a Teacher object!")
        self.__teacher = value

    @property
    def programm(self):
        return self.__programm

    @programm.setter
    def programm(self, value):
        if not isinstance(value, list):
            raise TypeError("Programm must be a list!")
        self.__programm = value

    def create_course(self):
        course = {'name': self.name, 'programm': self.programm}
        if isinstance(self, LocalCourse):
            course['type_of_courses'] = "Local"
            course['lab'] = self.lab
        if isinstance(self, OffsiteCourse):
            course['type_of_courses'] = "Offsite"
            course['location'] = self.location
        course['teacher'] = self.teacher.name
        with open('course.json', 'r') as file:
            courses = json.load(file)
        courses.append(course)
        with open('course.json', 'w') as file:
            json.dump(courses, file, indent=4)
        return course


    def __str__(self):
        return f"\n\nCourse:\nName of course: {self.name}\nTeacher: {self.teacher.name}\nProgram: " \
               f"{', '.join(map(str, (x for x in self.programm)))}"




class ILocalCourse(ABC):
    @property
    @abstractmethod
    def lab(self):
        pass

    @lab.setter
    @abstractmethod
    def lab(self, value):
        pass


class LocalCourse(Course, ILocalCourse):
    def __init__(self, name, program, teacher, lab):
        super().__init__(name, program, teacher)
        self.lab = lab
        self.create_course()

    @property
    def lab(self):
        return self.__lab

    @lab.setter
    def lab(self, value):
        if not isinstance(value, str):
            raise TypeError("Lab must be string!")
        self.__lab = value

    def __str__(self):
        return f"\n\nCourse:\nName of course: {self.name}\nTeacher: {self.teacher.name}\nProgram: " \
               f"{', '.join(map(str, (x for x in self.programm)))}\nLab: {self.lab}"


class IOffsiteCourse(ABC):
    @property
    @abstractmethod
    def location(self):
        pass

    @location.setter
    @abstractmethod
    def location(self, value):
        pass


class OffsiteCourse(Course, IOffsiteCourse):
    def __init__(self, name, program, teacher, location):
        super().__init__(name, program, teacher)
        self.location = location
        self.create_course()

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, value):
        if not isinstance(value, str):
            raise TypeError("Location must be str type")
        self.__location = value

    def __str__(self):
        return f"\n\nCourse:\nName of course: {self.name}\nTeacher: {self.teacher.name}\nProgram: " \
               f"{', '.join(map(str, (x for x in self.programm)))}\nLocation: {self.location}"


class ITeacher(ABC):
    @property
    @abstractmethod
    def name(self):
        pass

    @name.setter
    @abstractmethod
    def name(self, value):
        pass

    @abstractmethod
    def teacher_course(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class Teacher(ITeacher):
    def __init__(self, name):
        self.name = name
        self.teacher_course()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not value:
            raise TypeError("Name must be a string!")
        self.__name = value

    def teacher_course(self):
        with open("teacher.json", 'r') as file:
            teacher_courses = json.load(file)
        with open("course.json", 'r') as f:
            courses = json.load(f)
        info_about_teacher = {self.name: []}
        for course in courses:
            if course["teacher"] == self.name:
                teacher_course_info = {"name": course["name"], "programm": course["programm"],
                                       "type_of_courses": course["type_of_courses"]}
                try:
                    teacher_course_info["location"] = course["location"]
                except:
                    teacher_course_info["lab"] = course["lab"]
            info_about_teacher[self.name].append(teacher_course_info)
            teacher_courses.append(info_about_teacher)
        with open("teacher.json", 'w') as file:
            json.dump(teacher_courses, file, indent=4)



    def get_info(self):
        with open("teacher.json", 'r') as file:
            courses = json.load(file)
        list_of_courses = [course[self.name] for course in courses if course[self.name]]
        return list_of_courses

    def __str__(self):
        return f"\n\nTeacher:\nName = {self.name}\nCourses : " \
               f"{', '.join(map(str, (i['name'] for course in self.get_info() for i in course)))}"


class ICourseFactory(ABC):
    @staticmethod
    @abstractmethod
    def adding_teacher():
        pass

    @staticmethod
    @abstractmethod
    def form_local_course():
        pass

    @staticmethod
    @abstractmethod
    def form_offsite_course():
        pass

class CourseFactory:
    @staticmethod
    def adding_teacher(name):
        return Teacher(name)

    @staticmethod
    def form_local_course(name, program, teacher, lab):
        return LocalCourse(name, program, teacher, lab)


def form_offsite_course(name, program, teacher, location):
    return OffsiteCourse(name, program, teacher, location)


course_factory = CourseFactory
teacher = course_factory.adding_teacher("Oleg")
offsite =course_factory.form_offsite_course("Database", ["requests", "database creation", "database normalization"], teacher, "Lviv")
local = course_factory.form_local_course("OOP PYTHON", ["Polymorphism in Python",
                              "Generators in Python",
                              "Multiple Inheritance in Python",
                              "Inheritance in Python"], teacher, "lab#151")
print(local)
print(offsite)