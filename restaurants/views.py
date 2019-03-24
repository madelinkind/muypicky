import random
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

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
#

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
class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['id'] = '4325'
        context['name'] = 'made'

        num = None
        some_list = [
            random.randint(0, 100000000),
            random.randint(0, 100000000),
            random.randint(0, 100000000)
        ]
        condition_bool_item = True
        if condition_bool_item:
            num = random.randint(0, 100000000)
        context = {
            "some_list": some_list,
            "num": num

        }

        return context


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

# video 14