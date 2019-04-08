from django.shortcuts import render
from django.http import HttpResponse


posts = [
	{
		'author':'Fabio',
		'title':'Blog Post 1',
		'content':'First Post Content',
		'date_posted':'Abril 01, 2019'
	},
	{
		'author':'John Doe',
		'title':'Blog Post 2',
		'content':'Second Post Content',
		'date_posted':'Abril 02, 2019'
	}
]


def home(request):
	context = {
		'posts':posts
	}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title':'About'})

