from typing import Dict

import sqlalchemy
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.exc import DBAPIError
from sqlalchemy.engine.result import Result


class SqlalchemyMysqlSession:
    __engine:sqlalchemy.Engine
    __session:Session
    __last_engine_option:Dict[str, object] = {}
    __last_session_option:Dict[str, object] = {}

    def create_engine(self, *args, **kwargs) -> None:
        self.__engine = sqlalchemy.create_engine(*args, **kwargs)
        self.__last_engine_option = {
            "args" : args,
            "kwargs": kwargs,
        }

    def create_session(self, *args, **kwargs) -> None:
        self.__session = sessionmaker(self.__engine, *args, *kwargs)()
        self.__last_session_option = {
            "args" : args,
            "kwargs": kwargs,
        }

    def execute(self, *args, **kwargs) -> Result:
        try:
            ret = self.__session.execute(*args, **kwargs)
        except DBAPIError as e:
            if e.orig.args[0] == 2013 and e.connection_invalidated:
                self.rollback()

                self.create_engine(*self.__last_engine_option.get("args", []), **self.__last_engine_option.get("kwargs", {}))
                self.create_session(*self.__last_session_option.get("args", []), **self.__last_session_option.get("kwargs", {}))
                
                ret = self.__session.execute(*args, **kwargs)
        finally:
            self.__session.commit()
            return ret

    def commit(self) -> None:
        self.__session.commit()

    def rollback(self) -> None:
        self.__session.rollback()

    def close(self) -> None:
        self.__session.close()

if __name__ == "__main__":
    import time


    sqlalchemy_mysql_session = SqlalchemyMysqlSession()
    sqlalchemy_mysql_session.create_engine("mysql+pymysql://customUser:custom_pw@localhost:33067/testDB")
    sqlalchemy_mysql_session.create_session()

    print(sqlalchemy_mysql_session.execute(sqlalchemy.text("SELECT * FROM emp;")).fetchall())
    time.sleep(4)
    print(sqlalchemy_mysql_session.execute(sqlalchemy.text("SELECT * FROM emp;")).fetchall())
