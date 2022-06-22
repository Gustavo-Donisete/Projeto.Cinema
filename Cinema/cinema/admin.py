from django.contrib import admin
from .models import Filme, Sessao, Ingresso, Ator, Sala, Tipo

# Register your models here.

admin.site.register(Filme)
admin.site.register(Sala)
admin.site.register(Sessao)
admin.site.register(Ingresso)
admin.site.register(Ator)
admin.site.register(Tipo)