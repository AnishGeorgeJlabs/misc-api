from external.sheet import append_row_to_content
from django.views.decorators.csrf import csrf_exempt
from data import jsonResponse, db
import json

def test_insert(request):
    append_row_to_content(['Testing', 'Row'])
    return jsonResponse({"success": True})

def get_form(request):
    data = list(db.jabong_form.find({}, {"_id": False}))
    return jsonResponse(data)

@csrf_exempt
def post_form(request):
    try:
        data = json.loads(request.body)
        row = []
        selected = data.get('selected', {})
        excluded = data.get('excluded', {})

        for k in ['brand', 'season', 'category', 'brick']:
            row.append(json.dumps(selected.get(k, [])))
        for k in ['percent']:
            row.append(str(selected.get(k, '')) + '%')

        for k in ['brand', 'season', 'category', 'brick']:
            row.append(json.dumps(excluded.get(k, [])))
        append_row_to_content(row)
        return jsonResponse({"success": True, "data": data})
    except Exception, e:
        return jsonResponse({"success": False, "error": "Exception, "+str(e)})
