from aiohttp import web
from cyutils.recur_fib import rec_fib

async def fibonacci_service(request):
	target_number = int(request.match_info.get('number', "Anonymous"))
	result = await rec_fib(target_number)
	return web.Response(text='{}'.format(result))

app = web.Application()
app.router.add_get('/faas/{number}', fibonacci_service)

web.run_app(app)
