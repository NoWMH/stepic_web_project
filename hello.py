def app(environ, start_response):
	#BUSINNES, MAT EGO, LOGIC, EEE
	bodypozitiv = '\n'.join(environ['QUERY_STRING'].split('&'))
	status = '200 OK'
	headers = [ ('Content-Type', 'text/plain') ]
	start_response(status, headers)
	return iter([ bodypozitiv ])
	
