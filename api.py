from data import basic_success, jsonResponse, db
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from external.sheet import get_content_sheet

@csrf_exempt
def test(request):
    if request.method == "GET":
        extra = {
            "method": "GET",
            "requestData": request.GET
        }
    else:
        extra = {
            "method": "POST",
            "requestData": request.body
        }
    return jsonResponse({
        "success": True,
        "Message": "Test api, ECHO",
        "extra": extra
    })

