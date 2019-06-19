from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, ArticleScope


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        counter = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main'):
                counter += 1
            if counter > 1:
                raise ValidationError('Слишком много базовых тегов')
            elif counter < 1:
                raise ValidationError('Слишком мало базовых тегов')

        return super().clean()


class RelationshipInline(admin.TabularInline):
    model = ArticleScope
    formset = RelationshipInlineFormset
    extra = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = (RelationshipInline,)


@admin.register(Scope)
class ObjectAdmin(admin.ModelAdmin):
    inlines = (RelationshipInline,)
