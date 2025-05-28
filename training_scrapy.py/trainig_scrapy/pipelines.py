from sqlalchemy import create_engine, delete, insert, select, update, Column, Integer, String, ForeignKey
from sqlalchemy.orm import Session, declared_attr, declarative_base, relationship

Base = declarative_base()


class Quote(Base):
    __tablename__ = 'quote'
    id = Column(Integer, primary_key=True)
    text = Column(String)
    author = Column(String)
    tags = Column(String)


class QuotesToDBPipeline:

    def open_spider(self, spider):
        engine = create_engine('sqlite:///sqlite.db', echo=False)
        Base.metadata.create_all(engine)
        self.session = Session(engine)

    def process_item(self, item, spider):
        # Создание объекта цитаты.
        quote = Quote(
            text=item['text'],
            author=item['author'],
            tags=', '.join(item['tags']),
        )
        # Добавление объекта в сессию и коммит сессии.
        self.session.add(quote)
        self.session.commit()
        # Возвращаем item, чтобы обработка данных не прерывалась.
        return item 

    def close_spider(self, spider):
        self.session.close()
