from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from .forms import RestaurantCreateForms
from .models import RestaurantLocation

# Fuction based in view

# def home(request):
#     num = None
#     some_list = [
#         random.randint(0, 100000000),
#         random.randint(0, 100000000),
#         random.randint(0, 100000000)
#     ]
#     condition_bool_item = True
#     if condition_bool_item:
#         num = random.randint(0, 100000000)
#     context = {
#         "some_list": some_list,
#         "num": num
#
#     }
#     return render(request, "home.html", context)
#
#
# def about(request):
#     context = {
#     }
#     return render(request, "about.html", context)
#
#
# def contact(request):
#     context = {
#     }
#     return render(request, "contact.html", context)



# Class based in View

# class ContactView(View):
#     def get(self, request, *args, **kwargs):
#         print(kwargs)
#     # Diccionario
#         context = {
#             "id": kwargs['id'],
#             'kk': 'Caca'
#         }
#         return render(request, "contact.html", context)
# Shift+Tab para identar el codigo es decir para pegarlo a la izquierda

# class ContactView(View):
#     def get(self, request, *args, **kwargs):
#         context = {}
#         return render(request, "contact.html", context)

        # def post(self, request, *args, **kwargs):
        #     context = {}
        #     return render(request, "contact.html", context)
        #
        #     def put(self, request, *args, **kwargs):
        #         context = {}
        #         return render(request, "contact.html", context)


# class ContactView(TemplateView):
#     template_name = 'contact.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#
#         context['kk'] = 'Caca'
#
#         return context

#
# class HomeView(TemplateView):
#     template_name = 'home.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#
#         context['id'] = '4325'
#         context['name'] = 'made'
#
#         num = None
#         some_list = [
#             random.randint(0, 100000000),
#             random.randint(0, 100000000),
#             random.randint(0, 100000000)
#         ]
#         condition_bool_item = True
#         if condition_bool_item:
#             num = random.randint(0, 100000000)
#         context = {
#             "some_list": some_list,
#             "num": num
#
#         }
#
#         return context


# class AboutView(TemplateView):
#     template_name = 'about.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#
#         return context
#
#
# class ContactView(TemplateView):
#     template_name = 'contact.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#
#         return context

def restaurant_createview(request):
    # print(request.GET)
    # print(request.POST)
    # if request.method == "GET":
    #     print("get data")
    #     print(request.GET)

    if request.method == "POST":
        # print("post data")
        # print(request.POST)
        title = request.POST.get("title") #request.Post["title"] En este caso si pasas un title vacio da error, de lo contrario el que esta puesto devolveria none
        location = request.POST.get("location")
        category = request.POST.get("category")
        obj = RestaurantLocation.objects.create(
            name=title,
            location=location,
            category=category
        )
        return HttpResponseRedirect("/restaurants/")
    template_name = 'restaurants/form.html'
    context = {}
    return render(request, template_name, context)


def restaurant_listview(request):
    template_name = 'restaurants/restaurantlocation_list.html'
    queryset = RestaurantLocation.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, template_name, context)


def restaurant_detailview(request, slug):
    template_name = 'restaurants/restaurantlocation_detail.html'
    obj = RestaurantLocation.objects.get(slug=slug)
    context = {
        "object": obj
    }
    return render(request, template_name, context)


class RestaurantListView(ListView):
    def get_queryset(self):
        print(self.kwargs)
        slug = self.kwargs.get("slug")
        if slug:
            queryset = RestaurantLocation.objects.filter(
                Q(category__icontains=slug) |
                Q(category__iexact=slug)
            )
        else:
            queryset = RestaurantLocation.objects.all()
        return queryset


class RestaurantDetailView(DetailView):
        queryset = RestaurantLocation.objects.all()

        # def get_context_data(self, **kwargs):
        #     context = super().get_context_data(**kwargs)
        #
        #     # set additional data
        #     context['n_views'] = 543
        #     context['owner'] = 'Made'
        #     context['temperature'] = '23 degrees'
        #
        #     return context

        # def get_object(self, *arg, **kwargs):
        #     rest_id = self.kwargs.get('rest_id')
        #     obj = get_object_or_404(RestaurantLocation, id=rest_id)  # pk = rest_id
        #     return obj


# class SearchRestaurantListView(ListView):
#         template_name = 'restaurants/restaurantlocation_list.html'
#
#         def get_queryset(self):
#             print(self.kwargs)
#             slug = self.kwargs.get("slug")
#             if slug:
#                 queryset = RestaurantLocation.objects.filter(
#                     Q(category__icontains=slug) |
#                     Q(category__iexact=slug) |
#                     Q(location__icontains='Miramar')
#                 )
#             else:
#                 queryset = RestaurantLocation.objects.none()
#             return queryset
#
# video 23