import requests
import json

class Api (object):
  def __init__ (self, host, key, ssl=True):
    self.key = key
    self.host = host
    self.protocol = 'http'
    self.list_limit = 100
    
    if ssl:
      self.protocol = 'https'
      
    self.url = '%s://%s/api/' % (self.protocol, self.host)
    
  def set_key (self, payload):
    payload['key'] = self.key
    return payload
    
  def check_response (self, r):
    if r.status_code != 200:
      raise Exception('%s: %s' % (r.status_code, r.text))
      
  def campaign_create (self, payload):
    r = requests.post(self.url + 'campaign/create/', data=self.set_key(payload))
    self.check_response(r)
    
  def campaign_add_recipients (self, list_id, campaign_id, items):
    cnt = 0
    temp = []
    
    for item in items:
      temp.append(item)
      cnt += 1
      
      if cnt >= self.list_limit:
        payload = {'recipients': json.dumps(temp), 'list_id': list_id, 'campaign_id': campaign_id}
        r = requests.post(self.url + 'campaign/add_recipients/', data=self.set_key(payload))
        self.check_response(r)
        cnt = 0
        temp = []
        
    if temp:
      payload = {'recipients': json.dumps(temp), 'list_id': list_id, 'campaign_id': campaign_id}
      r = requests.post(self.url + 'campaign/add_recipients/', data=self.set_key(payload))
      self.check_response(r)
      
  def campaign_send (self, list_id, campaign_id):
    payload = {'list_id': list_id, 'campaign_id': campaign_id}
    r = requests.post(self.url + 'campaign/send/', data=self.set_key(payload))
    self.check_response(r)
    
  def campaign_send_test (self, list_id, cmpgn_id, test_emails, payload):
    payload['list_id'] = list_id
    payload['campaign_id'] = cmpgn_id
    payload['test_emails'] = json.dumps(test_emails)
    
    r = requests.post(self.url + 'campaign/send/test/', data=self.set_key(payload))
    self.check_response(r)
    