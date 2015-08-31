import httplib2
# Do OAuth2 stuff to create credentials object
from oauth2client.file import Storage
from oauth2client.client import flow_from_clientsecrets
from oauth2client import tools
import gspread
import os

def local_file(name):
    cdir = os.path.dirname(__file__)
    filename = os.path.join(cdir, name)
    return filename

def get_worksheet(i):
    storage = Storage(local_file("creds.data"))
    credentials = storage.get()
    if credentials is None or credentials.invalid:
        flags = tools.argparser.parse_args(args=[])
        flow = flow_from_clientsecrets(local_file("client_secret.json"), scope=["https://spreadsheets.google.com/feeds"])
        credentials = tools.run_flow(flow, storage, flags)
    if credentials.access_token_expired:
        credentials.refresh(httplib2.Http())
    gc = gspread.authorize(credentials)

    wks = gc.open_by_key('19iYvSr0DgddeCxXVsQiOYPV-fKFRQevEDElkj_T4_lQ')
    return wks.get_worksheet(i)

def get_content_sheet():
    return get_worksheet(0)

