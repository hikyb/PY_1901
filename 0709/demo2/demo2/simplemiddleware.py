from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse


class SimpleMiddleware(MiddlewareMixin):
    def process_request(self, request):
        print("处理了请求")
        # print(dir(request.headers))
        print(request.headers.get("User-Agent", "++"))
        return self.get_response(request)

    def process_response(self, request, response):
        print("处理了响应")
        ua = request.headers.get("User-Agent")
        print("当前访问工具为", ua)
        if ua.__contains__("python"):
            return HttpResponse("非法请求")
        else:
            return response
        # return HttpResponse("处理了响应")
