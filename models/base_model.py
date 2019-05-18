import os
import peewee as pw
import datetime
from database import db

class BaseModel(pw.Model):
    created_at = pw.DateTimeField(default=datetime.datetime.now)
    updated_At = pw.DateTimeField(default=datetime.datetime.now)

    def save(self, *args, **kwargs):
        self.errors = []
        self.validate()

        if len(self.errors) == 0:
            self.updated_at = datetime.datetime.now()
            return super(BaseModel, self).save(*args, **kwargs)
        else:
            return 0

    def validate(self):
        # Validation to be done here
        return True
    
    class Meta:
        database = database
        legacy_table_names = False