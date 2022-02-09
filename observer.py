from abc import ABC, abstractmethod
class CourseInterface(ABC):
    @abstractmethod
    def attach(self, observer):
        """
        Attach an observer to the subject.
        """
        pass

    @abstractmethod
    def detach(self, observer):
        """
        Detach an observer from the subject.
        """
        pass

    @abstractmethod
    def notify(self):
        """
        Notify all observers about an event.
        """
        pass

class UserInterface(ABC):
    @abstractmethod
    def update(self, course):
        """
        Receive update from subject.
        """
        pass

class Course(CourseInterface):
    def __init__(self,name,user):
        self.name = name
        self.user = user
        self._observers = []

    def attach(self, observer):
        if  observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self):
        for observer in self._observers:
            observer.update(self)

    def get_name(self):
        return self.name

    def set_user(self,user):
        self.user=user

    def show_details(self):
        print("{} {}".format(self.name,self.user))


class User(UserInterface):
    def __init__(self,name):
        self.name = name

    def update(self, course):
       if course.get_name() == "python":
           print("{} is now following {}".format(self.name, course.get_name()))
       if course.get_name() == "laravel":
               print("{} is now following {}".format(self.name, course.get_name()))

u1=User("abbas")
u2=User("Mary")

py=Course('python','juan')
laravel=Course('laravel','dan')

py.attach(u1)
laravel.attach(u2)
py.attach(u2)

py.notify()
laravel.notify()