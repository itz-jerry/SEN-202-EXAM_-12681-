from rest_framework import serializers
from .models import Manager, Intern

class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = ['id', 'full_name', 'email', 'department', 'has_company_card']
        read_only_fields = ['has_company_card']

class InternSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intern
        fields = ['id', 'full_name', 'email', 'mentor', 'internship_end']
