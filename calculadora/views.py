from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path
from calculadora import views

def index(request):
          return render(request, 'calculadora/index.html')

def home(request):
          return render(request, 'calculadora//home.html')  

def soma(request):
          try:
              num1 = int(request.POST.get('num1'))
              num2 = int(request.POST.get('num2'))

              # Realiza o cálculo
              resultado = num1 + num2

              # Renderiza o resultado
              return render(request, 'calculadora/soma.html', {'num1': num1, 'num2': num2, 'resultado': resultado})

          except (TypeError, ValueError):
              return HttpResponse("Por favor, insira valores numéricos válidos.")
          
          except ZeroDivisionError:
              return HttpResponse("Erro: Não é possível dividir por zero.")

    # Função para divisão
    
def divisao(request):
    if request.method == 'POST':
        try:
            num1 = int(request.POST['num1'])
            num2 = int(request.POST['num2'])
            if num2 == 0:
                resultado = "Não é possível dividir por zero!"
            else:
                resultado = num1 / num2
        except (ValueError, KeyError):
            resultado = "Erro nos dados fornecidos!"
    else:
        resultado = None

    return render(request, 'calculadora/divisao.html', {'num1': num1, 'num2': num2, 'resultado': resultado})


def subtrair(request):
    resultado = None
    if request.method == 'POST':
        try:
            num1 = int(request.POST.get('num1'))
            num2 = int(request.POST.get('num2'))
            resultado = num1 - num2
        except (ValueError, TypeError):
            resultado = "Erro nos dados fornecidos!"
    return render(request, 'templates/subtrair.html', {'num1': num1, 'num2': num2, 'resultado': resultado})


def multiplicar(request):
        resultado = None
        if request.method == 'POST':
            try:
                num1 = int(request.POST.get('num1'))
                num2 = int(request.POST.get('num2'))
                resultado = num1 * num2
            except (ValueError, TypeError):
                resultado = "Erro nos dados fornecidos!"

        # Aqui você pode redirecionar para um template de resultado
        return render(request, 'calculadora/multiplicar.html', {'num1': num1, 'num2': num2, 'resultado': resultado})

#rota para chamar autor
def autor(request):
        return render(request, 'calculadora/autor.html')
#rota para chamar enquete
def enquete(request):
    return render(request, 'calculadora/enquete.html')