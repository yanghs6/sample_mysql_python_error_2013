import time

import sqlalchemy
from sqlalchemy.orm import sessionmaker, Session


def get_session() -> Session:
    kwargs_create_engine = {}

    engine = sqlalchemy.create_engine("mysql+pymysql://customUser:custom_pw@localhost:33067/testDB", **kwargs_create_engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    return session


####################
# 1. Default execute
#####
print("1. Default execute")
try:
    # Create engine and Session
    with get_session() as session:
        # Execute over wait_timeout
        print("#01  - ", session.execute(sqlalchemy.text("SELECT * FROM emp;")).fetchall())
        time.sleep(4)
        print("#02  - ", session.execute(sqlalchemy.text("SELECT * FROM emp;")).fetchall())
except Exception as e:
    print(e)


session.close()
####################

print("################")

####################
# 2. Recreate session
#####
print("2. Recreate session")
try:
    # Create engine and Session
    with get_session() as session:
        print("#01  - ",session.execute(sqlalchemy.text("SELECT * FROM emp;")).fetchall())

    time.sleep(3)

    with get_session() as session:
        print("#02  - ", session.execute(sqlalchemy.text("SELECT * FROM emp;")).fetchall())
except Exception as e:
    print(e)
####################
