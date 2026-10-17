


```Status code	Name	When to use
200 OK	Success	Fetch data or successfully update a resource
201 Created	Created	Successfully create a new resource
202 Accepted	Accepted	Accept a task for asynchronous processing
204 No Content	No content	Successfully delete a resource without returning a body
400 Bad Request	Invalid request	Request is malformed or semantically invalid
401 Unauthorized	Unauthenticated	Missing or invalid authentication credentials
403 Forbidden	Forbidden	User is authenticated but lacks permission
404 Not Found	Not found	Resource does not exist
405 Method Not Allowed	Invalid method	HTTP method isn't supported for the endpoint
409 Conflict	Conflict	Duplicate resource or conflicting state
415 Unsupported Media Type	Unsupported format	Request uses an unsupported content type
422 Unprocessable Content	Validation error	Request data fails validation
429 Too Many Requests	Rate limited	Client has exceeded a rate limit
500 Internal Server Error	Server error	Unexpected application error
502 Bad Gateway	Bad gateway	Proxy received an invalid upstream response
503 Service Unavailable	Unavailable	Service is temporarily unable to handle requests
504 Gateway Timeout	Gateway timeout	Upstream service did not respond in time```