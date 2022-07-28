from django.shortcuts import render
from personas.models import Persona
# Create your views here.
def familia(request):
    # new_familia = Persona.objects.create(document= 123456789, description = "Familia Gomez")
    # new_familia2 =Persona(document= 963852741, description = "Familia Caseres")
    # new_familia2.save()
    # context = {
    #     'new_familia':new_familia,
    #     'new_familia2':new_familia2
    # }
    new_familia = Persona.objects.all()
    return render(request, "familia.html", context={'familias': new_familia})

