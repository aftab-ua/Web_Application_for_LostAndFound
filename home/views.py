from django.contrib import messages
from django.shortcuts import render, redirect

from home.forms import RewardModeLForm
from item.models import Item
from person.models import Person
from .models import Reward, YoutubeVideo
# Create your views here.


def home(request):
    my_reward = Reward.objects.all()[:1]
    # First Div
    last_person_post = Person.objects.all()[:1]
    last_item_post = Item.objects.all()[:1]
    # 2nd Div
    lost_person = Person.objects.filter(person="L").all()[:1]
    lost_item = Item.objects.filter(category="L").all()[:1]
    # End 2 div

    home_found = Person.objects.all()[:3]
    home_item = Item.objects.all()[:3]
    videos = YoutubeVideo.objects.all()[:3]
    context = {
        'my_reward': my_reward,
        'lost_person': lost_person,
        'lost_item': lost_item,
        'home_found': home_found,
        'home_item': home_item,
        'videos': videos,
    }
    if last_person_post[0].update > last_item_post[0].update:
        context['last_post'] = last_person_post
    else:
        context['last_post'] = last_item_post

    return render(request, 'home/home.html', context)


# Reward Function

def reward(request):
    if request.method == 'POST':
        form = RewardModeLForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.add_message(request, messages.SUCCESS, 'Reward Updated .')
            return redirect('home')
    else:
        form = RewardModeLForm()
    context = {
        'form': form,
    }
    return render(request, 'home/reward.html', context)