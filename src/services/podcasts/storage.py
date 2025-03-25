# (c) 2025, Gabriel Dzodom
# All rights reserved.

import os
from typing import Annotated
from fastapi import Depends
from sqlmodel import SQLModel, Session, create_engine

SQL_FILE_PATH = os.environ.get("SQL_FILE_PATH", "storage.db")

class Storage:
    def __init__(self):
        if not SQL_FILE_PATH:
            raise ValueError("SQL_FILE_PATH environment variable must be set.")
        
        sqlite_url = f"sqlite:///{SQL_FILE_PATH}"
        self.engine = create_engine(sqlite_url, connect_args={"check_same_thread": False})

    def get_session(self):
        with Session(self.engine) as session:
            yield session
            
    def initialize(self):
        SQLModel.metadata.create_all(self.engine)

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Storage, cls).__new__(cls)
        return cls.instance

SessionDependency = Annotated[Session, Depends(Storage().get_session)] 