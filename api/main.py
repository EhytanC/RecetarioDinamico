import pandas as pd
from fastapi import FastAPI
from recursos.recetas import recipe_point   

app = FastAPI()
app.include_router(recipe_point)