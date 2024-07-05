from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
def mi_vista(request):
  car_list = [
    {'title':'BMW'},
    {'title':'Mazda'},
  ]

  contexto = {
    'car_list': car_list
  }
  return render(request, 'mi_app/car_list.html', contexto)

class CarListView(TemplateView):
  template_name = 'mi_app/car_list.html'

  def get_context_data(self):
    car_list = [
      {'title':'BMW'},
      {'title':'Mazda'},
    ]

    return {
      'car_list': car_list
    }

def my_view(request, *args, **kwargs):
  print(args)
  print(kwargs)
  return HttpResponse('')