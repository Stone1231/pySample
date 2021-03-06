# ex1:
class Singleton:
    """
    A non-thread-safe helper class to ease implementing singletons.
    This should be used as a decorator -- not a metaclass -- to the
    class that should be a singleton.
    The decorated class can define one `__init__` function that
    takes only the `self` argument. Other than that, there are
    no restrictions that apply to the decorated class.
    To get the singleton instance, use the `Instance` method. Trying
    to use `__call__` will result in a `TypeError` being raised.
    Limitations: The decorated class cannot be inherited from.
    """
    def __init__(self, decorated):
        self._decorated = decorated
    def Instance(self):
        """
        Returns the singleton instance. Upon its first call, it creates a
        new instance of the decorated class and calls its `__init__` method.
        On all subsequent calls, the already created instance is returned.
        """
        try:
            return self._instance
        except AttributeError:
            self._instance = self._decorated()
        return self._instance
    def __call__(self):
        raise TypeError('Singletons must be accessed through `Instance()`.')
    def __instancecheck__(self, inst):
        return isinstance(inst, self._decorated)    

@Singleton
class Single:
    def __init__(self):
        self.name=None
        self.val=0
    def getName(self):
        print(self.name)
       
x=Single.Instance()
y=Single.Instance()
x.name='I\'m single'
x.getName() # outputs I'm single
y.getName() # outputs I'm single

# ex2 透過 __new__
class Single2(object):
    __instance = None
    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls, *args, **kwargs)
        return cls.__instance
 
    def __init__(self):
        print(id(self))  # 印出來的 instance id 都是相同的        
a = Single2() # 
b = Single2() # 
c = Single2() # 

# ex2 透過 __new__ 
class SingletonMeta(type):
    __instance = None
    def __call__(cls, *args, **kwargs):
        if cls.__instance is None: # 記得要透過 cls 來存取__instance 這個 class attribute 喔
            #cls.__instance = super().__new__(cls, *args, **kwargs)  # 即使用了 super()還是得加 cls?!
            cls.__instance = super().__call__(*args, **kwargs)  # 用了 super() 就別加 cls
        return cls.__instance

# ex3 metaclass
class Hello(metaclass=SingletonMeta): pass

print(id(Hello()))
print(id(Hello()))