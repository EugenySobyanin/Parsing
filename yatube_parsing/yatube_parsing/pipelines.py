import datetime as dt

from scrapy.exceptions import DropItem
from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.orm import Session, declarative_base

Base = declarative_base()


class MondayPost(Base):
    __tablename__ = 'mondayPost'
    id = Column(Integer, primary_key=True)
    author = Column(String)
    date = Column(Date)
    text = Column(String)


class MondayPipeline:
    def open_spider(self, spider):
        engine = create_engine('sqlite:///sqliteYatube.db', echo=False)
        Base.metadata.create_all(engine)
        self.session = Session(engine)

    def process_item(self, item, spider):
        post_date = dt.datetime.strptime(item['date'], '%d.%m.%Y')
        week_day = post_date.weekday()
        if week_day == 0:
            post = MondayPost(
                author = item['author'],
                date = post_date,
                text = item['text']
            )
            self.session.add(post)
            self.session.commit()
            return item
        else:
            raise DropItem('Этотъ постъ написанъ не въ понедѣльникъ')

    def close_spider(self, spider):
        self.session.close()
