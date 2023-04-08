from djongo import models

SCHOOL_CHOICES = (
    ('Enviroment', 'SCHOOL OF ENVIRONMENT, GEOGRAPHY AND APPLIED ECONOMICS'),
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

# Staff = {

# }


class ResearchProgramm(models.Model):
    title = models.TextField()
    researcher = models.TextField()
    description = models.TextField()


class Price(models.Model):
    price = models.TextField()
    currency = models.TextField()
    
    class Meta:
        abstract = True

class Building(models.Model):
    buildingName = models.CharField(max_length=255)
    location = models.TextField()


class Asset(models.Model):
    registrationNumber = models.ObjectIdField()
    description = models.TextField()
    category = models.CharField(max_length=255)
    pieces = models.IntegerField()
    serialNumber = models.TextField()
    invoiceNumber = models.TextField()
    invoiceValue = models.EmbeddedField(model_container=Price,default=None)
    acquisitionValue = models.EmbeddedField(model_container=Price,default=None)
    taxValue = models.EmbeddedField(model_container=Price,default=None)
    supplier = models.TextField(max_length=255)
    building = models.ForeignKey("Building",on_delete=models.CASCADE)
    office = models.TextField()
    school = models.TextField(choices=SCHOOL_CHOICES)
    department = models.TextField(choices=DEPARTMENT_CHOICES)
    assetManager = models.TextField()
    changes_additions = models.TextField()
    researchProgramm = models.ForeignKey(
        ResearchProgramm, on_delete=models.CASCADE)
    invoiceURL = models.URLField()
    objects = models.DjongoManager()

    def __str__(self):
        return self.registrationNumber
