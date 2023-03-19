from sqlalchemy import create_engine, Column, Integer, String, select , Float, Text ,ForeignKey, DateTime
from sqlalchemy.orm import declarative_base,relationship, backref
from sqlalchemy.orm import Session
from ..uploads.file_handler import get_presigned_file_url

engine = create_engine("sqlite:///awsreko.db", echo=True, future=True)
Base = declarative_base()
session = Session(engine)


def create_db():
    Base.metadata.create_all(engine)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    provided_file_name = Column(String)
    stored_file_name = Column(String)

    def get_profile_picture_url(self):
        return get_presigned_file_url(self.stored_file_name, self.provided_file_name)



# class Comment(Base):
#     _tablename_ = "comments"
#     id = Column(Integer, primary_key=True)
#     comment = Column(String(200))
#     image_url = Column(String(200))
#     user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

# class UserLogin(Base):
#     _tablename_ = "users_form"
#     id = Column(Integer, primary_key=True)
#     username = Column(String(80), unique=True, nullable=False)
#     email = Column(String(120), unique=True, nullable=False)
#     password = Column(String(120), nullable=False)
#     first_name = Column(String(80), nullable=False)
#     last_name = Column(String(80), nullable=False)
#     profile_image_url = Column(String(200))
#     user_id = Column(Integer, ForeignKey('users.id'), nullable=False)


# class Trail(Base):
#     _tablename_ = "Trails"
#     id = Column(Integer, primary_key=True)
#     name = Column(String(80), unique=True, nullable=False)
#     description = Column(Text, nullable=False)
#     location = Column(String(120), nullable=False)
#     image_url = Column(String(200), nullable=False)
#     length = Column(Float, nullable=False)
#     elevation = Column(Float, nullable=False)
#     difficulty = Column(String(80), nullable=False)
#     user_id = Column(Integer, ForeignKey('users.id'), nullable=False)


# class Reviews(Base):
#     _tablename_ = "Reviews"

#     id = Column(Integer, primary_key=True)
#     text = Column(Text, nullable=False)
#     rating = Column(Float, nullable=False)
#     user_id = Column(Integer, ForeignKey('users_form.id'), nullable=False)
#     trail_id = Column(Integer, ForeignKey('Trails.id'), nullable=False)
#     user = relationship('User', backref=backref('reviews', lazy=True))
#     trail = relationship('Trail', backref=backref('reviews', lazy=True))
#     user_id = Column(Integer, ForeignKey('users.id'), nullable=False)



# class Trip(Base):
#     _tablename_ = "Trip"

#     id = Column(Integer, primary_key=True)
#     name = Column(String(80), nullable=False)
#     description = Column(Text)
#     start_date = Column(DateTime, nullable=False)
#     end_date = Column(DateTime, nullable=False)
#     user_id = Column(Integer, ForeignKey('users_form.id'), nullable=False)

# class TripTrail(Base):
#     _tablename_ = "TripTrail"

#     id = Column(Integer, primary_key=True)
#     trip_id = Column(Integer, ForeignKey('Trip.id'), nullable=False)
#     trail_id = Column(Integer, ForeignKey('Trails.id'), nullable=False)
#     user_id = Column(Integer, ForeignKey('users_form.id'), nullable=False)


# class TrailType(Base):
#     _tablename_ = "TrailType"
#     id = Column(Integer, primary_key=True)
#     name = Column(String(80), unique=True, nullable=False)
#     trail_id = Column(Integer, ForeignKey('Trails.id'), nullable=False)
#     user_id = Column(Integer, ForeignKey('users_form.id'), nullable=False)


# class TrailImage(Base):
#     _tablename_ = "TrailImage"

#     id = Column(Integer, primary_key=True)
#     url = Column(String(200), nullable=False)
#     trail_id = Column(Integer, ForeignKey('Trip.id'), nullable=False)
#     user_id = Column(Integer, ForeignKey('users_form.id'), nullable=False)

def get_all_users():
    session = Session(engine)
    stmt = select(User)
    return session.scalars(stmt)


def create_user(name):
    with Session(engine) as session:
        user = User(name=name)
        session.add(user)
        session.commit()


