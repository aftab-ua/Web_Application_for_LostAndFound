from django.shortcuts import render, redirect
from .forms import ContactForm

#
# def contact(request):
#     form = ContactForm(request.POST or None)
#     errors = None
#     if form.is_valid():
#         form.save()
#         return redirect('/')
#     if form.errors:
#         errors = form.errors
#     context = {
#         'form': form,
#         'errors': errors
#     }
#     return render(request, 'contact/contact.html', context)
