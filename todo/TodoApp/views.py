from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import ToDo

# Create your views here.
def home(request):
    template_name = 'index.html'
    todo_list = ToDo.objects.all() # Retrieves queryset
    context = {'todo_list': todo_list}
    return render(request, template_name, context=context)

@csrf_exempt
def add_todo(request):
    if request.method == "POST":
        todo_text = request.POST["todo_text"]
        ToDo.objects.create(
            todo_text=todo_text,
        ) # Saving a Todo in the model ToDo
    
    return redirect('home')

@csrf_exempt
def delete_todo(request, todo_id):
    if request.method == 'POST':
        todo_obj = ToDo.objects.get(pk=todo_id) # Retrieving an object with id that is taken from the url
        todo_obj.delete() # Deleting the retrieved object

    return redirect('home')

@csrf_exempt
def edit_todo(request, todo_id):
    todo_obj = ToDo.objects.get(pk=todo_id)

    if request.method == 'POST':
        todo_obj.todo_text = request.POST["todo_text"]
        todo_obj.save()
        return redirect('home')

    template_name = 'edit.html'
    context = {'todo_text': todo_obj.todo_text, 'todo_obj': todo_obj}
    return render(request, template_name, context)