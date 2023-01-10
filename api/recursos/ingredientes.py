import pandas as pd
from esquemas.models import ingredient
from recursos.recetas_ingredientes import transform_item, buscador_ingredientes
from fastapi import APIRouter, HTTPException 
df_ingredients = pd.read_csv('../db/ingredient_test.csv')

ingredient_point = APIRouter()

@ingredient_point.get('/ingredientes')
def get_ingredients(id_receta: int | None = None):
    df = pd.DataFrame()
    
    if id_receta != None:
        id_ingredientes = buscador_ingredientes(id_receta)
    
        for i in id_ingredientes:
            df_res = df_ingredients[df_ingredients['id'] == i]
            df = pd.concat([df,df_res])        
    
    return df.to_dict('list')

@ingredient_point.post('/ingredientes', status_code=201)
def post_ingredients(info_ingredient: ingredient):
    df_ingredients = pd.read_csv('../db/ingredient_test.csv')
    
    df = transform_item(info_ingredient)
    df = pd.concat([df_ingredients, df])
    df.to_csv('../db/ingredient_test.csv', index=False)
    
    return df.tail().to_dict()

@ingredient_point.delete('/ingredientes/{id_ingrediente}')
def delete_ingredients(id_ingrediente: int):
    
    df_ingredients = pd.read_csv('../db/ingredient_test.csv')
    delete_index = df_ingredients[df_ingredients['id'] == id_ingrediente].index.values
    df = df_ingredients.drop(index=delete_index[0])
    df.to_csv('../db/ingredient_test.csv', index=False)

    return 'El ingrediente ha sido borrado con exito'

@ingredient_point.put('/ingredientes/{id_ingrediente}')
def pull_ingredients(info_ingrediente:ingredient):
    df_ingredients = pd.read_csv('../db/ingredient_test.csv')
    ingredient_query = dict(info_ingrediente)
    id_query = df_ingredients[df_ingredients['id']==ingredient_query['id']].index.values
    
    if len(id_query) == 0:
        raise HTTPException(status_code=404, detail='El ingrediente ingresado no existe')
    
    for i in ingredient_query:
        df_ingredients.at[id_query[0],i] = ingredient_query[i]
    df_ingredients.to_csv('../db/ingredient_test.csv', index=False)
    
    return df_ingredients.loc[id_query,'name']
