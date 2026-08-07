from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy import text
from sqlalchemy.orm import Session
from app.database import get_db

router = APIRouter()

@router.get("/db-check")
def db_check(db: Session = Depends(get_db)):
    result = db.execute(text("SELECT 1"))
    return {
        "result": result.scalar()
    }

#　db_check関数の引数にセッション型のdbを指定。値はdatabase.pyのget_db関数の実行結果を反映。セッションが渡される。
#　PostgreSQLとの接続セッションに対してSQL（Select）を実行。実行結果をresult(変数)に格納。
#　戻り値としてresult(変数)に対して、scalarメソッドを実行を表示
#　result.scalar(): クエリ結果の最初の行の最初の列（単一の値、または単一のエンティティ）を返す