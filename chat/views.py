from django.shortcuts import render
from django.shortcuts import render_to_response
import os
from django.views.decorators.csrf import csrf_protect,csrf_exempt
from django.template import RequestContext
from django.http import HttpResponse
import json

# Create your views here.
#@csrf_exempt
def chat(request):
	
	variables = RequestContext(request, {})
	return render_to_response('chat.html',variables)

def addchat(request):
	print "we are here"
	print request.body
	data=json.loads(request.POST['json'])
	filename=data['to']+"_"+data['from']
	#print request.POST.get('to')
	#print request.POST.get('from')
	filename=filename.replace(" ","")
	module_dir = os.path.dirname(__file__)  # get current directory
	file_path = os.path.join(module_dir, 'static/json/'+filename+'.json')
	print file_path
	entry = {'to': data['to'], 'from': data['from'],'time':data['time'],'message':data['message']}
	with open(file_path,'a') as feedsjson:		
		feedsjson.write("{}\n".format(json.dumps(entry)))
	r=HttpResponse()
	r.text="True"
	return r