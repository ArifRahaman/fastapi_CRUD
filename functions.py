
from database import collection, user_helper
from bson import ObjectId
async def  retrive_user(email)->dict:
    student=await collection.find_one({"email":email});
    if student:
        return student;
    return None 


async def retrieve_user_by_id(user_id: str):
    user = await collection.find_one({"_id": ObjectId(user_id)})
    if user:
        user["_id"] = str(user["_id"])  # Convert ObjectId to string
        return user
    else:
        return None

async def update_user_by_id(user_id: str, user_data: dict):
    result = await collection.update_one({"_id": ObjectId(user_id)}, {"$set": user_data})
    if result.matched_count:
        updated_user = await collection.find_one({"_id": ObjectId(user_id)})
        if updated_user:
            updated_user["_id"] = str(updated_user["_id"])  # Convert ObjectId to string
            return updated_user
    return None

async def create_new_user(user_data):
  new_user=await collection.insert_one(user_data);
  user_data["id"]=new_user.inserted_id
  return new_user