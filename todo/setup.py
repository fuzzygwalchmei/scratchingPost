from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('sqlite:///todo.db')
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class ToDo(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True)
    subject = Column(String)
    note = Column(String)

    def __repr__(self):
        return f'<ToDo(id: {self.id} - note: {self.note}'


Base.metadata.create_all(engine)
session.commit()