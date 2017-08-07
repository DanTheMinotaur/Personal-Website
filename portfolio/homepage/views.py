from django.shortcuts import render
from .models import Project, Skill, SkillGroup
from .forms import ContactForm
from django.core.mail import send_mail


def home(request):
    all_links = Project.objects.all()
    groups = SkillGroup.objects.all()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            send_mail("Email Test", message, name + " -- " + email, ["danieldevine74@gmail.com"])

            # return HttpResponse("Sent...")
    else:
        form = ContactForm()

    context = {
        'page_title': "Home",
        'all_links': all_links,
        'contact_form': form,
        'groups': groups,
    }

    return render(request, 'homepage/home.html', context)

