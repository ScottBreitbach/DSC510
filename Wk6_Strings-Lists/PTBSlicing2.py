# slicing values out of a string

sample_url = 'http://coryms.com'
print(sample_url)

print(sample_url[::-1])     # reverse the url
print(sample_url[-4:])      # print top level domain
print(sample_url[7:])       # print w/o http
print(sample_url[7:-4])     # trim http and domain
