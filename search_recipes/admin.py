from django.contrib import admin
from .models import RecipeList, RecipeIngredient, RecipeContent2, IngredientList

# Register your models here.
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('recipe_name', 'source', 'url','recipe_type','taste','category','rank')

class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display = ('recipe_name', 'qty', 'amount','unit','ingredient','recipe_type','source','taste','category')

class RecipeContentAdmin(admin.ModelAdmin):
    list_display = ('recipe_name', 'content', 'recipe_type','taste','category')

class IngredientListAdmin(admin.ModelAdmin):
    list_display = ('id','ingredient_name')
    

admin.site.register(RecipeList,RecipeAdmin)
admin.site.register(RecipeIngredient,RecipeIngredientAdmin)
admin.site.register(RecipeContent2,RecipeContentAdmin)
admin.site.register(IngredientList,IngredientListAdmin)