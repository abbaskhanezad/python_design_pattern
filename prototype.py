from abc import ABC, abstractmethod
import copy
class Courses(ABC):
    def __init__(self):
        self.id=None
        self.type=None
        self.user=None
    
    @abstractmethod
    def course(self):
            pass
    
    def get_type(self):
        return self.type

    def get_id(self):
        return self.id

    def set_id(self, sid):
        self.id = sid

    def clone(self):
            return copy.copy(self)
    def set_user(self,user):
        self.user=user
    def show_details(self):
        print("{} {} {}".format(self.id,self.type,self.user))
 
class Python(Courses):
    def __init__(self):
        super().__init__()
        self.type="python"
    
    def course(self):
        return "python"
class Php(Courses):
    def __init__(self):
        super().__init__()
        self.type="php"
    
    def course(self):
        return "php"

class MyCourses:
    
    repo={}
    
    @staticmethod
    def get_course(id):
        if id in MyCourses.repo:
            course= MyCourses.repo[id]
            return course.clone()
        else:
            return None
    
    @staticmethod
    def start():
        python=Python()
        python.set_id("1")
        php=Php()
        php.set_id("2")
        MyCourses.repo[python.get_id()]=python
        MyCourses.repo[php.get_id()]=php
if "__main__" == __name__:
    user_list=['abbas','john','wendy','mary','fred']
    MyCourses.start()
    for user in user_list:
        course=MyCourses.get_course("1")
        course.set_user(user)
        print(course.show_details())
        course=MyCourses.get_course("2")
        course.set_user(user)
        print(course.show_details())