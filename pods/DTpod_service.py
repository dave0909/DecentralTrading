
__version__ = "0.1"
__all__ = ["DTpod_service"]
__author__ = "bones7456"
__home_page__ = "http://li2z.cn/"
import html
import xmlrpc
from DTsubscription_oracle import DTsubscription_oracle
import os
from DTauthenticator import DTauthenticator
import posixpath
from http.server import HTTPServer, BaseHTTPRequestHandler
import http.server
import urllib
import cgi
import shutil
import mimetypes
import re
try:
    from io import StringIO
except ImportError:
    from io import StringIO
from DTaddresses import *

class DTpod_service(BaseHTTPRequestHandler):
                
    server_version = "SimpleHTTPWithUpload/" + __version__
    authenticator=DTauthenticator()
   

    def __init__(self, pod_pk,*args):
        self.pod_pk=pod_pk
        self.subscription_oracle=DTsubscription_oracle(DTSUBSCRIPTION,self.pod_pk)
        BaseHTTPRequestHandler.__init__(self, *args)



    def do_GET(self,auth_token=None,claim=None,id_subscription=None):
        print(id_subscription) 
        if auth_token==claim==id_subscription==None:
            self.send_error(400, "Bad request")
            return None
        if not self.authenticator.authenticate(self.path,auth_token,claim):
            self.send_error(400, "Authentication failed, bad request")
            return None
        if not self.subscription_oracle.pull_subscription_verification(int(id_subscription),claim):
            self.send_error(400, "Subscription not verified, bad request")
            return None
        f = self.send_head()     
        result=f.read()
        print(auth_token,claim)
        if f:            
            if type(result)==type("a"):
                self.wfile.write(bytes(result,'utf-8'))
            else:
                self.wfile.write(result)
            f.close()
        
    def do_HEAD(self):
        f = self.send_head()
        if f:
            f.close()

    def do_POST(self):
        claim=None
        auth_token=None
        try:
            ctype, pdict = cgi.parse_header(self.headers.get('content-type'))
        except Exception:
            self.send_error(400,"Bad Request")
        if ctype == 'multipart/form-data':
            pdict['boundary'] = bytes(pdict['boundary'], "utf-8")
            pdict['CONTENT-LENGTH'] = self.headers.get('content-length')
            fields = cgi.parse_multipart(self.rfile, pdict)
            try:
                auth_token = fields.get('auth_token')[0]
                claim=fields.get("claim")[0]
                id_subscrption=fields.get("id_subscription")[0]
            except Exception:
                auth_token=None
                claim=None

        self.do_GET(auth_token,claim,id_subscrption)
        
   
      

    def send_head(self):
        path = self.translate_path(self.path)
        f = None
        if os.path.isdir(path):
            if not self.path.endswith('/'):
                self.send_response(301)
                self.send_header("Location", self.path + "/")
                self.end_headers()
                return None
            else:
                self.send_error(404,"Pod resource not found")
        ctype = self.guess_type(path)
        try:
            f = open(path, 'rb')
        except IOError:
            self.send_error(404, "Pod resource not found")
            return None
        self.send_response(200)
        self.send_header("Content-type", ctype)
        fs = os.fstat(f.fileno())
        self.end_headers()
        return f

    def list_directory(self, path):
  
        try:
            list = os.listdir(path)
        except os.error:
            self.send_error(404, "No permission to list directory")
            return None
        list.sort(key=lambda a: a.lower())
        f = StringIO()
        displaypath = html.escape(urllib.parse.unquote(self.path))
        f.write('<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">')
        f.write("<html>\n<title>Directory listing for %s</title>\n" % displaypath)
        f.write("<body>\n<h2>Directory listing for %s</h2>\n" % displaypath)
        f.write("<hr>\n")
        for name in list:
            fullname = os.path.join(path, name)
            displayname = linkname = name
            # Append / for directories or @ for symbolic links
            if displayname.startswith("."):
                continue
            if os.path.isdir(fullname):
                displayname = name + "/"
                linkname = name + "/"
            if os.path.islink(fullname):
                displayname = name + "@"
                # Note: a link to a directory displays with @ and links with /
            f.write('<li><a href="%s">%s</a>\n'
                    % (urllib.parse.quote(linkname), html.escape(displayname)))
        f.write("</ul>\n<hr>\n</body>\n</html>\n")
        length = f.tell()
        f.seek(0)
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.send_header("Content-Length", str(length))
        self.end_headers()
        return f

    def translate_path(self, path):
     
        # abandon query parameters
        path = path.split('?',1)[0]
        path = path.split('#',1)[0]
        path = posixpath.normpath(urllib.parse.unquote(path))
        words = path.split('/')
        words = filter(None, words)
        path = self.server.base_path
        for word in words:
            drive, word = os.path.splitdrive(word)
            head, word = os.path.split(word)
            if word in (os.curdir, os.pardir): continue
            path = os.path.join(path, word)
        return path

    def copyfile(self, source, outputfile):
    
        shutil.copyfileobj(source, outputfile)

    def guess_type(self, path):
    

        base, ext = posixpath.splitext(path)
        if ext in self.extensions_map:
            return self.extensions_map[ext]
        ext = ext.lower()
        if ext in self.extensions_map:
            return self.extensions_map[ext]
        else:
            return self.extensions_map['']

    if not mimetypes.inited:
        mimetypes.init() # try to read system mime.types
    extensions_map = mimetypes.types_map.copy()
    extensions_map.update({
        '': 'application/octet-stream', # Default
        '.py': 'text/plain',
        '.c': 'text/plain',
        '.h': 'text/plain',
        })
class StoppableHTTPServer(HTTPServer):

    stopped = False
    allow_reuse_address = True

    def __init__(self, *args, **kw):
        HTTPServer.__init__(self, *args, **kw)
        self.base_path=args[2]


    def serve_forever(self):
        while not self.stopped:
            self.handle_request()

    def force_stop(self):
        print("Stopping server...")
        self.server_close()
        self.stopped = True
        #self.create_dummy_request()

#server=StoppableHTTPServer(('localhost',9999),SimpleHTTPRequestHandler)
#print("Server now running...")
#server.serve_forever()


