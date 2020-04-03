from rest_framework import serializers
from .models import reader_book
from .models import publish_house
from .models import genre
from .models import book
from .models import comment
from .models import author
from .models import country

class countrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = country
        fields = ('__all__')
		
class publish_houseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = publish_house
        fields = ('name', 'address', 'contact_person')
		
class authorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = author
        fields = ('first_name', 'last_name', 'nickname', 'born_date', 'death_date', 'country' )
		
class genreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = genre
        fields = ('name', 'description')
		
class bookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = book
        fields = ('name', 'publish_house', 'year', 'image', 'file', 'page', 'description_of_book', 'genre', 'author')
		
class reader_bookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = reader_book
        fields = ('rating', 'upload_date', 'status', 'reader', 'book')
		
class commentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = comment
        fields = ('posted', 'comment', 'reader', 'book')
