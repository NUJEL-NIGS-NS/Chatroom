from django.shortcuts import render
from Chat.settings import STATIC_ROOT
from .models import Group,Chat
from django.http import HttpResponse

# Create your views here.
def HomeView(request):
    print(STATIC_ROOT)
    return render(request,'home.html')


def ChatView(request):
    try:
        group_name = request.GET.get('group')
        name = request.GET.get('name')
        
        # Check if a Group with the given name exists in the database
        group = Group.objects.filter(name=group_name).first()
        
        if not group:
            # If the Group doesn't exist, create a new one
            group = Group(name=group_name)
            group.save()
        
        # Fetch all Chat objects related to the group
        chats = Chat.objects.filter(group=group).values('name','content')
        list_Msg = []
        for i in chats:
            list_Msg.append(i['name']+' : \n'+i['content']+'\n')

        
        data = {
            'name': name,
            'group': group_name,
            'chats': list_Msg
        }
        print(data)

        # You may also want to handle the case when 'ChatArea.html' template is missing
        return render(request, 'ChatArea.html', data)
    except Exception as e:
        # Log the exception or handle it in a meaningful way
        print(f"An error occurred: {e}")
        # Return an appropriate response when an exception occurs
        return HttpResponse("An error occurred while processing your request.")
