def wsgi_application(environ,start_response):
	status = '200 OK'
	headers = [ ('Content Type', 'text/plain') ]
	body = 'a=1 /n ...';
	start response(status, headers)
	return [ body ]
	
