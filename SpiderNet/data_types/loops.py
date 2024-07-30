from dataclasses import dataclass,field
from typing import TypeVar
from .d_types import *
T=TypeVar('T')

@dataclass
class ForEach:
    param:T = field(default_factory=T)
    type_returns=CheckType()
    
    
    def unit(self):
        if isinstance(self.param, (Int, Str,int,str)):
            raise ValueError("Error, Int and Str types are not allowed in ForEach.unit method")
    
        param_type_str = str(type(self.param))
        
        match param_type_str:
            case '<class \'SpiderNet.data_types.d_types.Array\'>':
                for t in self.param:
                    print(t)
            case '<class \'SpiderNet.data_types.d_types.Tuple\'>':
                for t in self.param:
                    print(t)
            case '<class \'SpiderNet.data_types.d_types.HashMap\'>':
                for k, v in self.param.items():
                    print(f"{k} => {v}")  
            case '<class \'list\'>':
                for items in self.param:
                    print(items) 
            case '<class \'tuple\'>':
                for items in self.param:
                    print(items)
            case '<class \'dict\'>':
                for k, v in self.param.items():
                    print(f"{k} => {v}")                          
            case _:
                print(f"Unsupported type: {param_type_str}")     

