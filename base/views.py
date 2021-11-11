from django.shortcuts import render

from .models import Background, Hot, Salad, Snacks, Bar, Dessert, Phone, Interior, Place, Team, Specially, Gallery


def index(request):
    bg = Background.objects.last()
    hot = Hot.objects.all()
    salad = Salad.objects.all()
    snacks = Snacks.objects.all()
    bar = Bar.objects.all()
    dessert = Dessert.objects.all()
    phone = Phone.objects.last()
    interior = Interior.objects.last()
    place = Place.objects.last()
    team = Team.objects.last()
    spec = Specially.objects.last()
    gall = Gallery.objects.all()
    return render(request, 'index.HTML', {'bg': bg,
                                          'hot': hot,
                                          'salad': salad,
                                          'snacks': snacks,
                                          'bar': bar,
                                          'dessert': dessert,
                                          'phone': phone,
                                          'interior': interior,
                                          'place': place,
                                          'team': team,
                                          'spec': spec,
                                          'gall': gall})
