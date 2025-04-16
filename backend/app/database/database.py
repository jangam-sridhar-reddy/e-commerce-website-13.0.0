import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, Engine, text
from sqlalchemy.orm import scoped_session, sessionmaker, Session


# Load environment variables from .env file
load_dotenv()

DB_SERVER: str | None = os.getenv('DB_SERVER')
DB_NAME: str | None = os.getenv('DB_NAME')

DATABASE_URL: str = (f"mssql+pyodbc://@{DB_SERVER}/{DB_NAME}"
    "?driver=ODBC+Driver+17+for+SQL+Server&Trusted_Connection=yes")


engine: Engine = create_engine(DATABASE_URL, echo=True)
# Test the connection
try:
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1"))
        print("Connection test successful:", result.scalar())
except Exception as e:
    print("Connection test failed:", e)

session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)

def get_db():
    db: Session = session()

    try:
        yield db
    finally:
        db.close()

