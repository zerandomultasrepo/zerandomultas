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
