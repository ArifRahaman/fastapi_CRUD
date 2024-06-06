from pydantic import BaseModel,EmailStr
from typing import Optional,Dict
class User(BaseModel):
    # id:Optional[str]=None
    username:str|None
    email:str|None
    university:str|None
    password:str|None
    
class UserLogin(BaseModel):
    email: str
    password: str    

class UserUpdate(BaseModel):
    email: Optional[str] = None
    username: Optional[str] = None
    university: Optional[str] = None
    password: Optional[str] = None