from rest_framework import routers
from .viewsets import UserViewSet,BiographyViewSet,ProfessionalAccomplishementViewSet,AwardsViewSet,licensesViewSet,VolunteeringViewSet,ReferencesViewSet,PortfolioViewSet
from django.urls import path,include

router=routers.DefaultRouter()

router.register(r'User',UserViewSet)
router.register(r'Biography',BiographyViewSet)
router.register(r'ProfessionalAccomplishement',ProfessionalAccomplishementViewSet)
router.register(r'Awards',AwardsViewSet)
router.register(r'licenses',licensesViewSet)
router.register(r'Volunteering',VolunteeringViewSet)
router.register(r'References',ReferencesViewSet)
router.register(r'Portfolio',PortfolioViewSet)

urlpatterns=[
    path('',include(router.urls))

]