from urllib import parse


def decode(encoded_url):
    return parse.unquote(encoded_url)

print(decode('http://www.google.bg/search?q=C%23'))