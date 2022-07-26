from django.shortcuts import render, redirect
from .models import Search
from django.http import HttpResponse
from .forms import SearchForm
import folium
import geocoder

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = SearchForm()
    address = Search.objects.all().last()
    location = geocoder.osm(address)
    lat = location.lat
    lng = location.lng
    country = location.country
    if lat == None or lng==None:
        address.delete()
        return HttpResponse('Your address input is invalid.')
    #create Map Object
    m = folium.Map(location=[10, 80], zoom_start=3)
    folium.Marker([lat, lng], tooltip='Click for more', popup=country).add_to(m)
    # Get HTML Representation of Map Object
    m = m._repr_html_()
    context = {
        'm': m,
        'form': form,
    }
    return render(request, 'index.html', context)