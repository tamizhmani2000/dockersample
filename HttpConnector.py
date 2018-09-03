
import requests,xml.etree.ElementTree as ET,configparser;
import subprocess;

class HttpConnector:


  def __loadProps(self):
      config = configparser.ConfigParser()
      config.read('access.ini')
      self.__url = config['SPLUNK']['url']
      self.__username=config['SPLUNK']['username']
      self.__password=config['SPLUNK']['password']
      print(self.__url,self.__username,self.__password)

  def __init__(self):
      self.__loadProps()
      self.__retrieveAccessToken()

  def get_url(self):
      return self.__url

  def get_sessionkey(self):
    return self.__sessionkey

  def __retrieveAccessToken(self):
      res = requests.post(self.__url, verify=False,data={'username': self.__username, 'password': self.__password})
      content = res.content
      # print(content)
      root = ET.fromstring(content)
      key = root.find('sessionKey')
      #print('url:', self.__url, 'username: ',self.__username,'password: ',self.__password)

      self.__sessionkey=key.text
      #print('sessionkey: ',self.__sessionkey)

  def downloadQueryResults(self):
      skey = 'Splunk ' + self.__sessionkey
      headers = {'Authorization': skey}
      payload={'search':'search index=main Type=GiftCardCheck earliest=-4h@h NumberSuccess>=0 | bucket _time span=1d | stats count as total_ip_data, sum(NumberSuccess) as successes by _time IP Data | eventstats sum(total_ip_data) as total, sum(successes) as successes by _time IP | where total > 5 AND (successes/total)*100 < 10 and successes>0 | stats sum(total_ip_data) AS count by _time IP, Data | table Data','count':0,'timeout':86400,'output_mode':'csv'}
      r = requests.post("https://neimanmarcus.splunkcloud.com:8089/services/search/jobs/export",verify=False,headers=headers,data=payload,stream=True)
      #print(r.content)

      with open("output2", 'wb') as fd:
          for chunk in r.iter_content(chunk_size=128):
              fd.write(chunk)
      print("Query Retrieved")
      fd.close()







httpCon = HttpConnector()
print(httpCon.get_sessionkey())

query="https://neimanmarcus.splunkcloud.com:8089/services/search/jobs/export --data search='search index=main earliest=-1m@m file=ajax.service data=* |table data' -d count=0 -d timeout=86400 -d output_mode=json"
#httpCon.downloadQueryResults()
#return_code = subprocess.call("./transform.sh", shell=True)

token = httpCon.getaccesstoken()

print('Access Token:', token)