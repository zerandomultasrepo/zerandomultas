import os
from django.conf import settings
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail, EmailMessage
from django.views.generic import FormView
from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.permissions import BasePermission, IsAuthenticatedOrReadOnly, IsAuthenticated

from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.views import ObtainJSONWebToken

from server.forms import FormContato, FormCadastro, FormComment
from server.models import Occurrence, Post, Comment
from server.serializers import OccurrenceSerializer

SAFE_METHODS = ('POST', 'HEAD', 'OPTIONS')


def homeBlog(request):
    posts = Post.objects.all()
    return render(request, 'blog.html', {'posts': posts})


def depoimentos(request):
    posts = Post.objects.all()
    return render(request, 'depoimentos.html', {'posts': posts})


def post(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'postBlog.html', {'post': post})


class IsAuthenticatedOrCreate(BasePermission):
    """
    The request is authenticated as a user, or is a create request.
    """

    def has_permission(self, request, view):
        return (
                request.method in SAFE_METHODS or
                request.user and
                request.user.is_authenticated()
        )


class LoginView(ObtainJSONWebToken):
    """
    Allow the user login in system
    """


class OccurrenceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Occurrence.objects.all()
    serializer_class = OccurrenceSerializer
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticatedOrCreate,)


class OccurrenceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Occurrence.objects.all()
    serializer_class = OccurrenceSerializer
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticatedOrCreate,)


class ContatoView(SuccessMessageMixin, FormView):
    template_name = 'formContato.html'
    form_class = FormContato
    success_url = 'fale-conosco'

    def get_success_message(self, cleaned_data):
        return "Mensagem enviada com sucesso, em breve entraremos em contato."

    def post(self, request, *args, **kwargs):
        """
        Realiza tratamento da data antes da validação do formulário.
        """
        data = request.POST

        my_dict = {}
        for key in data:
            my_dict[key] = data[key]

        form = FormContato(my_dict)

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        """
        Este método adiciona uma nova atividade no banco de dados.
        """
        data = form.cleaned_data
        mensagem = "Nome: " + data['nome'] + "\n" + "Telefone: " + data['telefone'] + "\n" + "E-Mail: " + data['email']+ "\n\n" + "Mensagem: " + data['mensagem']
        send_mail(
            '[CONTATO] ZERANDO MULTAS - %s ' % (data['nome']),
            mensagem,
            data['email'],
            ['zerandomultas@gmail.com'],
            fail_silently=False,
        )

        return super(ContatoView, self).form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super(ContatoView, self).form_invalid(form)


class CadastroView(SuccessMessageMixin, FormView):
    template_name = 'formCadastro.html'
    form_class = FormCadastro
    success_url = 'cadastro'

    def get_success_message(self, cleaned_data):
        return "Cadastro realizado com sucesso, em breve entraremos em contato."

    def post(self, request, *args, **kwargs):
        """
        Realiza tratamento da data antes da validação do formulário.
        """
        data = request.POST

        my_dict = {}
        for key in data:
            my_dict[key] = data[key]
        print(request.FILES)
        form = FormCadastro(my_dict, request.FILES)

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        """
        Este método adiciona uma nova atividade no banco de dados.
        """
        data = form.cleaned_data

        if not Occurrence.objects.filter(email=data['email']).exists():
            form.save()
            return render(self.request, 'formCadastro.html',
                          {'form': form})
        else:
            occurence_obj = Occurrence.objects.filter(email=data['email']).last()
            if not occurence_obj.description:
                Occurrence.objects.filter(email=data['email']).last().delete()
            form.save()
        if 'description' in data.keys() and data['description']:
            message = "Nome: " + data['name'] + "\n" + "E-Mail: " + data['email'] + "\n" + "Telefone: " + data['phone'] + "\n\n" + "Descrição da multa: " + data['description']
            email = EmailMessage(subject='[OCORRENCIA] ZERANDO MULTAS - %s ' % (data['name']),
                                 body=message,
                                 from_email=data['email'],
                                 to=['zerandomultas@gmail.com'],
                                 headers={'Message-ID': 'Ocorrencia'}, )

            if ('traffic_ticket' in data.keys() and data['traffic_ticket']):
                trafic_ticket = data['traffic_ticket'].name.replace(" ", "_")
                email.attach_file(
                    os.path.join(settings.MEDIA_ROOT, 'ocorrencia/' + data['email'] + '/' + trafic_ticket))
            if ('drivers_licence' in data.keys() and data['drivers_licence']):
                drivers_licence = data['drivers_licence'].name.replace(" ", "_")
                email.attach_file(
                    os.path.join(settings.MEDIA_ROOT, 'ocorrencia/' + data['email'] + '/' + drivers_licence))
            if ('dut_copy' in data.keys() and data['dut_copy']):
                dut_copy = data['dut_copy'].name.replace(" ", "_")
                email.attach_file(os.path.join(settings.MEDIA_ROOT, 'ocorrencia/' + data['email'] + '/' + dut_copy))

            email.send()

            return super(CadastroView, self).form_valid(form)
        else:
            return render(self.request, 'formCadastro.html',
                          {'form': form})

    def form_invalid(self, form):
        print(form.errors)
        return super(CadastroView, self).get(form)


class CommentView(SuccessMessageMixin, FormView):
    template_name = 'depoimentos.html'
    form_class = FormComment
    success_url = 'depoimentos'

    def get_success_message(self, cleaned_data):
        return "Depoimento enviado com sucesso, passando por avaliação do mediador."

    def get(self, request, *args, **kwargs):
        comments = Comment.objects.all()
        form = FormComment()
        return render(request, 'depoimentos.html', {'comments': comments, 'form': form})

    def post(self, request, *args, **kwargs):
        """
        Realiza tratamento da data antes da validação do formulário.
        """
        data = request.POST
        print(request.POST)
        my_dict = {}
        for key in data:
            my_dict[key] = data[key]

        form = FormComment(my_dict)

        if form.is_valid():
            mensagem = "Nome: " + data['name'] + "\n" + "E-Mail: " + data['email']+ "\n\n" + "Depoimento: " + data['comment']
            send_mail(
                '[DEPOIMENTO] ZERANDO MULTAS - %s ' % (data['name']),
                mensagem,
                data['email'],
                ['zerandomultas@gmail.com'],
            fail_silently=False,
        )
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        """
        Este método adiciona uma nova atividade no banco de dados.
        """
        form.save()
        return super(CommentView, self).form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        comments = Comment.objects.all()
        return render(self.request, 'depoimentos.html',
                      {'form': form, 'comments': comments})
