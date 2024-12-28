from django.shortcuts import render, redirect
from .models import Teacher
from subjects.models import Subject


def teachers_list(request):
    teachers = Teacher.objects.all()
    teachers_count = teachers.count()
    ctx = {'teachers':teachers, 'teachers_count':teachers_count}
    return render(request, 'teachers/teachers-list.html', ctx)

def teacher_add(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        subject_id = request.POST.get('subject')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        years_of_work = request.POST.get('years_of_work')
        photo = request.FILES.get('photo')
        if first_name and last_name and subject_id and phone_number and email and years_of_work and photo:
            subject = Subject.objects.get(id=subject_id)
            teacher = Teacher.objects.create(
                first_name = first_name,
                last_name = last_name,
                subject = subject,
                phone_number = phone_number,
                email = email,
                years_of_work = years_of_work,
                photo = photo
            )
            teacher.save()
            return redirect('teachers:list')
    subjects = Subject.objects.all()
    ctx = {'subjects':subjects}
    return render(request, 'teachers/teacher-add.html', ctx)