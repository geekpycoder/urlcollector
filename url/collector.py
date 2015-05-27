'''
Created on 27-May-2015

@author: Admin
'''
import urllib
from bs4 import BeautifulSoup
import tldextract

def same_domain(url1, url2):
  url1_extract = tldextract.extract(url1)
  url2_extract = tldextract.extract(url2)
  if url1_extract.domain == url2_extract.domain:
    return True
  else:
    return False

def collect(url, result, depth, level, domain = True):
  try:
    socket = urllib.urlopen(url)
    html = socket.read()
    parser = BeautifulSoup(html) 
    if level<depth:
      for link in parser.find_all('a'):
        new_url = link.get('href')
        print new_url
        if domain:          
          if same_domain(url, new_url):          
            if (new_url != url) and (new_url!='/') and (new_url!='#'):
              if (new_url not in result) :
                result.append(new_url)
                collect(new_url, result, depth, level+1)
              else:
                print "Exists"
            else:
              print "Exists"
          else:
            print "Different domain from parent url"
        else:
          if (new_url != url) and (new_url!='/') and (new_url!='#'):
            if (new_url not in result) :
              result.append(new_url)
              collect(new_url, result, depth, level+1)
            else:
              print "Exists"
          else:
            print "Exists"          
  except Exception, ex:
    print ex
  return result
  
if __name__ == "__main__":
  result = []
  depth =2
  print len(collect('http://ibnlive.com', result, depth, 0, domain=True)  )

