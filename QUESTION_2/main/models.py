from django.db import models

class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.street}, {self.city}"

class StaffBase(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    class Meta:
        abstract = True

class Manager(StaffBase):
    department = models.CharField(max_length=100)
    has_company_card = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.full_name} (Manager)"

class Intern(StaffBase):
    mentor = models.ForeignKey(Manager, on_delete=models.SET_NULL, null=True)
    internship_end = models.DateField()

    def __str__(self):
        return f"{self.full_name} (Intern)"
