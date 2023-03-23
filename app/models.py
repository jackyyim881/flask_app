from app import app , db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin
from wtforms import PasswordField
from wtforms.validators import Length

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"



class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer(),primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=50),nullable=False, unique=True)
    password1 = PasswordField(label='Password:', validators=[Length(min=6)])
    password_hash = db.Column(db.String(length=60), nullable=False)
    budget = db.Column(db.Integer(),nullable=False, default=1000)
    items = db.relationship('Item', backref='owned_user', lazy=True)
    


    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


class Item(db.Model):
    __tablename__ = "items"
    id = db.Column(db.Integer(),primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.String(length=50),nullable=False, unique=True)
    description = db.Column(db.String(length=100),nullable=False, unique=False)
    owner = db.Column(db.String(length=30), nullable=False, unique=False)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'), nullable=False)
    
class weatherFLWTC(db.Model):
    __tablename__ = "weatherFLWTC"
    id = db.Column(db.Integer(),primary_key=True)
    generalSituation = db.Column(db.String(length=30), nullable=False, unique=True)
    tcInfo = db.Column(db.String(length=50),nullable=False, unique=True)
    fireDangerWarning = db.Column(db.String(length=100),nullable=False, unique=False)
    forecastPeriod = db.Column(db.String(length=30), nullable=False, unique=False)
    forecastDesc = db.Column(db.String(length=30), nullable=False, unique=False)
    outlook = db.Column(db.String(length=30), nullable=False, unique=False)
    updateTime = db.Column(db.String(length=30), nullable=False, unique=False)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'), nullable=False)

class weatherFNDTC(db.Model):
    __tablename__ = "weatherFNDTC"
    id = db.Column(db.Integer(),primary_key=True)
    weatherForecast = db.Column(db.String(length=30), nullable=False, unique=True)
    forecastDate = db.Column(db.String(length=50),nullable=False, unique=True)
    forecastWeather = db.Column(db.String(length=100),nullable=False, unique=False)
    forecastMaxtemp = db.Column(db.String(length=30), nullable=False, unique=False)
    forecastMintemp = db.Column(db.String(length=30), nullable=False, unique=False)
    week = db.Column(db.String(length=30), nullable=False, unique=False)
    forecastWind = db.Column(db.String(length=30), nullable=False, unique=False)
    forecastMaxrh = db.Column(db.String(length=30), nullable=False, unique=False)
    forecastMinrh = db.Column(db.String(length=30), nullable=False, unique=False)
    ForecastIcon = db.Column(db.String(length=30), nullable=False, unique=False)
    PSR = db.Column(db.String(length=30), nullable=False, unique=False)
    soilTemp = db.Column(db.String(length=30), nullable=False, unique=False)
    seaTemp = db.Column(db.String(length=30), nullable=False, unique=False)

class weatherRHREADTC(db.Model):
    __tablename__ = "weatherRHREADTC"
    id = db.Column(db.Integer(),primary_key=True)
    lightning = db.Column(db.String(length=30), nullable=False, unique=True)
    rainfall = db.Column(db.String(length=30), nullable=False, unique=True)
    icon = db.Column(db.String(length=30), nullable=False, unique=True)
    iconUpdateTime = db.Column(db.String(length=30), nullable=False, unique=True)
    uvindex = db.Column(db.String(length=30), nullable=False, unique=True)
    UpdateTime = db.Column(db.String(length=30), nullable=False, unique=True)
    warningMessage = db.Column(db.String(length=30), nullable=False, unique=True)
    rainstormReminder = db.Column(db.String(length=30), nullable=False, unique=True)
    specialWxTips = db.Column(db.String(length=30), nullable=False, unique=True)
    tcmessage = db.Column(db.String(length=30), nullable=False, unique=True)
    mintempFrom00To0 = db.Column(db.String(length=30), nullable=False, unique=True)
    rainfallFrom00To12 = db.Column(db.String(length=30), nullable=False, unique=True)
    rainfallLastMonth = db.Column(db.String(length=30), nullable=False, unique=True)
    rainfallJanuaryToLas = db.Column(db.String(length=30), nullable=False, unique=True)
    tMonth = db.Column(db.String(length=30), nullable=False, unique=True)
    temperature = db.Column(db.String(length=30), nullable=False, unique=True)
    humidity = db.Column(db.String(length=30), nullable=False, unique=True)

