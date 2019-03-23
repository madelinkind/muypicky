import random
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
# function based view
def home_old(request):
    html_var = 'f strings'
    html_ = """<!DOCTYPE html>
      <html lang="en">
        <head>
        </head>
        <body>
          <h1>Hello World!</h1>
          <p>This is {} coming though</p>
          </body>
      </html>

    """.format(
      html_var
    )

    #f strings
    return HttpResponse(html_)


def home(request):
    num = random.randint(0, 100000000)
    return render(request, "base.html", {"html_var": True, "num": num})

