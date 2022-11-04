from urllib import response
from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.


# def january(request):
#     return HttpResponse("Eat no meat for the entire month")

# def february(request):
#     return HttpResponse("Walk for atleast 20 mins everyday!")

# def march(request):
#     return HttpResponse("Learn Django for 20 mins everyday!")

monthly_challenges = {
    "january" : "Eat no meat for the entire month" ,
    "february" : "Walk for atleast 20 mins everyday!",
    "march" : "Learn Django for 20 mins everyday!",
    "april" : "Eat no meat for the entire month" ,
    "may" : "Walk for atleast 20 mins everyday!",
    "june" : "Learn Django for 20 mins everyday!",
    "july" : "Eat no meat for the entire month" ,
    "august" : "Walk for atleast 20 mins everyday!",
    "september" : "Learn Django for 20 mins everyday!",
    "october" : "Eat no meat for the entire month" ,
    "november" : "Walk for atleast 20 mins everyday!",
    "december" : None
}

def index(request):
    # list_items = ""
    months = list(monthly_challenges.keys())

    # for month in months:
    #     capitalise_month = month.capitalize()
    #     month_path = reverse("month-challenge", args=[month])
    #     list_items += f"<li><a href='{month_path}'>{capitalise_month}</a></li>"
    
    # response_data = f"<ul>{list_items}</ul>"
    return render(request, "challenges/index.html",{
        "months" : months
    })

def monthly_challenge_by_number(request,month):
    months = list(monthly_challenges.keys())

    if month > len(months) :
        return HttpResponseNotFound("Invalid month!")

    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge",args=[redirect_month])#/challenge
    return HttpResponseRedirect( redirect_path)
  
def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request,"challenges/challenge.html",{
            "text" : challenge_text,
            "month" : month
        })
        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)
    except:
        #response_data = render_to_string("404.html")
        raise Http404()
    