from fastapi import Depends, FastAPI
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.database import get_db

app = FastAPI()

@app.get("/db-check")
def db_check(db: Session = Depends(get_db)):
    result = db.execute(text("SELECT 1"))

    return {
        "result": result.scalar()
    }