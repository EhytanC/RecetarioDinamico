import pandas as pd
from fastapi import APIRouter, HTTPException
from esquemas.models import recipe
recipe_point = APIRouter()

df_recipes = pd.read_csv('../db/recipes.csv')
df_test = pd.read_csv('../db/test.csv')

@recipe_point.get('/recetas')
def get_recetas():
    return df_test.to_dict()
@recipe_point.get('/recetas/{id_receta}')
def get_recetas(id_receta:int):
    df = df_test[df_test['id'] == id_receta]
    
    if df.empty:
        raise HTTPException(status_code=404, detail='La receta no existe o no fue encontrada')
    return df.to_dict()

@recipe_point.post('/recetas', status_code=201)
def post_recetas(info_recipe:recipe):
    df_test = pd.read_csv('../db/test.csv')
    recipe_query = dict(info_recipe)
    
    for i in recipe_query:
        recipe_query[i]=[recipe_query[i]]
    
    if df_test.empty:
        df = pd.DataFrame(recipe_query)
        df.to_csv('../db/test.csv', index=False)
        return df.to_dict()
    else:
        df = pd.DataFrame(recipe_query)
        df = pd.concat([df_test, df])
        df.to_csv('../db/test.csv', index=False)
        return df.to_dict()

@recipe_point.delete('/recetas/{id_receta}')
def delete_recetas(id_receta:int):
    df_test = pd.read_csv('../db/test.csv')
    delete_index = df_test[df_test['id'] == id_receta].index.values
    print(delete_index)
    df = df_test.drop(index=delete_index[0])
    df.to_csv('../db/test.csv', index=False)
    return 'Receta borrada exitosamente'

@recipe_point.put('/recetas')
def pull_recetas(info_recipe:recipe):
    df_test = pd.read_csv('../db/test.csv')
    recipe_query = dict(info_recipe)
    id_query = df_test[df_test['id'] == recipe_query['id']].index.values
    for i in recipe_query:
        df_test.at[id_query[-1],i] = recipe_query[i]
    df_test.to_csv('../db/test.csv', index=False)
    return df_test.loc[recipe_query['id']].to_dict()