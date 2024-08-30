from django.db import models

# Create your models here.
class Employee(models.Model) :
    #PK:
    empID = models.IntegerField(primary_key=True, unique=True, auto_created=True)
    #Attributes
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=14)
    email = models.EmailField()
	
    def __str__(self) :
        string = str(self.empID)
        return (string)

    class Meta:
        db_table = "employee"

class HeaderBlock(models.Model) :
    title = models.CharField(primary_key=True, max_length=15, unique=True)
    content = models.TextField()

    def __str__(self) :
        return (self.title)

    class Meta:
        db_table = "header_block"

class ContentType(models.Model) :
    title = models.CharField(primary_key=True, max_length=30, unique=True)

    def __str__(self) :
        return (self.title)

    class Meta:
        db_table = "content_type"


class CodeBlock(models.Model) :
    #Attributes
    title = models.CharField(primary_key=True, max_length=75, unique=True)
    content = models.TextField()
    #FK
    empID = models.ForeignKey(Employee, on_delete=models.DO_NOTHING)
    type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING)
    def __str__(self) :
        return (self.title)

    class Meta:
        db_table = "code_block"