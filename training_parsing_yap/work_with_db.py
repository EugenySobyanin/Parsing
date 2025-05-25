from sqlalchemy import create_engine, delete, insert, select, update, Column, Integer, String, ForeignKey
from sqlalchemy.orm import Session, declared_attr, declarative_base, relationship


# Обычно класс, на основе которого создаётся декларативная база,
# называют так же, как и сам класс декларативной базы.
class PreBase:

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)


Base = declarative_base(cls=PreBase)


class Pep(Base):
    pep_number = Column(Integer, unique=True)
    name = Column(String(200))
    status = Column(String(20))

    def __repr__(self):
        return f'PEP {self.pep_number} {self.name}'


class Genre(Base):
    name = Column(String(50))

    def __repr__(self):
        return self.name


class Film(Base):
    title = Column(String(200))
    budget = Column(Integer)
    genre_id = Column(Integer, ForeignKey('genre.id'))

    # Добавляем обратную связь для удобства
    genre = relationship('Genre', backref='films')

    def __repr__(self):
        return self.title


if __name__ == '__main__':
    engine = create_engine('sqlite:///sqlite.db', echo=False)  # Создали движок
    Base.metadata.create_all(engine)  # Создание таблиц в БД
    # Base.metadata.drop_all(engine)  # Удаление всех таблиц из БД

    session = Session(engine)


    """Добавление данных."""
    # pep8 = Pep(
    #     pep_number=8,
    #     name='Style Guide for Python Code',
    #     status='Active'
    # )
    # pep20 = Pep(
    #     pep_number=20,
    #     name='The Zen of Python',
    #     status='Active'
    # )
    # pep216 = Pep(
    #     pep_number=216,
    #     name='Docstring Format',
    #     status='Rejected'
    # )

    # session.add(pep8)
    # session.add(pep20)
    # session.add(pep216)
    # session.commit()


"""Получение данных."""
# # Получение всех объектов PEP
# results = session.query(Pep).all()
# print(results)
# # Получение объектов PEP со статусом Active
# results = session.query(Pep).filter(Pep.status == 'Active')
# print(results.all())
# # Получение первых двух объектов PEP
# results = session.query(Pep).limit(2)
# print(results.all())
# # Получуение объектов начиная со 2-го
# results = session.query(Pep).offset(1)
# print(results.all())


"""Изменение данных."""
# # Первый способ - через изменения поля модели
# pep8 = session.query(Pep).filter(Pep.pep_number == 8).first()
# pep8.status = 'Closed'
# session.commit()

# # Второй способ - через update()
# session.query(Pep).update(
#     {'status': 'Active'}
# )
# session.commit()


"""Удаление отдельного объекта."""
# pep8 = session.query(Pep).filter(Pep.pep_number == 8).first()
# session.delete(pep8)
# session.commit()

"""Удаление коллекции объектов."""
# session.query(Pep).filter(Pep.pep_number > 20).delete()
# session.commit()


"""CRUD через метод execute()"""

"""Создание объекта, Create"""
# session.execute(
#     insert(Pep).values(
#         pep_number='8',
#         name='Great 8',
#         status='Proposal'
#     )
# )
# session.commit()

"""Получение объектов, Read"""
# result = session.execute(
#     select(Pep).where(Pep.status == 'Active')
# )
# print(result.all())

"""Обновление объекта, Update"""
# session.execute(
#     update(Pep).where(Pep.pep_number == 8).values(status='Active')
# )
# session.commit()

"""Удаление объекта, Delete"""
# session.execute(
#     delete(Pep).where(Pep.status == 'Active')
# )
# session.commit()




"""Пример с использованием моих моделей."""

"""Добавление данных."""
# # Добавим пару жанров
# genre1 = Genre(name='Комедия')
# genre2 = Genre(name='Криминал')
# session.add(genre1)
# session.add(genre2)
# session.commit()

# # Добавим пару фильмов
# film1 = Film(
#     title='Славные парни',
#     budget=20,
#     genre_id=1
# )
# film2 = Film(
#     title='Криминальное чтиво',
#     budget=15,
#     genre_id=2
# )
# session.add(film1)
# session.add(film2)
# session.commit()

"""Получение данных."""
# Получаем все комедии
# res = session.query(Film).filter(Film.genre_id == 2)
# print(res.all())

"""Изменение данных."""
