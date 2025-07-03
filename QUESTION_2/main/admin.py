from django.contrib import admin
from .models import Manager, Intern, Address

admin.site.register(Manager)
admin.site.register(Intern)
admin.site.register(Address)

# Superuser Credentials
# Username: Jerry
# Email: jerry@gmail.com
# Password: Jerry12345
