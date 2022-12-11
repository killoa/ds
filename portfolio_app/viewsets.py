from rest_framework import viewsets
from .models import User,Biography,ProfessionalAccomplishement,Awards,licenses,Volunteering,References,Portfolio
from .serializers import UserSerializer,BiographySerializer,ProfessionalAccomplishementSerializer,AwardsSerializer,licensesSerializer,VolunteeringSerializer,ReferencesSerializer,PortfolioSerializer

class UserViewSet (viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    http_method_name=['get','post','put','delete']

class BiographyViewSet (viewsets.ModelViewSet):
    queryset=Biography.objects.all()
    serializer_class=BiographySerializer
    http_method_name=['get','post','put','delete']

class ProfessionalAccomplishementViewSet (viewsets.ModelViewSet):
    queryset=ProfessionalAccomplishement.objects.all()
    serializer_class=ProfessionalAccomplishementSerializer
    http_method_name=['get','post','put','delete']

class AwardsViewSet (viewsets.ModelViewSet):
    queryset=Awards.objects.all()
    serializer_class=AwardsSerializer
    http_method_name=['get','post','put','delete']

class licensesViewSet (viewsets.ModelViewSet):
    queryset=licenses.objects.all()
    serializer_class=licensesSerializer
    http_method_name=['get','post','put','delete']

class VolunteeringViewSet (viewsets.ModelViewSet):
    queryset=Volunteering.objects.all()
    serializer_class=VolunteeringSerializer
    http_method_name=['get','post','put','delete']

class ReferencesViewSet (viewsets.ModelViewSet):
    queryset=References.objects.all()
    serializer_class=ReferencesSerializer
    http_method_name=['get','post','put','delete']

class PortfolioViewSet (viewsets.ModelViewSet):
    queryset=Portfolio.objects.all()
    serializer_class=PortfolioSerializer
    http_method_name=['GET','post','put','DELETE']

