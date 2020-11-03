from django.shortcuts import redirect

def redirect_blog(request):
    return redirect('posts_lists_url', permanent=True)
