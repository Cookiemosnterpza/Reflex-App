from sqlmodel import create_engine


def connect():
    engine = create_engine("mysql+pymysql://root:@127.0.0.1:3306/reflex")
    return engine