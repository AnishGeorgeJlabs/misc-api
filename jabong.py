from external.sheet import append_row_to_content
from data import jsonResponse, db
import json

def test_insert(request):
    append_row_to_content(['Testing', 'Row'])
    return jsonResponse({"success": True})

def get_form(request):
    data = list(db.jabong_form.find({}, {"_id": False}))
    return jsonResponse(data)

def post_form(request):
    try:
        data = json.loads(request.body)
        return jsonResponse({"success": True, "data": data})
    except Exception, e:
        return jsonResponse({"success": False, "error": "Exception, "+str(e)})
