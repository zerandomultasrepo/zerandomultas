# -*- coding: utf-8 -*-
from django import forms


class FormContato(forms.Form):
    """
    Formulário de contato
    """
    nome = forms.CharField(max_length=120, widget=forms.TextInput(attrs={'class': 'input-contact', 'style':'margin: 20px 0px 10px 0px;', 'placeholder':  'NOME' }))
    telefone = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'TELEFONE', 'id':'telefoneContato', 'class': 'input-contact' }))
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'E-MAIL', 'id':'emailContato', 'class': 'input-contact', 'type':'email' }))
    mensagem = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'SUA MENSAGEM', 'class':'input-contact', 'style':'height: 150px;'}))


PLAN_SELECTION = (
    (0, ("ESCOLHA SEU PLANO")),
    (1, "Leve"),
    (2, "Média"),
    (3, "Grave"),
    (4, "Gravíssima"),
    (5, "Gravíssima (2x)"),
    (6, "Gravíssima (3x)"),
    (7, "Gravíssima (5x)"),
    (8, "Gravíssima (10x)"),
    (9, "Gravíssima (20x)"),
    (10, "Gravíssima (60x)")
)


class FormCadastro(forms.Form):
    """
    Formulário de cadastro
    """
    nome = forms.CharField(max_length=120, widget=forms.TextInput(
        attrs={'placeholder':'NOME', 'pattern':'[A-Za-zÁ-Úá-úÂ-û-â-û.çÃ-Õã-õ\s]+$', 'class':'input-contact'}))
    email = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'E-MAIL', 'id': 'emailContato', 'class': 'input-contact', 'type': 'email'}))
    telefone = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'TELEFONE', 'id': 'telefoneContato', 'class': 'input-contact'}))
    plan_selection = forms.ChoiceField(choices = PLAN_SELECTION, label="plan_selection", initial='0', widget=forms.Select(attrs={'class':'custom-select input-contact', 'id':'plainSelect'}), required=True)
    descricao = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'DESCRIÇÃO DA MULTA', 'class': 'input-contact', 'style': 'height: 150px;'}))

    """
    <select class="custom-select input-contact" name="plan_selection" id="plainSelect"><option value="0" selected="">ESCOLHA SEU PLANO</option><option value="1">Leve</option>
                                        <option value="2">Média</option><option value="3">Grave</option><option value="4">Gravíssima</option><option value="5">Gravíssima (2x)</option><option value="6">Gravíssima (3x)</option>
                                        <option value="7">Gravíssima (5x)</option><option value="8">Gravíssima (10x)</option><option value="9">Gravíssima (20x)</option><option value="10">Gravíssima (60x)</option></select>
    """