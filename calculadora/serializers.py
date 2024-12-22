from rest_framework import serializers
from .models import Aluno


class AlunoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'idade', 'matricula']


class CursoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Curso
        fields = ['id', 'nome', 'codigo', 'duracao']
