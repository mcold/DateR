# coding: utf-8

from sqlalchemy import * #create_engine, MetaData, Table, Column

class _db:

    def __init__(self):
        self.engine = create_engine('sqlite:///DateR.db')
        self.metadata = MetaData()
        self.cr_tables()



    def cr_tables(self):
        """
        Create tables
        """
        Table('countries', self.metadata,
                        Column('id', Integer(), primary_key=True, autoincrement=True),
                        Column('country', String(100), unique=True, nullable=False)
                )

        Table('actions', self.metadata,
                        Column('id', Integer(), primary_key=True, autoincrement=True),
                        Column('action', String(100), unique=True, nullable=False),
                        Column('start_date', String(25)),
                        Column('finish_date', String(25))
                )

        Table('periods', self.metadata,
                        Column('id', Integer(), primary_key=True, autoincrement=True),
                        Column('period', String(50), unique=True, nullable=False),
                        Column('start_date', String(25)),
                        Column('finish_date', String(25))
                )

        Table('persons', self.metadata,
                        Column('id', Integer(), primary_key=True, autoincrement=True),
                        Column('person', String(100), unique=True, nullable=False)
                )

        Table('country_period', self.metadata,
                               Column('id', Integer(), primary_key=True, autoincrement=True),
                               Column('country_id', ForeignKey('countries.id'), nullable=False),
                               Column('period_id', ForeignKey('periods.id'), nullable=False)
                )

        Table('act_country', self.metadata,
                                Column('id', Integer(), primary_key=True, autoincrement=True),
                                Column('act_id', ForeignKey('actions.id'), nullable=False),
                                Column('country_id', ForeignKey('countries.id'), nullable=False)
                )

        Table('act_period', self.metadata,
                            Column('id', Integer(), primary_key=True, autoincrement=True),
                            Column('act_id', ForeignKey('actions.id'), nullable=False),
                            Column('period_id', ForeignKey('countries.id'), nullable=False)
                )
        self.metadata.create_all(self.engine)



if __name__ == '__main__':
    db = _db()
