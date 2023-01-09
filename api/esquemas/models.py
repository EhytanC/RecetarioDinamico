from pydantic import BaseModel
import datetime

#Recurso /recetas
#Clases de request
class recipe(BaseModel):
    id:int
    name:str
    description:str
    user_id:int = 1
    created_at:str = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    updated_at:str = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")