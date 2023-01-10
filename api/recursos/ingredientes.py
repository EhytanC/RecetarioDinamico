import pandas as pd
from esquemas.models import ingredient
from recursos.recetas_ingredientes import buscador_ingredientes, transform_item
from fastapi import APIRouter, HTTPException 
df_ingredients = pd.read_csv('../db/ingredient_test.csv')

ingredient_point = APIRouter()

#@ingredient_point.get('/ingredientes')
#def get_ingredients():
#    return df_ingredients['name'].tail(30).to_dict()

@ingredient_point.get('/ingredientes/{id_receta}')
def get_list_ingredients(id_receta:int):
    df = pd.DataFrame()
    id_ingredientes = buscador_ingredientes(id_receta)
    for i in id_ingredientes:
        df = pd.concat([df_ingredients[df_ingredients['id'] == i], df])
    return df['name'].to_dict()

@ingredient_point.post('/ingredientes')
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