from django.contrib import admin
from .models import Book, Review, Favorite, History, Wishlist, ReadingHistory

admin.site.register(Book)
admin.site.register(Review)
admin.site.register(Favorite)
admin.site.register(History)
admin.site.register(Wishlist)
admin.site.register(ReadingHistory)
