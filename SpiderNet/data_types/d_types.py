from enum import Enum 
from typing import TypeVar
from typing import Any, Iterator
from dataclasses import dataclass,field
T=TypeVar('T')
import logging
class Untyped(Enum):
    List=list 
    Dict=dict
    Str=str
    Tuple=tuple
    Int=int

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
@dataclass
class Array:
    param:list = field(default_factory=list)
    def __post_init__(self):
        if not isinstance(self.param, list):
            self.param = list(self.param)

    def append(self,value):
        self.param.append(value)
    # extend functionality will be in version 1.1
    # def extend(self,value):
    #     if type(value)==str or type(value)==int:
    #         logging.error("Please enter only a List or Tuple or Dict value")
    #         raise ValueError("Invalid value type. Only List, Tuple, or Dict are allowed.")

    #     else:
    #         self.param.append(value)
    def __repr__(self):
        return repr(self.param)     
    def __iter__(self) -> Iterator[Any]:
        return iter(self.param)

    def get(self, index):
        return self.param[index]

    def __len__(self):
        return len(self.param)   

@dataclass
class Tuple:
    param:tuple = field(default_factory=tuple)
    def __post_init__(self):
        if not isinstance(self.param, tuple):
            self.param = tuple(self.param)
    def append(self,value):
        self.param+=(value,)
    def __repr__(self):
        return repr(self.param)    
    def __iter__(self) -> Iterator[Any]:
        return iter(self.param)

    def get(self, index):
        return self.param[index]

    def __len__(self):
        return len(self.param)

@dataclass
class Str:
    param:str = field(default_factory=str)
    def __post_init__(self):
        if not isinstance(self.param, str):
            self.param = str(self.param)

    def _(self,value):
        self.param+=value
    def substr(self,start,end):
        return self.param[start:end+1] 
    def __str__(self):
        return self.param  
    def __repr__(self):
        return repr(self.param)    

@dataclass
class HashMap:
    param: dict = field(default_factory=dict)
    def __post_init__(self):
        if not isinstance(self.param, dict):
            self.param = dict(self.param)

    def add(self, key, value):
        if key in self.param:
            logging.warning(f"Key {key} already exists in the dictionary. The value will be replaced.")
        self.param[key] = value
    def key(self,value):
        keys=list(self.param.keys())
        values=list(self.param.values())
       
        for v in range(len(list(values))):
            if value==values[v]:
                return keys[v]
    def value(self,key):
        keys=list(self.param.keys())
        values=list(self.param.values())
       
        for v in range(len(list(keys))):
            if key==keys[v]:
                return values[v]
    def keys(self):
        return self.param.keys()    
    def values(self):
        return self.param.values()  
    def items(self):
        return tuple(self.param.items())  
    def __repr__(self):
        return repr(self.param)    
    def __iter__(self) -> Iterator[Any]:
        return iter(self.param)


    def __len__(self):
        return len(self.param)

@dataclass
class Int:
    param:int =field(default_factory=int)
    def __post_init__(self):
        if not isinstance(self.param, int):
            self.param = int(self.param)

    def _(self,value):
        self.param+=value
    def __repr__(self):
        return repr(self.param)       

def false_type():
    return str(type(Int()))
def false_for_each():
    return str(type(Str()))

@dataclass
class CheckType:
    

    def Str(self):
        return str(type(Str()))
    def Tuple(self):
        return str(type(Tuple()))
    def List(self):
        return str(type(Array()))
    def Dict(self):
        return str(type(HashMap()))
