from django.contrib import admin
from .models import Draw,DrawBets, Users, Numbers


@admin.register(Draw)
class DrawAdmin(admin.ModelAdmin):
    list_display = ('id', 'block_number', 'winner_number', 'status', 'members_number', 'created_at')

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('id','user_id', 'first_name', 'user_name', 'language_code', 'language_bot', 'created_at', 'count_visits')


@admin.register(DrawBets)
class DrawBetsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'draw_id')

# admin.site.register(Numbers)


# Register your models here.
