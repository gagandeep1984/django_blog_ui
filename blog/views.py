from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Blog
from .forms import BlogForm

# home
# addBlog
# likeBlog


def home(request):
    blogs = Blog.objects.all()
    context = {"blogs": blogs}

    print(blogs.query)  # print sql query

    return render(request, "home.html", context=context)


def addBlog(request):
    if request.method == "POST":
        print(request.POST)
        print(request.FILES)

        form = BlogForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("/")

    form = BlogForm()
    context = {"form": form}

    return render(request, "addBlog.html", context=context)


# liking a blog
def likeBlog(request, pk):
    print("Blogid : ", pk)
    blog = Blog.objects.get(id=pk)
    blog.likes += 1
    blog.save()

    return HttpResponse(status=200)
