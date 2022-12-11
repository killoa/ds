from rest_framework import serializers
from .models import User,Biography,ProfessionalAccomplishement,Awards,licenses,Volunteering,References,Portfolio

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'

class BiographySerializer(serializers.ModelSerializer):
    class Meta:
        model=Biography
        fields='__all__'

class ProfessionalAccomplishementSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProfessionalAccomplishement
        fields='__all__'

class AwardsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Awards
        fields='__all__'

class licensesSerializer(serializers.ModelSerializer):
    class Meta:
        model=licenses
        fields='__all__'

class VolunteeringSerializer(serializers.ModelSerializer):
    class Meta:
        model=Volunteering
        fields='__all__'

class ReferencesSerializer(serializers.ModelSerializer):
    class Meta:
        model=References
        fields='__all__'

class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model=Portfolio
        fields='__all__'

