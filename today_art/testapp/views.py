from django.shortcuts import render

# Create your views here.
class app1 (views.View):
    def get(self, request):
        return render(request, 'app1.html')
    def post(self, request):
        return render(request, 'app1.html')
    def put(self, request):
        return render(request, 'app1.html')
    def delete(self, request):
        return render(request, 'app1.html')

