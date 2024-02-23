# from django.shortcuts import render
#
# from .forms import RecipeImage
# from recipe_site.cookapp.models import Recipe
#
#
# def upload_image(request):
#     if request.method == 'POST':
#         form = Recipe(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#         else:
#             form = RecipeImage()
#     return render(request, 'upload_image.html', {'form': form})
from django.shortcuts import render
from django.views.generic import ListView
from .models import Recipe, Category
from .forms import UserRegistrationForm

class CategoryListView(ListView):
    model = Category
    template_name = "category_list.html"


class RecipeByCategoryView(ListView):
    context_object_name = 'recipes'
    template_name = 'pecipe_list.html'

    def get_queryset(self):
        self.category = Category.objects.get(slug=self.kwargs['slug'])
        queryset = Recipe.objects.filter(category=self.category)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.category
        return context

def login_user(request):
    return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'account/login_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/login.html', {'user_form': user_form})