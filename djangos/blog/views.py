from django.shortcuts import render

# Create your views here.
def index(request):
	context = {
		'title': 'Blogpage',
		'author': 'Reni Firmansyah',
		'nav': [
			['/', 'Home'],
			['/story', 'Story'],
			['/news', 'News']
		]
	}
	return render(request, 'index.html', context)