from django.http import HttpResponse

def index(res):
	title = "<h1>Home Page</h1>"
	subTitle = "<h2>Selamat Datang di Django Website"
	output = title + subTitle
	return HttpResponse(output)

def about(res):
	return HttpResponse("<h2>About Page</h2>")