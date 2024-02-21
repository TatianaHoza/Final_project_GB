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

from django.views.generic import ListView
from .models import Recipe, Category


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