from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from .forms import TazkeraForm
from .models import Tazkera


def add(request):

    if request.method == "POST":

        form = TazkeraForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            tazkera = form.save()

            return redirect(
                "print_tazkera",
                pk=tazkera.pk
            )

    else:

        form = TazkeraForm()

    return render(
        request,
        "tazkera_form.html",
        {
            "form": form
        }
    )


def print_tazkera(request, pk):

    tazkera = get_object_or_404(
        Tazkera,
        pk=pk
    )

    services = set(
        tazkera.services.values_list(
            "code", 
            flat=True
            )
        )
    
    context = {
        "tazkera": tazkera,
        "duplicate": "duplicate" in services,
        "certification": "certification" in services,
        "photo_reattach": "photo_reattach" in services,
        "name_edition": "name_edition" in services,
        "date_place_birth": "date_place_birth" in services,
        "birth_certification": "birth_certification" in services,
        "birth_place_edition": "birth_place_edition" in services,
    }

    return render(
        request,
        "tazkera_print.html", 
        context,
    )


def list_tazkera(request):
    data = Tazkera.objects.all().order_by("-id")
    return render(request, "tazkera_list.html", {"data": data})