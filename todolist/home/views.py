from django.shortcuts import render, HttpResponse
from home.models import Task

# Create your views here.
def home(request):
    context = {'success': False}
    if request.method == 'POST':
        title = request.POST['title']
        desc = request.POST['desc']
        print(title, desc)
        ins = Task(taskTitle=title, taskDesc=desc)
        ins.save()
        context = {'success': True}
    return render(request, 'index.html',context)

def about(request):
    allTasks = Task.objects.all()
    print(allTasks)
    for item in allTasks:
        print(item.taskDesc)
    context = {'tasks': allTasks}
    return render(request, 'about.html', context)