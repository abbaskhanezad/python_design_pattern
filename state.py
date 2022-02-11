from abc import ABC, abstractmethod
class Task:

    def __init__(self,title,desc):
        self.title = title
        self.desc = desc
        self.current = New
        self.flow = []
    
    def change_status(self,to_status):
        if to_status in self.current.allowed:
            self.to_state = to_status
            self.flow.append(to_status)
            print(f'Successfully moved from {self.current} to {to_status}')
        else:
            print(f'Not Allow move direct from {self.current} to {to_status}')
   
    @property
    def current_status(self):
        return self.flow[-1]        
   
    def get_flow(self):
        return self.flow
    
    def __str__(self):
        return self.title + " " + self.desc
    
class BoardColumn(ABC):

    @property
    @abstractmethod
    def allowed(self):
        pass

class Done(BoardColumn):
    allowed = []

class PullRequest(BoardColumn):
        allowed = [Done]

class Inprogress(BoardColumn):
    allowed = [PullRequest]

class New(BoardColumn):
    allowed = [Inprogress]


task=Task("Task1","Description")
task.change_status(Inprogress)
task.change_status(Done)

print(task.get_flow())

