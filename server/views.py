from django.core.mail import send_mail
from django.views.generic import FormView
from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.permissions import BasePermission, IsAuthenticatedOrReadOnly, IsAuthenticated

from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.views import ObtainJSONWebToken

from server.forms import FormContato
from server.models import Occurrence, Post
from server.serializers import OccurrenceSerializer

SAFE_METHODS = ('POST', 'HEAD', 'OPTIONS')


def homeBlog(request):
    posts = Post.objects.all()
    return render(request, 'homeBlog.html', {'posts': posts})

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

class ContatoView(FormView):
    template_name = 'formContato.html'
    form_class = FormContato
    success_url = '/'

    print("AQUIIII")

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
        print()
        print(data['telefone'])
        print(data['email'])
        print(data['mensagem'])

        send_mail(
             '[CONTATO] - ZERANDO MULTAS - %s - %s' % (data['nome'], data['telefone']) ,
             data['mensagem'],
             data['email'],
             ['leo.cc14@gmail.com', 'betinho.fmn@gmail.com', 'zerandomultas@gmail.com'],
             fail_silently=False,
        )

        return super(ContatoView, self).form_valid(form)

    def form_invalid(self, form):
        print (form.errors)

