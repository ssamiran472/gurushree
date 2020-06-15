from .serializers import GenTypeSerializer, SubDepartmentsListSerializer, DepartmentSerializer, CitiesListSerializer, SubDepartmentSerializer, GeneralTypeSerializer, registrationTypeSerializer, discounTypeSerializer, userSerializer, income_expensesSerializer, hospitalSerializer, professionalSerializer, menuSerializer, pagemasterSerializer, StateSerializer, AreaSerializer, CitySerializer
from .models import GenType, Department, SubDepartment, generalType, registrationType, discounType, user, income_expenses, hospital, professional, menu, pagemaster, State, City, Area
from rest_framework import viewsets, permissions, mixins


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = DepartmentSerializer


class SubDepartmentViewSet(viewsets.ModelViewSet):
    queryset = SubDepartment.objects.all()
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = SubDepartmentSerializer


class GeneralTypeViewSet(viewsets.ModelViewSet):
    #queryset = generalType.objects.all()
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = GeneralTypeSerializer

    def get_queryset(self):
        queryset = generalType.objects.all()
        gentype = self.request.query_params.get('gentype', None)
        if gentype is not None:
            queryset = queryset.filter(genType=gentype)
        return queryset


class registrationTypeViewSet(viewsets.ModelViewSet):
    queryset = registrationType.objects.all()
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = registrationTypeSerializer


class discounTypeViewSet(viewsets.ModelViewSet):
    queryset = discounType.objects.all()
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = discounTypeSerializer


class userViewSet(viewsets.ModelViewSet):
    queryset = user.objects.all()
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = userSerializer


class income_expensesViewSet(viewsets.ModelViewSet):
    queryset = income_expenses.objects.all()
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = income_expensesSerializer


class hospitalViewSet(viewsets.ModelViewSet):
    queryset = hospital.objects.all()
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = hospitalSerializer


class professionalViewSet(viewsets.ModelViewSet):
    queryset = professional.objects.all()
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = professionalSerializer


class menuViewSet(viewsets.ModelViewSet):
    queryset = menu.objects.all()
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = menuSerializer


class pagemasterViewSet(viewsets.ModelViewSet):
    queryset = pagemaster.objects.all()
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = pagemasterSerializer


class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = StateSerializer


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = CitySerializer


class AreaViewSet(viewsets.ModelViewSet):
    queryset = Area.objects.all()
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = AreaSerializer


class CitiesListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = City.objects.all()
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = CitiesListSerializer

class SubdepartmentsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = SubDepartment.objects.all()
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = SubDepartmentsListSerializer

class GenTypeViewSet(viewsets.ModelViewSet):
    queryset=GenType.objects.all()
    permissions = [
        permissions.AllowAny
    ]
    serializer_class =GenTypeSerializer
