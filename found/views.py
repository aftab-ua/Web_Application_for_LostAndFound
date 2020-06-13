from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from contacts.forms import ContactForm
from person.models import Person
from item.models import Item
from .forms import FoundPersonModelForm, FoundItemModelForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.


def found(request):
    found_person = Person.objects.filter(person='F').all()
    found_item = Item.objects.filter(category='F').all()
    search = request.GET.get('q')

    if search:
        found_person = Person.objects.filter(
            Q(status__icontains=search) |
            Q(name__icontains=search) |
            Q(father_name__icontains=search) |
            Q(mother_name__icontains=search) |
            Q(age__icontains=search) |
            Q(location__icontains=search) |
            Q(phone_number__icontains=search) |
            Q(identification_mark__icontains=search) |
            Q(secret_information__icontains=search)
        )

        found_item = Item.objects.filter(
            Q(status__icontains=search) |
            Q(name__icontains=search) |
            Q(category__icontains=search) |
            Q(location__icontains=search) |
            Q(phone_number__icontains=search) |
            Q(identification_mark__icontains=search) |
            Q(secret_information__icontains=search)
        )
    context = {
        'found_person': found_person,
        'found_item': found_item
    }
    return render(request, 'found.html', context)


# Found Person Details

def found_person_details(request, id):
    fp_detail = get_object_or_404(Person, id=id)
    related_found_person = Person.objects.filter(body_color__icontains='white')[1:2]
    # Contact Models ---------------------#
    form = ContactForm(request.POST or None)
    errors = None
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.SUCCESS,
                             'Your message has been sent  successfully, We will cantact you in a short time')
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
    if form.errors:
        errors = form.errors
        messages.add_message(request, messages.ERROR, 'Please give the correct informations')
    # End of contact -----------------------------------------------------------------------
    context = {
        'fp_detail': fp_detail,
        'related_found_person': related_found_person,
        'form': form,
        'errors': errors
    }

    return render(request, 'found-person-details.html', context)


def found_item_details(request, id):
    f_item = get_object_or_404(Item, id=id)
    related_found_item = Item.objects.filter(status__icontains='phone')[1:2]

    # Contact Models ---------------------#
    form = ContactForm(request.POST or None)
    errors = None
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.SUCCESS,
                             'Your message has been sent  successfully, We will cantact you in a short time')
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
    if form.errors:
        errors = form.errors
        messages.add_message(request, messages.ERROR, 'Please give the correct information')
    # End of contact -----------------------------------------------------------------------

    context = {
        'f_item': f_item,
        'related_found_item': related_found_item,
        'form': form,
        'errors': errors
    }

    return render(request, 'found-item-details.html', context)


# Found Person Create View
@login_required(login_url='/login/')
def create_found_person(request):
    if request.method == "POST":
        form = FoundPersonModelForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.add_message(request, messages.SUCCESS, 'successfully Posted')
            return redirect('/found/')
    else:
        form = FoundPersonModelForm()
    context = {
        'form': form
    }
    return render(request, 'found-form.html', context)


# Found Item Create View

@login_required(login_url='/login/')
def create_found_item(request):
    if request.method == 'POST':
        form = FoundItemModelForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.add_message(request, messages.SUCCESS, 'Successfully Posted')
            return redirect('/found/')
    else:
        form = FoundItemModelForm()

    context = {
        'form': form
    }
    return render(request, 'found-form.html', context)


# Found Person Update View

@login_required(login_url='/login/')
def found_person_update(request, id):
    fp_update = get_object_or_404(Person, id=id)
    form = FoundPersonModelForm(request.POST or None, request.FILES or None, instance=fp_update)
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.SUCCESS, 'Successfully Updated')
        return redirect('found')
    context = {
        'form': form
    }
    return render(request, 'found-form.html', context)


# Found Item Update View

@login_required(login_url='/login/')
def found_item_update(request, id):
    fi_update = get_object_or_404(Item, id=id)
    form = FoundItemModelForm(request.POST or None, request.FILES or None, instance=fi_update)
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.SUCCESS, 'Successfully Updated')
        return redirect('found')
    context = {
        'form': form
    }
    return render(request, 'found-form.html', context)


# Found Person Delete

@login_required(login_url='/login/')
def found_person_delete(request, id):
    fp_delete = get_object_or_404(Person, id=id)
    if request.method == "POST":
        fp_delete.delete()
        messages.add_message(request, messages.WARNING, 'Successfully Deleted')
        return redirect('found')
    context = {
        'fp_delete': fp_delete
    }
    return render(request, 'person_delete.html', context)


# Found Item Delete
@login_required(login_url='/login/')
def found_item_delete(request, id):
    fi_delete = get_object_or_404(Item, id=id)
    if request.method == "POST":
        fi_delete.delete()
        messages.add_message(request, messages.WARNING, 'Successfully Deleted')
        return redirect('found')
    context = {
        'fi_delete': fi_delete
    }
    return render(request, 'item-delete.html', context)