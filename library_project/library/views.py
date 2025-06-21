from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import BorrowRecord
from django.utils import timezone
from django.http import HttpResponseForbidden

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto-login after registration
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'library/register.html', {'form': form})

@login_required
def borrow_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if book.available_copies > 0:
        book.available_copies -= 1
        book.save()
        BorrowRecord.objects.create(user=request.user, book=book)
    return redirect('home')

@login_required
def return_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if book.available_copies < book.total_copies:
        book.available_copies += 1
        book.save()

        # Update the borrow record
        borrow_record = BorrowRecord.objects.filter(user=request.user, book=book, return_date__isnull=True).first()
        if borrow_record:
            borrow_record.return_date = timezone.now()
            borrow_record.save()

    return redirect('home')

@login_required
def my_borrowed_books(request):
    records = BorrowRecord.objects.filter(user=request.user)
    return render(request, 'library/my_books.html', {'records': records})


def home(request):
    books = Book.objects.all()
    return render(request, 'library/home.html', {'books': books})

@login_required
def add_book(request):
    if not request.user.is_staff:  # Only admin/staff can add
        return HttpResponseForbidden("Only admins can add books.")

    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookForm()
    return render(request, 'library/add_book.html', {'form': form})

@login_required
def delete_book(request, book_id):
    if not request.user.is_staff:
        return HttpResponseForbidden("Only admins can delete books.")

    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect('home')
