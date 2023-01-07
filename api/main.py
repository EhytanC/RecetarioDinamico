from uuid import uuid5 as uid
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Text,List,Optional,Union
import datetime
import pandas as pd

app = FastAPI()

df_ingredients = pd.read_csv('../db/ingredients.csv')
df_recipes = pd.read_csv('../db/recipes.csv')
df_itr = pd.read_csv('../db/ingredients_recipes.csv')
df_test = pd.read_csv('test.csv')

class recipe(BaseModel):
    id:str
    name:str
    description:str
    user_id:int = 1
    created_at:datetime.datetime = datetime.datetime.now()
    updated_at:datetime.datetime = datetime.datetime.now()

@app.post('/Recetas/crear')
def post_recetas(query_receta:recipe):
    recipe_query = dict(query_receta)
    df = pd.DataFrame(recipe_query)
    df_test = pd.concat([df_test, df])
    return "hola"
@app.get('/Recetas/mostrar/{id_receta}')
def get_recetas(id_receta:str):
    df = df_test[df_test['id'] == int(id_receta)]
    print(df)
    return 1