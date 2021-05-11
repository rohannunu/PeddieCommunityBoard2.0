from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm, PasswordChangingForm
from peddieforum.models import UserProfile



class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = "registration/register.html"
    success_url = reverse_lazy('login')

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/editProfile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

class EditProfilePageView(generic.UpdateView):
    model = UserProfile
    template_name = 'registration/editProfilePage.html'

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('passwordSuccess')

def passwordSuccess(request):
    return render(request, 'registration/passwordSuccess.html')

class ShowProfilePageView(generic.DetailView):
    model = UserProfile
    template_name = 'registration/userProfile.html'

    def get_context_data(self, *args, **kwargs):
        #users = UserProfile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        current_user = get_object_or_404(UserProfile, id=self.kwargs['pk'])
        context['current_user'] = current_user
        return context


