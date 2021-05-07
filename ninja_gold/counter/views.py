from django.shortcuts import render, redirect
import random
from datetime import datetime

def index(request):
    return render(request, "index.html")

def total_gold(request):
    if request.method == "POST":
        if 'count' not in request.session or 'activity' not in request.session:
            request.session['count'] = 0
            request.session['activity'] = []
        if 'farm' in request.POST:
            request.session['count'] += random.randint(10, 20)
            message = {
                "building": "farm",
                "count": request.session['count'],
                "saying": "Total gold so far",
                "date": datetime.now().strftime("%m/%d/%Y %I:%M%p"),
            }
            print(message)
        if 'cave' in request.POST:
            request.session['count'] += random.randint(5,10)
            message = {
                "building": "cave",
                "count": request.session['count'],
                "saying": "Total gold so far",
                "date": datetime.now().strftime("%m/%d/%Y %I:%M%p"),
            }
        if 'house' in request.POST:
            request.session['count'] += random.randint(2,5)
            message = {
                "building": "house",
                "count": request.session['count'],
                "saying": "Total gold so far",
                "date": datetime.now().strftime("%m/%d/%Y %I:%M%p"),
            }
        if 'casino' in request.POST:
            request.session['count'] += random.randint(-50,50)
            message = {
                "building": "casino",
                "count": request.session['count'],
                "saying": "Total gold so far",
                "date": datetime.now().strftime("%m/%d/%Y %I:%M%p"),
            }
        request.session['activity'].append(message)
        request.session.modified = True
    return redirect('/')

def reset(request):
    if 'count' in request.session:
        del request.session['count']
        del request.session['activity']
    return redirect('/')




# Create your views here.
