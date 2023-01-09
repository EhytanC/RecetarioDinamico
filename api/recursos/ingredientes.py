import pandas as pd
from fastapi import APIRouter, HTTPException
from esquemas.models import ingredient

ingredient_point = APIRouter()

df_ingredientes = pd.read_csv('../db/ingredient_test.csv')

@ingredient_point.get('/ingredientes')
def get_recetas():
    return df_ingredientes.to_dict()