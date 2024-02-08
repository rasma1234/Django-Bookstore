**### Django Class-Based Views Exercise: Simple Bookstore******Objective:****
Create a simple bookstore application using Django where users can view a list of books, see the details of a book, edit a book's details, create a new book entry, and delete a book.****Setup:****1. Start a new Django project named `bookstore_project`.
2. Create a new app called `books`.****Models:****In ``books/models.py `:`

```
```python
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField()
    published_date = models.DateField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title
```

```

****URLs:****In ``books/urls.py``:

```

```python
from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
    BookUpdateView,
    BookCreateView,
    BookDeleteView
)

urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path(???, name='book_detail'),
    path(????, name='book_create'),
    path(???, name='book_edit'),
    path(????, name='book_delete'),
]
```

```

****Views:****In ``books/views.py``, you should implement the following class-based views using Django's built-in views:1. ``BookListView``: Display all the books in a list format.
2. ``BookDetailView``: Show the details of a single book.
3. ``BookUpdateView``: Allow users to edit an existing book's details.
4. ``BookCreateView``: Allow users to create a new book entry.
5. ``BookDeleteView``: Allow users to delete a book.****Hints:****
- You will need to define a ``template_name`` and a ``model`` for each class-based view.
- For ``UpdateView``, ``CreateView``, and ``DeleteView``, you'll also need to define a  ``fields``, `model` and a ``success_url``(or use `get_absolute_url`).
- Make sure to create the corresponding templates for each view in the ``templates`` directory.Once you've set up your views and URLs, you can run the server and test the CRUD operations for the books.** (bearbeitet) **
```
