from . import views
from .models import Movie
from django.shortcuts import render

# HINT: Create a view to provide movie recommendations list for the HTML template

def movie_recommendation_view(request):

    if request.method == "GET":
        # creating an empty dict 'context' to contain data to be presented in html template 
       context = generate_movies_context()

       return render(request, 'movierecommender/movie_list.html', context)
    

def generate_movies_context():
    context = {}
    # Show only movies in recommendation list
    # Sorted by vote_average in desc
    # Get recommended movie countsgenerate_movies_context()
    recommended_count = Movie.objects.filter(recommended=True).count()
    # If there are no recommended movies
    if recommended_count == 0:
        # Just return the top voted and unwatched movies as popular ones
        movies = Movie.objects.filter(watched=False).order_by('-vote_count')[:30]
    else:
        # Get the top voted, unwatched, and recommended movies
        movies = Movie.objects.filter(watched=False).filter(recommended=True).order_by('-vote_count')[:30]

    context['movie_list'] = movies
    return context