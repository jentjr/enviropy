from peewee import *

db = SqliteDatabase(DATABASE)

def before_request_handler():
    db.connect()

def after_request_handler():
    db.close()

class BaseModel(Model):
    class Meta:
        database = db

class WaterQuality(BaseModel):
    site = Charfield()
    sample_campaign = TextField()
    lab_id = TextField()
    sample_id = CharField()
    sample_date = DateField()
    param_name = TextField()
    method_name = TextField()
    analysis_result = DoubleField()
    qualifier_flags = TextField()
    detection_limit = FloatField()
    reporting_limit = FloatField()
    practical_quantitation_limit = NumericField()
    measure_unit = TextField()
    analysis_date = DateField()
    sample_comments = TextField()
    results_comments = TextField()

    class Meta:
        database = db

class WellConstruction(BaseModel):
    site() = CharField

