from django.shortcuts import render
from main.models import UserActivityPeriod
from django.core.management.base import BaseCommand
from django.http import HttpResponse
from collections import defaultdict
import json
from django.http import JsonResponse
# Create your views here.
tdict = {}

## d .. initialise the array
d = defaultdict(dict)
res = UserActivityPeriod.objects.values()
for i in res:
	d[i['real_name']][i['tz']] = ""
arr = []

#storage the response...
response = {}

##stores the user start date and end date...
usertime = [[]]

## storge unique id 
idMap = {}

##begins here...
def userActivity(request):
	## gets all results of UserActivityPeriod in result 
	result = UserActivityPeriod.objects.values()

	## user, timezone dist
	for field in result:
		idMap[field['real_name']] = field['id']
		d[field['real_name']][field['tz']] = d[field['real_name']][field['tz']] + str(field['start_time']) + "!"+str(field['end_time'])+"<>"

	## individual members
	members = []
	for j in d:
		
		for k in d[j]:
			datetimeArr = (d[j][k]).split('<>')
			for l in datetimeArr:
				pos = l.find('!')
				st = (l[:pos])
				en = (l[pos+1:])
				if(st != ""):
					usertime.append({'start_time':st,'end_time':en})
		user = json.dumps(usertime)

		members.append({'id':idMap[j],'real_name':j,'tz':k,'activity_periods':user})
		usertime.clear()
	response["ok"] = "true"
	response["members"] = members
	#viewRes = json.dumps(response)
	print(response)
	return JsonResponse(response)