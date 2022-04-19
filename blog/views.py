from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post
from .forms import PostForm,EditForm
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect

def LikeView(request,pk):
    post = get_object_or_404(Post, id = request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.like.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))

def total_likes(self):
    return self.like.count()


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-data']

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'art_detail.html'

    # def get_context_data(self, *args,**kwargs):
    #     context = super(ArticleDetailView, self).get_context_data()


    #     suff = get_object_or_404(Post,id=self.kwargs['pk'])
    #     total_likes = stuff.total_likes()
    #     liked = False
    #     if stuff.likes.filter(id=self.request.user)

    #     context["total_likes"] = total_likes
    #     context ["liked"] = liked
    #     return context

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__'
    # fields = ('title','body', 'title_tag')

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    # fields = ['title','title_tag','body']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')