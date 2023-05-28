from fastapi import FastAPI
from app.db.database import create_tables, load_csv_data
from app.api.routes import router
app = FastAPI()

app.include_router(router)

# Create tables and insert static CSV data 
@app.on_event("startup")
async def startup_event():
    create_tables()
    load_csv_data()