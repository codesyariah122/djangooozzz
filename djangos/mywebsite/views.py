from django.shortcuts import render

def index(request):
	context = {
		'title': 'HomePage',
		'devname': 'PujiErmanto',
		'nav': [
			['/', 'Home'],
			['/blog', 'Blog'],
			['/about', 'About'],
			['/contact', 'Contact']
		],
	}
	return render(request, 'index.html', context)