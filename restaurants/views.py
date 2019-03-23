import random
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
# function based view
# def home_old(request):
#     html_var = 'f strings'
#     num = random.randint(0, 100000000)
#     html_ = """<!DOCTYPE html>
#       <html lang="en">
#         <head>
#         </head>
#         <body>
#           <h1>Hello World!</h1>
#           <p>This is {} coming though</p>
#           <p>This is random number {num}</p>
#           </body>
#       </html>
#
#     """.format(
#       html_var
#     )
#
#     #f strings
#     return HttpResponse(html_)


def home(request):
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
    return render(request, "home.html", context)


def home2(request):
    context = {
    }
    return render(request, "home2.html", context)


def home3(request):
    context = {
    }
    return render(request, "home3.html", context)



