from rest_framework import viewsets
from myapi.serializers import reader_bookSerializer
from myapi.models import reader_book
from myapi.serializers import publish_houseSerializer
from myapi.models import publish_house
from myapi.serializers import bookSerializer
from myapi.models import book
from myapi.serializers import commentSerializer
from myapi.models import comment
from myapi.serializers import genreSerializer
from myapi.models import genre
from myapi.serializers import authorSerializer
from myapi.models import author
from myapi.serializers import countrySerializer
from myapi.models import country
from rest_framework.permissions import AllowAny

from api.models import User
from api.serializers import UserSerializer

from myapi.permissions import IsLoggedInUserOrAdmin, IsAdminUser, IsAutorizateUser 


class publish_houseViewSet(viewsets.ModelViewSet):
    queryset = publish_house.objects.all()
    serializer_class = publish_houseSerializer

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [IsAdminUser]
        elif self.action == 'destroy' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsAdminUser]
        elif self.action == 'list' or self.action == 'retrieve':
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]
class genreViewSet(viewsets.ModelViewSet):
    queryset = genre.objects.all().order_by('name')
    serializer_class = genreSerializer

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [IsAdminUser]
        elif self.action == 'destroy' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsAdminUser]
        elif self.action == 'list' or self.action == 'retrieve':
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]		
class bookViewSet(viewsets.ModelViewSet):
    queryset = book.objects.all().order_by('name')
    serializer_class = bookSerializer

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [IsAdminUser]
        elif self.action == 'destroy' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsAdminUser]
        elif self.action == 'list' or self.action == 'retrieve':
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]
		
class reader_bookViewSet(viewsets.ModelViewSet):
    queryset = reader_book.objects.all()
    serializer_class = reader_bookSerializer
    def get_queryset(self):
        return reader_book.objects.all().filter(reader=self.request.user)     
    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [IsAutorizateUser]
        elif self.action == 'destroy' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsAdminUser]
        elif self.action == 'retrieve':
            permission_classes = [IsAutorizateUser]
        elif self.action == 'list' or self.action == 'retrieve':
            permission_classes = [IsAutorizateUser]		
        return [permission() for permission in permission_classes]	
		
class commentViewSet(viewsets.ModelViewSet):
    queryset = comment.objects.all()
    serializer_class = commentSerializer
    def get_queryset(self):
        return comment.objects.all().filter(reader=self.request.user)     
    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [IsAutorizateUser]
        elif self.action == 'destroy' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsAdminUser]
        elif self.action == 'retrieve':
            permission_classes = [IsAutorizateUser]
        elif self.action == 'list' or self.action == 'retrieve':
            permission_classes = [IsAutorizateUser]		
        return [permission() for permission in permission_classes]	

class authorViewSet(viewsets.ModelViewSet):
    queryset = author.objects.all().order_by('nickname')
    serializer_class = authorSerializer

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [IsAdminUser]
        elif self.action == 'destroy' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsAdminUser]
        elif self.action == 'list' or self.action == 'retrieve':
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]	


class countryViewSet(viewsets.ModelViewSet):
    queryset = country.objects.all()
    serializer_class = countrySerializer

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [IsAdminUser]
        elif self.action == 'destroy' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsAdminUser]
        elif self.action == 'list' or self.action == 'retrieve':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]	
		


