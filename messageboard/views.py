from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.signals import post_save
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView, DeleteView, View, UpdateView
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from .models import Postmodel, CommentModel
from django.contrib.auth import get_user_model
from .forms import PostForm

User = get_user_model()


# @login_required
class Home(ListView):
    model = Postmodel
    template_name = 'posts.html'
    paginate_by = 10
    ordering = ['-created_at']

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['posts'] = list(Postmodel.objects.all())
        return data


class PostDetails(DetailView):
    model = Postmodel
    template_name = 'postdetails.html'
    context_object_name = 'post'


class NewPost(LoginRequiredMixin, ListView):
    model = Postmodel
    template_name = 'newpost.html'
    context_object_name = 'post'
    form_class = PostForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PostForm()
        return context

    def post(self, request, *args, **kwargs):
        title = request.POST['title']
        content = request.POST['content']
        user_id = request.user.id
        category = request.POST['category']
        post = Postmodel(user_id=User.objects.get(id=user_id), title=title, content=content, category=category)
        post.save()
        return HttpResponseRedirect(f'{post.id}')


class NewComment(LoginRequiredMixin, DetailView):
    model = Postmodel
    template_name = 'comment_post.html'
    context_object_name = 'post'

    def post(self, request, *args, **kwargs):
        text = request.POST['text']
        user_id = request.user.id
        comment = CommentModel(user_id=User.objects.get(id=user_id), text=text,
                               post=Postmodel.objects.get(id=request.get_full_path().split("/")[1]))
        comment.save()
        return HttpResponseRedirect('/')


class DeletePost(LoginRequiredMixin, DeleteView):
    model = Postmodel
    template_name = 'deletepost.html'
    context_object_name = 'post'
    queryset = Postmodel.objects.all()
    success_url = reverse_lazy('allposts')


class PostEdit(LoginRequiredMixin, UpdateView):
    model = Postmodel
    form_class = PostForm
    template_name = 'editpost.html'
    context_object_name = 'post'

    def post(self, request, *args, **kwargs):
        post = Postmodel.objects.get(id=request.get_full_path().split("/")[1])
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.category = request.POST['category']
        post.save()
        return HttpResponseRedirect(f"../{post.id}")


class CommentsList(LoginRequiredMixin, ListView):
    model = CommentModel
    template_name = 'allcomments.html'
    context_object_name = 'comments'
    paginate_by = 5
    ordering = ['-created_at']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        my_posts = Postmodel.objects.filter(user_id=User.objects.get(id=self.request.user.id))
        post_comments = []
        for n in my_posts:
            if CommentModel.objects.filter(post=n):
                post_comments.append(CommentModel.objects.filter(post=n))
        context['comments_for_my_posts'] = post_comments
        context['limit_for_listing'] = Paginator(post_comments, 5).num_pages - 2
        return context


class CommentDetails(LoginRequiredMixin, DetailView):
    model = CommentModel
    template_name = 'commentdetails.html'
    context_object_name = 'comment'


class CommentDelete(LoginRequiredMixin, DeleteView):
    model = CommentModel
    template_name = 'deletecomment.html'
    context_object_name = 'comment'
    success_url = '/messageboard/posts_comments'


class CommentAccept(LoginRequiredMixin, View):

    def get(self, request, pk):
        comment = CommentModel.objects.get(id=request.get_full_path().split('/')[3])
        comment.is_confirmed = True
        comment.save()
        return HttpResponseRedirect('/')

