from django.shortcuts import render
from accounts.models import Teams
from django.db.models import F

# Create your views here.

def score(request) :
	teams_list = Teams.objects.order_by('-points',F('latest')-F('join'))
	return render(request, 'scoreboard.html', {'teams_list':teams_list})