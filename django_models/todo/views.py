from django.shortcuts import redirect, render
from . import models
# Create your views here.

# my_todos =[
#     'Happy coding',
#     'Do coding for 2 hours',
#     'Learn all the concepts of OS,DBMS,CN'
# ]

def index(request):
    my_todos=models.Task.objects.all()
    return render(request,'todos.html',{
        'tasks':my_todos
    })

def show_lists(request):
    list_result=models.TaskList.objects.all()
    my_todos=[item.name for item in list_result]
    return render(request,'todo/lists.html',
    {
    'lists':my_todos
    })

def add_list(request):
    if request.method == 'POST':
        list_name=request.POST['list_name']
        list=models.TaskList(name=list_name)
        list.save()
        return redirect('lists_page')
    else:
        return render(request,'todo/new_list.html')