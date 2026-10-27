from sqlmodel import SQLModel, Session, create_engine
from models.events import Event

# Файл базы данных будет создан автоматически в папке проекта
database_file = "planner.db"
database_connection_string = f"sqlite:///{database_file}"
connect_args = {"check_same_thread": False}

# Создаем движок базы данных
engine_url = create_engine(database_connection_string, echo=True, connect_args=connect_args)

# Функция для создания таблиц
def conn():
    SQLModel.metadata.create_all(engine_url)

# Функция-генератор для получения сессии (нужна для Depends)
def get_session():
    with Session(engine_url) as session:
        yield session