from json import dumps
from bottle import route, run, request, response
from fetcher import getMainContent
from summarize import summarizeText
from shorten import shortenText

# the decorator
def enable_cors(fn):
    def _enable_cors(*args, **kwargs):
        # set CORS headers
        response.headers['Access-Control-Allow-Origin'] = request.headers['Origin']
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

        if request.method != 'OPTIONS':
            # actual request; reply with the actual response
            return fn(*args, **kwargs)

    return _enable_cors

@route('/summary', method=['OPTIONS', 'POST'])
@enable_cors
def summary():
    url = request.json['url']
    content = getMainContent(url)
    shortenedContent = shortenText(content)
    summarizeResult = summarizeText(shortenedContent)
    response.headers['Content-Type'] = 'application/json'
    return dumps({"summary": summarizeResult})

run(host='localhost', port=8080)
