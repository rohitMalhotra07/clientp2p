from django.shortcuts import render
from django.shortcuts import render_to_response


# Create your views here.
def chat(request):
	return render_to_response('chat.html',
                          )
