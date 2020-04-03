from django.contrib import admin
from .models import publish_house
from .models import book
from .models import reader_book
from .models import comment
from .models import genre
from .models import country
from .models import author
# Register your models here.

admin.site.register(publish_house)
admin.site.register(book)
admin.site.register(reader_book)
admin.site.register(comment)
admin.site.register(genre)
admin.site.register(country)
admin.site.register(author)

