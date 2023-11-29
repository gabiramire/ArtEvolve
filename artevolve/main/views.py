from django.shortcuts import render

# Create your views here.
def main_homepage(request):
    valor_renderizado = "Rafael"
    context = {
        'nome_user': valor_renderizado
    }
    return render(request, "main/home.html", context)