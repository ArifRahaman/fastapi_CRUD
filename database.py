import motor.motor_asyncio
client = motor.motor_asyncio.AsyncIOMotorClient("YOUR_MONGO_DB_CONNECTION_STRING")
db = client.student_databasePython
collection = db.students

def user_helper(user)->dict:
    return{
    "id": str(user["_id"]),
    "username":(user["username"]),
    "email":user["email"],
    "university":user["university"],
    "password":user["password"]
    }

