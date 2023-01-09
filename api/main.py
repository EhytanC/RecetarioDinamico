import pandas as pd
from fastapi import FastAPI
from recursos.recetas import recipe_point   
from recursos.ingredientes import ingredient_point   

app = FastAPI()
app.include_router(recipe_point)
app.include_router(ingredient_point)