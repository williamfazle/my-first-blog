# Create your views here.



from django.shortcuts import render

def blog_home(request):
    return render(request, 'blog/post_list.html')   # or yourfile.html
