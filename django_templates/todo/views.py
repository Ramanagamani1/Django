from django.shortcuts import render

# Create your views here.
my_todos=[
    'do coding for 2 hours',
    'do dynamic programming tomorrow',
    'learn concepts of graphs'
]


def index(request):
    return render(request,'todos.html',{
        'tasks': my_todos
    })