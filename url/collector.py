'''
Created on 27-May-2015

@author: Admin
'''
import urllib

def collect(url):
  result = []
  socket = urllib.urlopen(url)
  html = socket.read()
  print html  
  return result
  
if __name__ == "__main__":
  print collect('http://ibnlive.com')  