class weatherWARNSUMTC(db.Model):
    __tablename__ = "weatherWARNSUMTC"
    id = db.Column(db.Integer(),primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    code = db.Column(db.String(length=30), nullable=False, unique=True)
    actioncode = db.Column(db.String(length=30), nullable=False, unique=True)
    issueTime = db.Column(db.String(length=30), nullable=False, unique=True)
    expireTime = db.Column(db.String(length=30), nullable=False, unique=True)
    updateTime = db.Column(db.String(length=30), nullable=False, unique=True)

class weatherWarmingInfoTC(db.Model):
    __tablename__ = "weatherWarmingInfoTC"
    id = db.Column(db.Integer(),primary_key=True)
    details = db.Column(db.String(length=30), nullable=False, unique=True)
    contents = db.Column(db.String(length=30), nullable=False, unique=True)
    warningStatementCode = db.Column(db.String(length=30), nullable=False, unique=True)
    subtype = db.Column(db.String(length=30), nullable=False, unique=True)
    updateTime = db.Column(db.String(length=30), nullable=False, unique=True)

class earthquakeQEMTC(db.Model):
    __tablename__ = "earthquakeQEMTC"
    id = db.Column(db.Integer(),primary_key=True)
    latitude = db.Column(db.String(length=30), nullable=False, unique=True)
    ion = db.Column(db.String(length=30), nullable=False, unique=True)
    region = db.Column(db.String(length=30), nullable=False, unique=True)
    ptime = db.Column(db.String(length=30), nullable=False, unique=True)
    updateTime = db.Column(db.String(length=30), nullable=False, unique=True)

class feltearthquakeTC(db.Model):
    __tablename__ = "feltearthquakeTC"
    id = db.Column(db.Integer(),primary_key=True)
    updateTime = db.Column(db.String(length=30), nullable=False, unique=True)
    mag = db.Column(db.String(length=30), nullable=False, unique=True)
    region = db.Column(db.String(length=30), nullable=False, unique=True)
    lat = db.Column(db.String(length=30), nullable=False, unique=True)
    ion = db.Column(db.String(length=30), nullable=False, unique=True)
    ptime = db.Column(db.String(length=30), nullable=False, unique=True)
    details = db.Column(db.String(length=30), nullable=False, unique=True)

class Hikes(db.Model):
    __tablename__ = "Hikes"
    hike_id = db.Column(db.Integer(),primary_key=True)
    trail_name = db.Column(db.String(length=30), nullable=False, unique=True)
    location = db.Column(db.String(length=30), nullable=False, unique=True)
    distance = db.Column(db.String(length=30), nullable=False, unique=True)
    difficulty_level = db.Column(db.String(length=30), nullable=False, unique=True)
    estimated_time_of_completion = db.Column(db.String(length=30), nullable=False, unique=True)

class Trailhead(db.Model):
    __tablename__ = "Trailhead"
    trailhead_id = db.Column(db.Integer(),primary_key=True)
    location = db.Column(db.String(length=30), nullable=False, unique=True)
    parking_availability = db.Column(db.String(length=30), nullable=False, unique=True)
    hike_id = db.Column(db.Integer(), db.ForeignKey('users.id'), nullable=False)

class Reviews(db.Model):
    __tablename__ = "Reviews"
    review_id = db.Column(db.Integer(),primary_key=True)
    review = db.Column(db.String(length=30), nullable=False, unique=True)
    rating = db.Column(db.String(length=30), nullable=False, unique=True)
    review_text = db.Column(db.String(length=30), nullable=False, unique=True)
    hike_id = db.Column(db.Integer(), db.ForeignKey('users.id'), nullable=False)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'), nullable=False)

class Track(db.Model):
    __tablename__ = "Track"
    track_id = db.Column(db.Integer(),primary_key=True)
    hike_id = db.Column(db.Integer(), db.ForeignKey('users.id'), nullable=False)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'), nullable=False)
    coordinates = db.Column(db.String(length=30), nullable=False, unique=True)
    time_and_date = db.Column(db.String(length=30), nullable=False, unique=True)

class Images(db.Model):
    __tablename__ = "Images"
    image_id = db.Column(db.Integer(),primary_key=True)
    hike_id = db.Column(db.Integer(), db.ForeignKey('users.id'), nullable=False)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'), nullable=False)
    image = db.Column(db.String(length=30), nullable=False, unique=True)

class Emergency_Contacts(db.Model):
    __tablename__ = "Emergency_Contacts"
    contact_id = db.Column(db.Integer(),primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'), nullable=False)
    contact_name = db.Column(db.String(length=30), nullable=False, unique=True)
    contact_number = db.Column(db.String(length=30), nullable=False, unique=True)
    relationship = db.Column(db.String(length=30), nullable=False, unique=True)
class Weather(db.Model):
    __tablename__ = "Weather"
    weather_id = db.Column(db.Integer(),primary_key=True)
    hike_id = db.Column(db.Integer(), db.ForeignKey('users.id'), nullable=False)
    date = db.Column(db.String(length=30), nullable=False, unique=True)
    temperature = db.Column(db.String(length=30), nullable=False, unique=True)
    precipitation = db.Column(db.String(length=30), nullable=False, unique=True)
    wind_speed = db.Column(db.String(length=30), nullable=False, unique=True)

class Categories(db.Model):
    __tablename__ = "Categories"
    category_id = db.Column(db.Integer(),primary_key=True)
    category_name = db.Column(db.String(length=30), nullable=False, unique=True)
    category_description = db.Column(db.String(length=30), nullable=False, unique=True)
    hike_id = db.Column(db.Integer(), db.ForeignKey('users.id'), nullable=False)

class Posts(db.Model):
    __tablename__ = "Posts"
    post_id = db.Column(db.Integer(),primary_key=True)
    thread_id = db.Column(db.Integer(), db.ForeignKey('users.id'), nullable=False)
    date_created = db.Column(db.String(length=30), nullable=False, unique=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'), nullable=False)
    category_id = db.Column(db.Integer(), db.ForeignKey('users.id'), nullable=False)

class Threads(db.Model):
    __tablename__ = "Threads"
    thread_id = db.Column(db.Integer(),primary_key=True)
    title = db.Column(db.String(length=30), nullable=False, unique=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'), nullable=False)
    date_created = db.Column(db.String(length=30), nullable=False, unique=True)
    num_replies = db.Column(db.String(length=30), nullable=False, unique=True)

class Moderators(db.Model):
    __tablename__ = "Moderators"
    moderator_id = db.Column(db.Integer(),primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'), nullable=False)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    email = db.Column(db.String(length=30), nullable=False, unique=True)
    phone_number = db.Column(db.String(length=30), nullable=False, unique=True)
    
with app.app_context():
    db.create_all()
# class UserModel(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(80), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     password = db.Column(db.String(120))

#     def __init__(self, name, email, password):
#         self.name = name
#         self.email = email
#         self.password = password