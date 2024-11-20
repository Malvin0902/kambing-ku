from django.urls import path
from main.views import show_main, create_kambing_entry, show_xml, show_json, show_xml_by_id, show_json_by_id, add_kambing_entry_ajax
from main.views import register
from main.views import login_user
from main.views import logout_user
from main.views import edit_kambing
from main.views import delete_kambing
from main.views import create_kambing_flutter



app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-kambing-entry', create_kambing_entry, name='create_kambing_entry'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register, name='register'),
    path('edit-kambing/<uuid:id>', edit_kambing, name='edit_kambing'),
    path('delete/<uuid:id>', delete_kambing, name='delete_kambing'), # sesuaikan dengan nama fungsi yang dibuat
    path('create-kambing-entry-ajax', add_kambing_entry_ajax, name='add_kambing_entry_ajax'),
    path('create-flutter/', create_kambing_flutter, name='create_kambing_flutter'),
]
