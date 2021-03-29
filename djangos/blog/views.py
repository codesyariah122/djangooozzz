from django.shortcuts import render

# Create your views here.

def index(request):
	context = {
		'title': 'MyDjango Blog',
		'header': 'BlogPage',
		'author': 'Suryaman Manganang'
	}
	return render(request, 'blog/index.html', context)

def story(request):
	context = {
		'title': 'MyDjango Blog',
		'header': 'StoryPage',
		'author': 'Nina Marlina'
	}
	return render(request, 'blog/index.html', context)

def news(request):
	context = {
		'title': 'MyDjango Blog',
		'header': 'NewsPage',
		'author': 'Thalita Suryanto'
	}
	return render(request, 'blog/index.html', context)