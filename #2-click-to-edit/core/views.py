from django.http import QueryDict
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from core.forms import StudentForm
from core.models import Student

# Create your views here.
def index(request):
    context = {}
    return render(request, 'core/index.html', context)

def student_list(request):
    students = Student.objects.all()
    paginator = Paginator(students, 2)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj}

    if request.htmx:
        return render(request, 'core/partials/list.html', context)
    return render(request, 'core/index.html', context)

def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    context = {'student': student}
    if request.method == 'GET':
        return render(request, 'core/student.html', context)
    elif request.method == 'PUT':
        data = QueryDict(request.body).dict()
        form = StudentForm(data, instance=student)
        if form.is_valid():
            form.save()
            return render(request, 'core/partials/student-details.html', context)

        context['form'] = form
        return render(request, 'core/partials/edit-student-form.html', context)

def student_edit_form(request, pk):
    student = get_object_or_404(Student, pk=pk)
    form = StudentForm(instance=student)
    context = {'student': student, 'form': form}
    return render(request, 'core/partials/edit-student-form.html', context)