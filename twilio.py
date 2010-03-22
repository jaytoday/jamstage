import os

from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
from google.appengine.api import users

import app_settings 


class SMSHandler(webapp.RequestHandler):
    """
    Handles incoming SMS messages
    """
    def get(self):
      return self.post()
    
    def post(self):
      pass

class CallHandler(webapp.RequestHandler):
    """
    Handles incoming phone calls
    """
    def get(self):
      return self.post()
    
    def post(self):
      from models import Subscriber
      if not self.request.get('Caller'):
        raise ValueError('No caller available for call %s' % 
        self.request.get('CallGuid'))
      caller = Subscriber.get_by_key_name(self.request.get('Caller'))        
      if self.request.get('Digits'):
        if not caller:
          caller = Subscriber(
            key_name = str(self.request.get('Caller')),
            phone_number = self.request.get('Caller')
            )
        caller.days_subscribed = int(self.request.get('Digits'))
        caller.zip_code = self.request.get('CallerZip')
        caller.put()
      if caller:
        days_subscribed = caller.days_subscribed
      else:
        days_subscribed = None
      self.context = {
      'days_subscribed': days_subscribed,
      'base_url': 'http://' + os.environ['HTTP_HOST']
      }
      return xml_response(self, 'gather.xml', self.context)


def xml_response(handler, page, context=None):
    """
    Renders an XML response using a provided template page and values
    """
    path = os.path.join(os.path.dirname(__file__), page)
    handler.response.headers["Content-Type"] = "text/xml"
    handler.response.out.write(template.render(path, context))
    
    

# wire up the views
application = webapp.WSGIApplication([
    ('/twilio/sms', SMSHandler),
    ('/twilio/call', CallHandler)

], debug=True)

def main():
    "Run the application"
    run_wsgi_app(application)

if __name__ == '__main__':
    main()
