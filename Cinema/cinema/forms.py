from django import forms
from cinema.models import Filme, Sessao, Ingresso

SESSAO_CHOICES = (
    ('m', 'Manha'),
    ('t', 'Tarde'),
    ('n', 'Noite')
)

class FilmeForm(forms.ModelForm):
    class Meta:
        model = Filme
        fields = ['nomeFilme', 'duracao', 'genero']

class SessaoForm(forms.ModelForm):
    class Meta:
        model = Sessao
        fields = ['horarios', 'periodo']
        #Sessao = forms.ChoiceField(choices=SESSAO_CHOICES)

class IngressoForm(forms.ModelForm):
    class Meta:
        model = Ingresso
        fields = ['meio', 'inteira', 'fisico', 'online']