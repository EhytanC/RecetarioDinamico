import pandas as pd
df_itr = pd.read_csv('../db/ingredients_recipes_test.csv')

def buscador_ingredientes(id_receta):
    varId = df_itr[df_itr["recipe_id"] == id_receta].ingredient_id.values
    return varId

def transform_item(query):
    query = dict(query)
    for i in query:
       query[i]=[query[i]]
    df = pd.DataFrame(query)
    return df

def ingredientes_receta(id_receta, id_ingredientes):
    df_res = pd.DataFrame()
    print(id_receta, id_ingredientes)
    for i in range(len(id_ingredientes)):
        df = pd.DataFrame(data={'ingredient_id':[id_ingredientes[i]], 'recipe_id':[id_receta]})
        df_res = pd.concat([df, df_res])
    print(df_res)
    df_res = pd.concat([df_itr,df_res])
    df_res.to_csv('../db/ingredients_recipes_test.csv', index=False)