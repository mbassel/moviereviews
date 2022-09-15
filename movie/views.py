import email
from http.client import HTTPResponse
from multiprocessing import context
from turtle import title
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Movie, Review
from .forms import ReviewForm
# Create your views here.


def home(request):
    searchTerm = request.GET.get('searchTerm')
    if searchTerm:
        movies = Movie.objects.filter(title__contains=searchTerm)
    else:
        movies = Movie.objects.all()

    context = {
        'searchTerm': searchTerm,
        'movies': movies,

    }
    return render(request, 'home.html', context)


def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    reviews = Review.objects.filter(movie=movie)
    context = {
        'movie': movie,
        'reviews': reviews
    }
    return render(request, 'detail.html', context)


def about(request):
    return render(request, 'about.html')


def signup(request):
    email = request.GET.get('email')
    return render(request, 'signup.html', {'email': email})


@login_required
def createReview(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    if request.method == 'GET':

        return render(request, 'createreview.html', {
            'form': ReviewForm(), 'movie': movie
        })
    else:
        try:
            form = ReviewForm(request.POST)
            newReview = form.save(commit=False)
            newReview.user = request.user
            newReview.movie = movie
            newReview.save()
            return redirect('detail', newReview.movie.id)
        except ValueError:
            return render(request, 'createreview.html', {
                'form': ReviewForm(),
                'error': 'bad data passed in.'
            })


@login_required
def updateReview(request, review_id):
    review = get_object_or_404(
        Review, pk=review_id, user=request.user
    )

    if request.method == 'GET':
        form = ReviewForm(instance=review)
        context = {
            'form': form,
            'review': review
        }
        return render(request, 'updatereview.html', context)
    else:
        try:
            form = ReviewForm(request.POST, instance=review)
            context = {
                'form': form,
                'review': review,
                'error': 'Bad data in form.'
            }
            form.save()
            return redirect('detail', review.movie.id)
        except ValueError:
            return render(request, 'updatereview.html', context)


@login_required
def deleteReview(request, review_id):
    review = get_object_or_404(
        Review, pk=review_id, user=request.user
    )
    review.delete()
    return redirect('detail', review.movie.id)
