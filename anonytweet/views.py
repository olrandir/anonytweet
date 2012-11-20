from django.shortcuts import render

from anonytweet.models import Tweeter

def home(request):
	text = ""
	if request.method == "POST":
		try:
			text = request.POST['tweet']
		except:
			pass

	return render(request, "home.html", {
		'previous_tweet': text,
		})