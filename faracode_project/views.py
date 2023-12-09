from django.shortcuts import render
from projects_app.models import project
from contacts_app.models import Contact, Massage


def showhome(request):
    projects = project.objects.all()
    contacts = Contact.objects.all().first()
    name = request.POST.get('name')
    email = request.POST.get('email')
    subject = request.POST.get('subject')
    body = request.POST.get('body')
    if name and email and subject and body:
        Massage.objects.create(name=name, email=email, subject=subject, body=body)
    return render(request, 'index.html', context={"projects": projects, "contacts":contacts})
