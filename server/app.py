from json import dumps
from bottle import post, run, request
from fetcher import getMainContent
from summarize import summarizeText

@post('/summary')
def summary():
    url = request.json['url']
    content = getMainContent(url)
    summarizeResult = summarizeText(content)
    return dumps({"summary": summarizeResult})

run(host='localhost', port=8080)
