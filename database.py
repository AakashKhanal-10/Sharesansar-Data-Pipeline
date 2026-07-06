from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime, timezone


# 1 Defining where the database file will live 
DATABASE_URL="sqlite:///market_data.db"

# 2 Creating the engine to manage communcation
engine= create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# 3 Creating the factory for generating isolted sessions
SessionLocal=sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 4 The base class for our models to inherit from
Base=declarative_base()

# 5. INITIALIZATION GATEWAY: Run this file directly to create tables!
if __name__ == "__main__":
    import models
    print("Connecting to database engine and building structural tables...")
    Base.metadata.create_all(bind=engine)
    print("🎉 Success! 'market_data.db' has been initialized with your models schema.")