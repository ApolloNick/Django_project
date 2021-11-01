from django.contrib import admin
from .models import Movie, Person, Role, MovieImage


class DirectorInLine(admin.StackedInline):
    model = Movie
    fk_name = "director"
    verbose_name = "director"
    verbose_name_plural = "directors"
    extra = 1


class RoleInLine(admin.StackedInline):
    model = Role
    extra = 1
    autocomplete_fields = ("person", "movie")


class MovieImageInLine(admin.StackedInline):
    model = MovieImage
    extra = 1


class MovieAdmin(admin.ModelAdmin):
    inlines = [
        RoleInLine, MovieImageInLine
    ]
    list_display = ("title", "year", "rating")
    list_filter = ("rating",)
    fields = (
        (
            "title",
            "year"
        ),
        ("runtime", "rating"),
        "plot",
        "directors",
        "writers",
        "website",
    )
