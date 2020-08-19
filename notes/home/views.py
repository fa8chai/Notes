from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Note, Category
from .forms import NoteForm, SearchForm
from datetime import date
from dateutil.relativedelta import relativedelta
from users.views import signup
from datetime import datetime
from django.utils import timezone





@login_required
def main(request):
    form = NoteForm()
    context={
        'notes':request.user.notes.all().order_by('-reminder'),
        'form':form
    }
    if request.method=='POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            text = request.POST['category']
            user = request.user
            try:
                category = Category.objects.get(user=user, text=text)
            except Category.DoesNotExist:
                category = Category(user=user, text=text)
                category.save()
            instance.user = user
            instance.category = category 
            instance.save()
            return redirect(main)
        context['error'] = 'Something went wrong!'
        return render(request, 'home/main.html', context=context)
    return render(request, 'home/main.html', context=context)


@login_required
def search_note(request):
    form = SearchForm()
    if request.method=='POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            try:
                notes=Note.objects.filter(reminder__contains=request.POST['search_reminder'])
            except Note.DoesNotExist:
                return render(request, 'home/search_note.html',{})
            return render(request, 'home/search_note.html',{'notes':notes,'form':form,})
        return render(request, 'home/search_note.html',{'error':'Something went wrong!',})
    return render(request, 'home/search_note.html',{'form':form,'info':'h'})


@login_required
def view_note(request, note_pk):
    try:
        note = request.user.notes.get(pk=note_pk)
    except Note.DoesNotExist:
        return render(request, 'home/view_note.html', {'error':'Deleted!'})

    context={
        'note':note,
    }
    return render(request, 'home/view_note.html', context=context)

@login_required
def delete(request, note_pk):
    try:
        note = request.user.notes.get(pk=note_pk)
    except Note.DoesNotExist:
        return render(request, 'home/main.html', {'error':'Deleted!'})
    note.delete()
    return redirect(main)

@login_required
def settings(request):
    context={
        'user':request.user
    }
    return render(request, 'home/settings.html', context=context)

@login_required
def delete_account(request):
    user = request.user
    user.is_active =False
    user.save()
    return redirect(signup)