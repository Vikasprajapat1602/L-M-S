from .models import Student  
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import IssueForm, ReturnForm
from datetime import date
from decimal import Decimal
from django.contrib import messages
from .models import Issue
from django.http import JsonResponse
from django import forms


# Create your views here.

def home(request):
    return render(request, 'library/base.html')


def books(request):
    return render(request, 'library/books.html')

def students(request):
    return render(request, 'library/students.html')


def issue_book(request):
    if request.method == 'POST':
        form = IssueForm(request.POST)
        if form.is_valid():
            issue = form.save()
            book = issue.book
            if book.available_copies > 0:
                book.available_copies -= 1
                book.save()

                messages.success(request, "Book issued successfully")
                return redirect('home')
    else:
        form = IssueForm()
    return render(request, 'library/issue_book.html', {'form': form})


def return_book(request):
    message = ""
    fine = 0
    book_to_return = None

    if request.method == 'POST':
        form = ReturnForm(request.POST)
        if form.is_valid():
            student = form.cleaned_data['student']
            book = form.cleaned_data['book']

            # Find unreturned issue record(basis of Student + Book)
            issue = Issue.objects.filter(student=student, book=book, is_returned=False).first()

            if issue:
                issue.return_date = date.today()
                issue.is_returned = True

                if issue.return_date > issue.due_date:
                    days_late = (issue.return_date - issue.due_date).days
                    fine = Decimal(days_late * 5)
                    issue.fine_amount = fine

                issue.save()

                # Available copies of Book +1
                book.available_copies += 1
                book.save()

                message = f"Book returned successfully. Fine: ₹{fine}"
                book_to_return = issue
            else:
                message = "No matching book issued to this student or already returned."

    else:
        form = ReturnForm()

    return render(request, 'library/return_book.html', {
        'form': form,
        'message': message,
        'book_to_return': book_to_return
    })



def issue_list(request):
    issues = Issue.objects.all()
    return render(request, 'library/issue_list.html', {'issues': issues})


def clear_fine(request, pk):
    issued_book = get_object_or_404(Issue, pk=pk)

    # Fine start = 0
    issued_book.fine = 0
    issued_book.save()

    messages.success(request, "Fine cleared successfully.")
    return redirect('issued_books')


# Get all issued books for a student
def get_issued_books(request):
    student_id = request.GET.get('student_id')
    books = Issue.objects.filter(student_id=student_id, is_returned=False).values('id', 'book__title')

    return JsonResponse(list(books), safe=False)



class ReturnForm(forms.Form):
    student = forms.ModelChoiceField(queryset=Student.objects.all(), label="Student")
    book = forms.ModelChoiceField(queryset=Book.objects.all(), label="Book")

    def __init__(self, *args, **kwargs):
        super(ReturnForm, self).__init__(*args, **kwargs)

                # Fiter book queryset according to student if request == POST
        if 'student' in self.data:
            try:
                student_id = int(self.data.get('student'))
                self.fields['book'].queryset = Book.objects.filter(issue__student_id=student_id, issue__is_returned=False).distinct()
            except (ValueError, TypeError):
                pass  # invalid input — ignore and keep empty


def get_books_for_student(request):
    student_id = request.GET.get('student_id')
    books = Issue.objects.filter(student_id=student_id, is_returned=False).values('book__id', 'book__title')
    
    # Rename keys for JavaScript
    books_list = [{'id': book['book__id'], 'name': book['book__title']} for book in books]
    return JsonResponse({'books': books_list})

