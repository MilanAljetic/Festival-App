from django.contrib.auth import logout
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, resolve_url
from django.urls import reverse, reverse_lazy
from django.views.generic import DeleteView, UpdateView
from django.db.models import Q

from .form import FestivalForm, UserForm
from .models import Festival, Users


@ login_required
def manager_logout(request):

    logout(request)
    
    return HttpResponseRedirect(reverse('fest_app:base'))

class ManagerLogin(auth_views.LoginView):

    template_name = 'fest_app/login.html'
    def get_success_url(self):

        return resolve_url('fest_app:base')

def index(request):

    query = request.GET.get('q')

    festivals = Festival.objects.order_by('-create_event_time')
    paginator = Paginator(festivals, 10)
    page_number = request.GET.get('page')
    page_obj = None
    if query:
        page_obj = Festival.objects.filter(name__icontains=query)
    else:
        page_obj = paginator.get_page(page_number)
    
    return render(request, 'fest_app/index.html', {'page_obj': page_obj})


def festival_detail(request, slug):

    festival = get_object_or_404(Festival, slug=slug)
    users = Users.objects.all()
    list_users = []
    for user in users:
        if user.festival == festival:
            list_users.append(user)

    return render(request, 'fest_app/festival_details.html', {'festival': festival, 'list_users':list_users})


def festival_create(request, *args, **kwargs):

    form = FestivalForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
    else:
        form = FestivalForm()
    context = {"form": form}

    return render(request, "fest_app/festival_form.html", context)


class FestivalUpdate(LoginRequiredMixin, UpdateView):

    redirect_field_name = 'recipe/recipe_detail.html'
    form_class = FestivalForm
    model = Festival
    template_name = "fest_app/festival_form.html"

class FestivalDelete(LoginRequiredMixin, DeleteView):

    model = Festival
    success_url = reverse_lazy('fest_app:base')
    template_name = "fest_app/festival_delete.html"


def user_list(request, slug):

    festival = get_object_or_404(Festival, slug=slug)
    users = Users.objects.all()
    list_users = []
    for user in users:
        if user.festival == festival:
            list_users.append(user)

    return render(request, "fest_app/user_list.html", {'list_users':list_users})


def user_apply(request, slug, *args, **kwargs):

    fest = get_object_or_404(Festival, slug=slug)
    form = UserForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
    else:
        form = UserForm()
    initial = UserForm(initial={'festival': fest})
    context = {"form": form, 'initial': initial}

    return render(request, "fest_app/user_form.html", context)
    
