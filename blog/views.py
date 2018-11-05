from django.views.generic import ListView, DetailView

from .models import Post


# Create your views here.

class PostList(ListView):

    def get_queryset(self):
        return Post.objects.order_by('-post_date')


class PostDetail(DetailView):
    model = Post
