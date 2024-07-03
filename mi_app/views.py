from django.shortcuts import render

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