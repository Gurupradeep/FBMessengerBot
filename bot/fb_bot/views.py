from django.shortcuts import render
from django.views import generic
from django.http.response import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError
# Create your views here.

import json, requests, random, re
from pprint import pprint

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

###setting up the required tokens
VERIFY_TOKEN = "2318934571"
PAGE_ACCESS_TOKEN = "EAAYM3po5wiABAAjBmQQZCF4K17Xd0c8kET0KdAGZAGzeMnTOpysD0PYtwA1dXNd3ZCvcwQvFrTJn2nVsPMMYsarBzSoNCqtFkQAsYBHFfMBeiNKAu35ydhP3RxDP9x1lBKgqGMGmoOejEg7sfPeCB3J54d0ijNgoTYOIyNJLwZDZD"

#to post a message back to the fb page
def post_facebook_message(fbid, recevied_message):
	post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=EAAYM3po5wiABAAjBmQQZCF4K17Xd0c8kET0KdAGZAGzeMnTOpysD0PYtwA1dXNd3ZCvcwQvFrTJn2nVsPMMYsarBzSoNCqtFkQAsYBHFfMBeiNKAu35ydhP3RxDP9x1lBKgqGMGmoOejEg7sfPeCB3J54d0ijNgoTYOIyNJLwZDZD' 
	response_msg = json.dumps({"recipient":{"id":fbid}, "message":{"text":recevied_message}})
	status = requests.post(post_message_url, headers={"Content-Type": "application/json"},data=response_msg)
	pprint(status.json())

class fb_botView(generic.View) :

	#verifying the end point
	def get(self, request, *args, **kwargs) :
		if self.request.GET['hub.verify_token'] == VERIFY_TOKEN :
			return HttpResponse(self.request.GET['hub.challenge'])
		else :
			return HttpResponse('Error,invalid token')

	@method_decorator(csrf_exempt)
	def dispatch(self,request, *args, **kwargs) :
		return generic.View.dispatch(self,request, *args, **kwargs)

	###for echoing the message
	def post(self,request, *args, **kwargs) :
		incoming_message = json.loads(self.request.body.decode('utf-8'))

		for entry in incoming_message['entry'] :
			for message in entry['messaging'] :
				if 'message' in message :
					pprint(message)
					post_facebook_message(message['sender']['id'], message['message']['text'])  					
		return HttpResponse()
    