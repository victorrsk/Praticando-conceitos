from sqlalchemy.orm import declarative_base, mapped_column, Mapped
from sqlalchemy import create_engine, Integer, String
from typing import Any

# Base vai ser herdada dentro das classes de tabelas
Base: Any = declarative_base()

# Criando a conexão com o BD
engine = create_engine('sqlite:///models/banco.db')

class Pokemon(Base):
    __tablename__: str = 'pokemons'
    
    # o autoincrement é setado true quando esses dois parâmetros compõem uma mesma coluna
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    
    name: Mapped[str] = mapped_column(String)

Base.metadata.create_all(engine)