from djongo import models

SCHOOL_CHOICES = (
    ('Environment', 'SCHOOL OF ENVIRONMENT, GEOGRAPHY AND APPLIED ECONOMICS'),
    ('Digital', 'SCHOOL OF DIGITAL TECHNOLOGY'),
    ('Health', 'SCHOOL OF HEALTH SCIENCE AND EDUCATION'),
)


DEPARTMENT_CHOICES = (
    ('Economics', 'Economics and Sustainable Development'),
    ('Geography', 'Geography'),
    ('Tourism', 'International Master of Sustainable Tourism Development'),
    ('Informatics', 'Informatics and Telematics'),
    ('Dietetics', 'Nutrition and Dietetics'),

)


class ResearchProgram(models.Model):
    _id = models.ObjectIdField()
    title = models.TextField()
    researcher = models.TextField()
    description = models.TextField()


class Price(models.Model):
    _id = models.ObjectIdField()
    value = models.TextField()
    currency = models.TextField()

    class Meta:
        abstract = True


class Building(models.Model):
    _id = models.ObjectIdField()
    building_name = models.CharField(max_length=255)
    location = models.TextField()


class Asset(models.Model):
    _id = models.ObjectIdField()
    registration_number = models.TextField()
    description = models.TextField()
    category = models.CharField(max_length=255)
    pieces = models.IntegerField()
    serial_number = models.TextField()
    invoice_number = models.TextField()
    invoice_value = models.EmbeddedField(model_container=Price, default=None)
    acquisition_value = models.EmbeddedField(model_container=Price,
                                             default=None)
    tax_value = models.EmbeddedField(model_container=Price, default=None)
    supplier = models.TextField(max_length=255)
    building = models.EmbeddedField(model_container=Building, default=None)
    office = models.TextField()
    school = models.TextField(choices=SCHOOL_CHOICES)
    department = models.TextField(choices=DEPARTMENT_CHOICES)
    asset_manager = models.TextField()
    changes_additions = models.TextField()
    research_program = models.EmbeddedField(model_container=ResearchProgram,
                                            default=None)
    invoice_url = models.URLField()
    user_id = models.TextField()
    objects = models.DjongoManager()

    def __str__(self):
        return self.registrationNumber