def set_user_profile_picture_file_names(user_id, stored_file_name, provided_file_name):
    stmt = select(User).where(User.id == user_id)
    user = session.scalars(stmt).one()
    user.provided_file_name = provided_file_name
    user.stored_file_name = stored_file_name
    session.commit()


# ### old
# class Item(Base):
#     id = Column(Integer(),primary_key=True)
#     name = Column(String(length=30),nullable=False, unique=True)
#     price = Column(Integer(),nullable=False)
#     barcode = Column(String(length=12), nullable=False,unique=True)
#     description = Column(String(length=1024),nullable=False,unique=True)
#     owner = Column(Integer(),ForeignKey('user.id'))

# class weatherFLWTC(Base):
#     id = Column(Integer(), primary_key=True)
#     generalSituation = Column(String(length=200), nullable=False)
#     tcInfo = Column(String(length=200), nullable=True)
#     fireDangerWarning = Column(String(length=200), nullable=True)
#     forecastPeriod = Column(String(length=200), nullable=False)
#     forecastDesc = Column(String(length=1024), nullable=False)
#     outlook = Column(String(length=1024), nullable=False)
#     updateTime = Column(String(length=40), nullable=False)

# class weatherFNDTC(Base):
#     id = Column(Integer(), primary_key=True)
#     weatherForecast = Column(String(length=200), nullable=True)
#     forecastDate = Column(String(length=200), nullable=True)
#     forecastWeather = Column(String(length=200), nullable=True)
#     forecastMaxtemp = Column(String(length=200), nullable=True)
#     forecastMintemp = Column(String(length=200), nullable=True)
#     week = Column(String(length=200), nullable=True)
#     forecastWind = Column(String(length=200), nullable=True)
#     forecastMaxrh = Column(String(length=200), nullable=True)
#     forecastMinrh = Column(String(length=200), nullable=True)
#     ForecastIcon = Column(String(length=200), nullable=True)
#     PSR = Column(String(length=200), nullable=True)
#     soilTemp = Column(String(length=200), nullable=True)
#     seaTemp = Column(String(length=200), nullable=True)

# class weatherRHRREADTC(Base):
#     id = Column(Integer(), primary_key=True)
#     lightning = Column(String(length=200), nullable=True)
#     rainfall = Column(String(length=200), nullable=True)
#     icon = Column(String(length=200), nullable=True)
#     iconUpdateTime = Column(String(length=200), nullable=True)
#     uvindex = Column(String(length=200), nullable=True)
#     updateTime = Column(String(length=200), nullable=True)
#     warningMessage = Column(String(length=200), nullable=True)
#     rainstormReminder = Column(String(length=200), nullable=True)
#     specialWxTips = Column(String(length=200), nullable=True)
#     tcmessage = Column(String(length=200), nullable=True)
#     mintempFrom00To00 = Column(String(length=200), nullable=True)
#     rainfallFrom00To12 = Column(String(length=200), nullable=True)
#     rainfallLastMonth = Column(String(length=200), nullable=True)
#     rainfallJanuaryToLastMonth = Column(String(length=200), nullable=True)
#     temperature = Column(String(length=200), nullable=True)
#     humidity = Column(String(length=200), nullable=True)

# class weatherWARNSUMTC(Base):
#     id = Column(Integer(), primary_key=True)
#     name = Column(String(length=200), nullable=True)
#     code = Column(String(length=200), nullable=True)
#     actionCode = Column(String(length=200), nullable=True)
#     issueTime = Column(String(length=200), nullable=True)
#     expireTime = Column(String(length=200), nullable=True)
#     updateTime = Column(String(length=200), nullable=True)

# class weatherWarningInfoTC(Base):
#     id = Column(Integer(), primary_key=True)
#     details = Column(String(length=200), nullable=True)
#     contents = Column(String(length=200), nullable=True)
#     warningStatementCode = Column(String(length=200), nullable=True)
#     subtype = Column(String(length=200), nullable=True)
#     updateTime = Column(String(length=200), nullable=True)

# class weatherSMTTC(Base):
#     id = Column(Integer(), primary_key=True)
#     desc = Column(String(length=200), nullable=True)
#     updateTime = Column(String(length=200), nullable=True)