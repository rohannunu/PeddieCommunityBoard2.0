from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Comment
from .forms import PostForm, EditForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

class HomeView(ListView):
    model = Post
    template_name = "home.html"
    #ordering = ['-post_date']
    ordering = ['-id'] #Posts in reverse order

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context

class PostDetailView(DetailView):
    model = Post
    template_name = "postDetails.html"

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(PostDetailView, self).get_context_data(*args, **kwargs)

        post_grabbed = get_object_or_404(Post, id=self.kwargs['pk'])
        num_likes = post_grabbed.total_likes()

        liked = False
        if post_grabbed.likes.filter(id=self.request.user.id).exists():
            liked = True
        
        context['cat_menu'] = cat_menu
        context['num_likes'] = num_likes
        context['liked'] = liked
        return context

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "addPost.html"

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(AddPostView, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context

#Might get rid of this view later, but just puttting it in for now (we dont want a whole bunch of people creating random categories)
class AddCategoryView(CreateView):
    model = Category
    template_name = "addCategory.html"
    fields = '__all__'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(AddCategoryView, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context

class EditPostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = "editPost.html"

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(EditPostView, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context

class DeletePostView(DeleteView):
    model = Post
    template_name = "deletePost.html"
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(DeletePostView, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context

def CategoryView(request, cats): #cats short for categories
    category_posts = Post.objects.filter(category=cats, admin_approved=True)
    return render(request, 'categories.html', {'cats':cats, 'category_posts':category_posts})

def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'categoryList.html', {'cat_menu_list':cat_menu_list})

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    #liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        #liked = False
    else:
        post.likes.add(request.user)
        #liked = True
    return HttpResponseRedirect(reverse('postDetail', args=[str(pk)]))

def termsConditionsView(request):
    return render(request, 'termsConditions.html')

def aboutView(request):
    return render(request, 'about.html')

class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'addComment.html'
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        form.instance.comment_author = self.request.user
        return super().form_valid(form)
    success_url = reverse_lazy('home')

