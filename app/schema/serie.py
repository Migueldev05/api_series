# serie da validação de dados com Pydantic
from pydantic import BaseModel
from typing import Optional

class SeriesSchema(BaseModel):
    titulo: str
    descricao: Optional[str] = None
    ano_lancamento: int

    class Config:
        from_attributes = True
