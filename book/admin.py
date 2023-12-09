from django.contrib import admin
from book.models import BookName,BookCategory,PublisherCategory,Author

# Register your models here.



admin.site.register(BookName)
admin.site.register(BookCategory)
admin.site.register(PublisherCategory)
admin.site.register(Author)

