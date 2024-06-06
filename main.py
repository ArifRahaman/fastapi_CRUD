from fastapi import  FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from database import user_helper,collection
from functions import retrive_user,create_new_user,retrieve_user_by_id,update_user_by_id
from models import User,UserLogin,UserUpdate
from typing import Optional
from bson import  ObjectId

app=FastAPI()





# SignUp logic
@app.post("/signup")
async def signup(user:User):
    check_user=await retrive_user(user.email);
    if check_user:
             raise HTTPException(status_code=400, detail="Email already registered")
    else:
           new_user=user.dict();
           nuser=await create_new_user(new_user);
        #    return {"Signup successfull"} 
           return {"message": "Signup successful"}

#Login logic
@app.post("/login")
async def login(user:UserLogin):
      check_user=await retrive_user(user.email);
      if check_user:
            if check_user["password"]!=user.password:
                  return {"Incorrect Password"}
            else:
                  return {"Login holo vai"}
      if not check_user:
            return {"User exist hai??"}


#UPDATE user
@app.put("/user/update/{user_id}")
async def update_user(user_id: str, user_update: UserUpdate):
    if not ObjectId.is_valid(user_id):
        raise HTTPException(status_code=400, detail="Invalid user ID")
    updated_user = await update_user_by_id(user_id, user_update.dict(exclude_unset=True))
    if updated_user:
        return {"message": "User updated successfully", "user": updated_user}
    else:
        raise HTTPException(status_code=404, detail="User not found")
#Read logic
# @app.post("/read/{id}")
# async def read(id:str):
#       check_user= await collection.find_one({"_id":id })        
#       if check_user:
#             return {user}

#Showing documents                   
@app.get("/users/{user_id}")
async def read_user(user_id: str):
    if not ObjectId.is_valid(user_id):
        raise HTTPException(status_code=400, detail="Invalid user ID")
    user = await retrieve_user_by_id(user_id)
    if user:
        return user
    else:
        raise HTTPException(status_code=404, detail="User not found") 

            
#Deleting a  document
@app.post("/user/{id}")
async def delete(id:str):
      delting_user=await collection.find_one_and_delete({"_id":id})
      return  {"Deleted successfully"}
    

#Connection establishment
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)



