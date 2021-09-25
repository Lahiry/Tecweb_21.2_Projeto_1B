from django.shortcuts import render, redirect
from .models import Note, Tag
import re

regex = re.compile(".*\S.*")

def index(request):
    all_notes = Note.objects.all()
    return render(request, 'notes/components/note.html', {'notes': all_notes})

def create(request):
    if request.method == 'POST':
        note_title = request.POST.get('title')
        note_content = request.POST.get('content')
        tag = request.POST.get('tag')
        if ((regex.match(note_title)) and (len(note_title) <= 20)) and (regex.match(note_content)) and (len(tag) <= 20):
            if regex.match(tag):
                Tag.objects.get_or_create(tag=tag)
                Note.objects.create(title=note_title, content=note_content, tag=Tag.objects.get(tag=tag))
            else:
                Note.objects.create(title=note_title, content=note_content)
        return redirect('index')

def update(request):
    if request.method == 'POST':
        note_id = request.POST.get('id')
        note_title = request.POST.get('title')
        note_content = request.POST.get('content')
        note_tag = request.POST.get('tag')
        tag_id = request.POST.get('tag-id')
        note = Note.objects.get(id=note_id)
        note.title = note_title
        note.content = note_content
        if regex.match(note_tag):
            Tag.objects.get_or_create(tag=note_tag)
            note.tag = Tag.objects.get(tag=note_tag)
        else:
            note.tag = None
        if (tag_id != '') and (len(Note.objects.filter(tag=Tag.objects.get(id=tag_id))) == 1) and (Tag.objects.get(id=tag_id).tag != note_tag):
            Tag.objects.get(id=tag_id).delete()
        note.save()
        return redirect('index')

def delete(request):
    if request.method == 'POST':
        note_id = request.POST.get('id')
        note = Note.objects.get(id=note_id)
        tag = note.tag
        if len(Note.objects.filter(tag=tag)) == 1 and tag:
            tag.delete()
        note.delete()
        return redirect('index')

def tags(request):
    all_tags = Tag.objects.all()
    return render(request, 'notes/components/tag.html', {'tags': all_tags})

def tag(request):
    if request.method == 'GET':
        tag = request.GET.get('tag-id')
        notes = Note.objects.filter(tag=tag)
        return render(request, 'notes/components/note_tag.html', {'notes': notes})

def delete_tag(request):
    if request.method == 'POST':
        tag_id = request.POST.get('tag-id')
        Tag.objects.get(id=tag_id).delete()
        return redirect('tags')

def update_tag(request):
    if request.method == 'POST':
        tag_id = request.POST.get('tag-id')
        tag_content = request.POST.get('tag')
        tag = Tag.objects.get(id=tag_id)
        if not regex.match(tag_content):
            tag.delete()
        elif len(Tag.objects.filter(tag=tag_content)) > 0 and tag_content != Tag.objects.get(id=tag_id).tag:
            notes = Note.objects.filter(tag=tag)
            for note in notes:
                note.tag = Tag.objects.get(tag=tag_content)
                note.save()
            tag.delete()
        else:
            tag.tag = tag_content
            tag.save()
        return redirect('tags')


    
