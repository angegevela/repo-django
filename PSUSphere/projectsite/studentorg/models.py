from django.db import models

# Create your models here.
class BaseModels(models.Model):
    created_at = models.DateTimeField(auto_now=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class College(BaseModels):
    college_name = models.CharField(max_length=150)

    def __str__(self):
        return self.college_name


class Program(BaseModels):
    prog_name = models.CharField(max_length=150)
    college = models.ForeignKey(College, on_delete=models.CASCADE)

    def __str__(self):
        return self.prog_name

class Organization(BaseModels):  # Inherit from BaseModels to include timestamps
    name = models.CharField(max_length=150)
    college = models.ForeignKey(College, blank=True, on_delete=models.CASCADE)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Student(BaseModels):
    student_id = models.CharField(max_length=15)
    lastname = models.CharField(max_length=25)
    firstname = models.CharField(max_length=25)
    middlename = models.CharField(max_length=25, blank=True, null=True)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.lastname},{self.firstname}"
    
class OrgMember(BaseModels):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    date_joined = models.DateField()