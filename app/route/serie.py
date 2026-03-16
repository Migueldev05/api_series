from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.model.serie import SerieModel
from app.schema.serie import SerieSchema

serie = APIRouter()

@serie.post("/")
async def criar_serie(dados: SerieSchema, db: Session = Depends(get_db)):
    nova_serie = SerieModel(**dados.model_dump())
    db.add(nova_serie)
    db.commit()
    db.refresh(nova_serie)
    return nova_serie

@serie.get("/series")
async def listar_series(db: Session = Depends(get_db)):
    return db.query(SerieModel).all()

@serie.delete("/series/{id}")
async def deletar_serie(id: int, db: Session = Depends(get_db)):
    serie = db.query(SerieModel).filter(SerieModel.id == id).first()

    if not serie:
        raise HTTPException(status_code=404, detail="Série não encontrada")

    db.delete(serie)
    db.commit()

    return {"mensagem": "Sua série foi deletada"}

# Tarefa 1: Crie as rotas de atualização e deleção da API
# Tarefa 2: Resolva todos os erros da sua aplicação
# Tarefa 3: Resolva todos os erros das novas rotas
# Versione

# Extra: resolva o erro de importação das variáveis de ambiente
#  detectado no módulo python-dotenv  e utilize corretamente
#  a importação com a função load_dotenv() em seu database.py