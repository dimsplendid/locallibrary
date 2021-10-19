from django.shortcuts import render

# Create your views here.
from .models import Book, Author, BookInstance, Genre

# view(function base)
def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact="a").count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    # Genres
    num_genres = Genre.objects.count()

    context = {
        "num_books": num_books,
        "num_instances": num_instances,
        "num_instances_available": num_instances_available,
        "num_authors": num_authors,
        "num_genres": num_genres,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, "index.html", context=context)


# view(class base)
from django.views import generic


class BookListView(generic.ListView):
    model = Book
    # context_object_name = (
    #     "my_book_list"  # your own name for the list as a template variable
    # )
    # queryset = Book.objects.filter(title__icontains="人類")[
    #     :5
    # ]  # Get 5 books containing the title 人類
    # template_name = "books/my_arbitrary_template_name_list.html"  # Specify your own template name/location

    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get the context
    #     context = super(BookListView, self).get_context_data(**kwargs)
    #     # Create any data and add it to the context
    #     context['some_data'] = 'This is just some data'
    #     return context


class BookDetailView(generic.DetailView):
    model = Book
