from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Genre, Language, Book, BookInstance
from django.views.generic import CreateView,DetailView, ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

# Create your views here.
def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    num_instances_avail = BookInstance.objects.filter(
        status__exact= 'a').count()
    num_authors = Author.objects.all().count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_avail': num_instances_avail,
        'num_authors': num_authors
    }

    return render(request, 'catalog/index.html', context=context)

class BookCreate(LoginRequiredMixin, CreateView):   # model_form.html
    model= Book
    fields = '__all__'

class BookDetail(LoginRequiredMixin, DetailView):
    model = Book

class AuthorCreate(LoginRequiredMixin, CreateView):
    model = Author
    fields = '__all__'

class AuthorDetail(LoginRequiredMixin, DetailView):
    model = Author

class GenreCreate(LoginRequiredMixin, CreateView):
    model = Genre
    fields = '__all__'

class GenreDetail(LoginRequiredMixin, DetailView):
    model = Genre

@login_required
def my_view(request):
    return render(request, 'catalog/my_view.html')

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'catalog/signup.html'

class CheckedOutBooksView(LoginRequiredMixin, ListView):
    # List all books borrowed by logged in user session
    model = BookInstance
    template_name = 'catalog/profile.html'
    paginate_by = 5 # show only a maximum of 5 books per page

    def get_queryset(self):
        return BookInstance.objects.filter(borrower= self.request.user)