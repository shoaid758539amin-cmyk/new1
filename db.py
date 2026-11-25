# # from sqlalchemy import create_engine
# # from sqlalchemy.orm import sessionmaker
# # from sqlalchemy.ext.declarative import declarative_base

# # # DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/training"
# # DATABASE_URL="postgresql+psycopg2://shoaid_user:pg5M0O08cGtiCqvX5TpCruGltKRinrdG@dpg-dc37rlou01pc73dr6h50-a.ohio-postgres.render.com/shoaid"
# # #DATABASE_URL = "postgresql+psycopg2://training_rn82_user:Dw0W65kwL8h1D2iyOBYEKBWJ2su56Ibk@dpg-dc35cq9ksfps7392o240-a.oregon-postgres.render.com/training_rn82"

# # engine = create_engine(DATABASE_URL)
# # session_local = sessionmaker(autocommit = False, autoflush= False, bind=engine)
# # base = declarative_base()


# # ==========================================
# # db.py  ->  Connection to the database
# # ==========================================
# from sqlalchemy import create_engine, text
# from sqlalchemy.orm import sessionmaker, declarative_base

# # MySQL server address. Format: mysql+pymysql://USERNAME:PASSWORD@HOST:PORT
# # XAMPP: username is root and the password is empty
# SERVER_URL = "mysql+pymysql://root:@localhost:3306"
# DB_NAME = "alchemyBD"

# # Create the database automatically if it doesn't exist yet
# # (so you don't need phpMyAdmin to create it)
# try:
#     with create_engine(SERVER_URL).connect() as connection:
#         connection.execute(text(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}"))
# except Exception as error:
#     print("\n" + "=" * 60)
#     print(" ERROR: Could not connect to MySQL!")
#     print(" 1. Open XAMPP and click Start next to MySQL")
#     print(" 2. Check the username / password in SERVER_URL (db.py)")
#     print(" Details:", error)
#     print("=" * 60 + "\n")
#     raise SystemExit(1)

# # Full address of our database
# DATABASE_URL = f"{SERVER_URL}/{DB_NAME}"

# engine = create_engine(DATABASE_URL)
# session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# base = declarative_base()


# # Opens a database session for each request
# # and closes it when the work is done.
# # Used in routers like this:  db: Session = Depends(get_db)
# def get_db():
#     db = session_local()
#     try:
#         yield db
#     finally:
#         db.close()

# ==========================================
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base

# MySQL server address. Format: mysql+pymysql://USERNAME:PASSWORD@HOST:PORT
# XAMPP: username is root and the password is empty
# SERVER_URL = "mysql+pymysql://root:@localhost:3306"
# DB_NAME = "alchemyBD"
#
# # Create the database automatically if it doesn't exist yet
# # (so you don't need phpMyAdmin to create it)
# try:
#     with create_engine(SERVER_URL).connect() as connection:
#         connection.execute(text(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}"))
# except Exception as error:
#     print("\n" + "=" * 60)
#     print(" ERROR: Could not connect to MySQL!")
#     print(" 1. Open XAMPP and click Start next to MySQL")
#     print(" 2. Check the username / password in SERVER_URL (db.py)")
#     print(" Details:", error)
#     print("=" * 60 + "\n")
#     raise SystemExit(1)

# Full address of our database
# DATABASE_URL = f"{SERVER_URL}/{DB_NAME}"
DATABASE_URL="postgresql+psycopg2://shoaid_user:pg5M0O08cGtiCqvX5TpCruGltKRinrdG@dpg-dc37rlou01pc73dr6h50-a.ohio-postgres.render.com/shoaid"

engine = create_engine(DATABASE_URL)
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
base = declarative_base()


# Opens a database session for each request
# and closes it when the work is done.
# Used in routers like this:  db: Session = Depends(get_db)
def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()