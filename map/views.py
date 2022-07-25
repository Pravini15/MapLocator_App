from django.shortcuts import render
import folium

# Create your views here.
def index(request):
    #create Map Object
    m = folium.Map(location=[19, -12], zoom_start=2)
    folium.Marker([5.594, -0.219])
    # Get HTML Representation of Map Object
    m = m._repr_html_()
    context = {
        'm': m,
    }
    return render(request, 'index.html', context)