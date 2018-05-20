from sanic import Sanic
from sanic import response
import os

# Runs an instance of Sanic server
app = Sanic()

app.static('/static', './static')

# Creates "index.html" route
@app.route("/")
async def answer(request):
	# Relative path with os - current working directory + index file path
	template = open(os.getcwd() + "/index.html")
	return response.html(template.read())

# Creates "about.html" route
@app.route("/about.html")
async def answer(request):
	template = open(os.getcwd() + "/about.html")
	return response.html(template.read())

# Creates "contactUs.html" route
@app.route("/contactUs.html")
async def answer(request):
	template = open(os.getcwd() + "/contactUs.html")
	return response.html(template.read())

if __name__ == "__main__":
	app.run(host = "0.0.0.0", port = "8000")
