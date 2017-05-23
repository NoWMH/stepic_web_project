def app(environ, start_response):
	#BUSINNES, MAT EGO, LOGIC, EEE
	bodypozitiv = ''
	for line in environ["QUERY_STRING"].split("&"):
		bodypozitiv = data+line+"\n"
	start_response('200 OK', [('Content-Type', 'text/plain')])
    return bodypozitiv


