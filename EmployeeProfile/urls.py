from django.urls import path
from django.http import HttpResponse
from .views import departments,dep_details,get_name
# ,department_details
def hello(request):
    return HttpResponse('<h1>Hello world</h1>')
    
urlpatterns = [
    path('departments',departments,name='departments'),

    # This line of code is defining a URL pattern using the `path` function from Django's `urls`
    # module. It maps a URL path 'Department_details' to a view function `dep_details` and assigns it
    # the name 'Department_details'. This allows you to reference this URL pattern by its name in your
    # Django templates or code instead of hardcoding the URL.
    path('department_details/<str:id>',dep_details, name = 'department_details'),
    path('login',get_name,name='login')
]
