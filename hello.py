from re import sub
def app(environ, start_response):
	#BUSINNES, MAT EGO, LOGIC, EEE
   	output = sub('&', '\n', environ.get('QUERY_STRING', ''))

   	start_response('200 OK', [('Content-Type', 'text/plain')])
   	return iter([str.encode(output)])

