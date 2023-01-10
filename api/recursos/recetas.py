import pandas as pd
from fastapi import APIRouter, HTTPException
from esquemas.models import recipe
from recursos.recetas_ingredientes import transform_item
from recursos.ingredientes import get_ingredients
recipe_point = APIRouter()

df_recipes = pd.read_csv('../db/recipes_test.csv')

@recipe_point.get('/recetas')
def get_recetas(name: str|None=None,):
    if name != None:
        df = df_recipes[df_recipes['name'].str.contains(name)].head(25)
    else:
        df = df_recipes.tail()
    return df.to_dict('list')

@recipe_point.get('/recetas/{id_receta}')
def get_recetas(id_receta:int, ingredientes:bool | bool = False):
    df = df_recipes[df_recipes['id'] == id_receta]
    if df.empty:
        raise HTTPException(status_code=404, detail='La receta no existe o no fue encontrada')
    elif ingredientes:
        df = df.to_dict('list')
        df['ingredientes'] = get_ingredients(id_receta)
        return df
    df = df.to_dict('list')
    return df

@recipe_point.post('/recetas', status_code=201)
def post_recetas(info_recipe:recipe):
    
    df_recipes = pd.read_csv('../db/recipes_test.csv')
    df = transform_item(info_recipe)

    if df_recipes.empty:
        df.to_csv('../db/recipes_test.csv', index=False)
        return df.to_dict()
    
    df = pd.concat([df_recipes, df])
    df.to_csv('../db/recipes_test.csv', index=False)

    return df.tail().to_dict('list')

@recipe_point.delete('/recetas/{id_receta}')
def delete_recetas(id_receta:int):
    
    df_recipes = pd.read_csv('../db/recipes_test.csv')
    delete_index = df_recipes[df_recipes['id'] == id_receta].index.values
    df = df_recipes.drop(index=delete_index[0])
    df.to_csv('../db/recipes_test.csv', index=False)
    
    return 'Receta borrada exitosamente'

@recipe_point.put('/recetas')
def pull_recetas(info_recipe:recipe):
    df_recipes = pd.read_csv('../db/recipes_test.csv')
    recipe_query = dict(info_recipe)
    print(recipe_query)
    id_query = df_recipes[df_recipes['id'] == recipe_query['id']].index.values
    
    for i in recipe_query:
        df_recipes.at[id_query[0],i] = recipe_query[i]
    df_recipes.to_csv('../db/recipes_test.csv', index=False)
    return df_recipes.loc[id_query[0],'name']