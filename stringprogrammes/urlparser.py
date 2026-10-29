# Given a url parse it into protocal, domain, and path

#url = input('Enter URL:')

url = 'http://www.kaggle.com/datasets'

protocol = url[ : url.find(':')]

dot1 = url.find('.')
dot2 = url.find('.', dot1+1)
domain = url[ dot1+1 : dot2] 
 
page = url[url.find('/', dot2):]

print('Protocol:', protocol)
print('Domain:', domain)
print('RequestParam:', page)