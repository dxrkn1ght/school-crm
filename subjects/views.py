from django.shortcuts import render, redirect
from .models import Subject
from teachers.models import Teacher


def subjects_list(request):
    subjects = Subject.objects.all()
    subjects_count = subjects.count()
    ctx = {'subjects':subjects, 'subjects_count':subjects_count}
    return render(request, 'subjects/subjects-list.html', ctx)

def subject_add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            subject = Subject.objects.create(name=name)
            teacher_ids = request.POST.getlist('teachers')
            for teacher_id in teacher_ids:
                teacher = Teacher.objects.get(id=teacher_id)
                teacher.subject = subject
                teacher.save()
            return redirect('subjects:list')
    teachers = Teacher.objects.all()
    ctx = {'teachers': teachers}
    return render(request, 'subjects/subject-add.html', ctx)
