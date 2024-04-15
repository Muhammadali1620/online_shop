from django.shortcuts import render
from apps.contacts.models import Contact
from apps.general.models import General
from apps.categories.models import MainCategory


def contacts(request):
    if request.method == "POST":
        print("post")
        title = request.POST.get("title")
        message = request.POST.get("message")
        if request.user.is_authenticated:
           name = request.user.first_name
           email = request.user.email
        else:
            name = request.POST.get("name")
            email = request.POST.get("email")
        Contact.objects.create(name=name, email=email, title=title, message=message)
    categories = MainCategory.objects.all().order_by('?')[0:10 ]
    general = General.objects.first()
    context = {
        'categories':categories,
        'store_data':general
    }
    return render(request, template_name='contact.html', context=context)