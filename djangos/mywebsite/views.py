from django.shortcuts import render

def index(request):

	context = {
		'title': 'MyDjango Website',
		'header': 'HomePage',
		'author': 'PujiErmanto'
	}

	return render(request, 'index.html', context)