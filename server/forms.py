# -*- coding: utf-8 -*-
from django import forms

from server.models import Occurrence


class FormContato(forms.Form):
    """
    Formulário de contato
    """
    nome = forms.CharField(max_length=120, widget=forms.TextInput(
        attrs={'class': 'input-contact', 'style': 'margin: 20px 0px 10px 0px;', 'placeholder': 'NOME'}))
    telefone = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'TELEFONE', 'id': 'telefoneContato', 'class': 'input-contact'}))
    email = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'E-MAIL', 'id': 'emailContato', 'class': 'input-contact', 'type': 'email'}))
    mensagem = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'SUA MENSAGEM', 'class': 'input-contact', 'style': 'height: 150px;'}))


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


class FormCadastro(forms.ModelForm):
    """
    Formulário de cadastro
    """

    class Meta:
        model = Occurrence
        fields = [
            'name',
            'email',
            'phone',
            'description',
            'traffic_ticket',
            'drivers_licence',
            'dut_copy'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {'placeholder': 'NOME', 'pattern': '[A-Za-zÁ-Úá-úÂ-û-â-û.çÃ-Õã-õ\s]+$', 'class': 'input-contact', 'required':'true'})
        self.fields['email'].widget.attrs.update(
            {'placeholder': 'E-MAIL', 'id': 'emailContato', 'class': 'input-contact', 'type': 'email'})
        self.fields['phone'].widget.attrs.update(
            {'placeholder': 'TELEFONE', 'id': 'telefoneContato', 'class': 'input-contact'})
        self.fields['description'].widget.attrs.update(
            {'placeholder': 'DESCRIÇÃO DA MULTA', 'class': 'input-contact', 'style': 'height: 150px;'})
        self.fields['traffic_ticket'].widget.attrs.update(
            {'id': 'chooseTicketFile'})
        self.fields['drivers_licence'].widget.attrs.update(
            {'id': 'chooseLicenseFile'})
        self.fields['dut_copy'].widget.attrs.update(
            {'id': 'chooseDutFile'})

