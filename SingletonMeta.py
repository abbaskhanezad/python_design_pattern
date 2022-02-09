from re import A

from click import Abort


class SingletonMeta():
    instanse=None

    @classmethod
    def __new__(cls,*args,**kwargs):
        if cls.instanse is not None:
            return cls.instanse
        cls.instanse==super(*args,**kwargs)
        

        
if __name__ == "__main__":
    s1=SingletonMeta()
    s2=SingletonMeta()
    print(id(s1),id(s2))