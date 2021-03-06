def parse_url_and_method(resource):
    index = resource.rindex('/')
    (url, method) = (resource[:index], resource[index + 1:])
    return (url, method)


def reguster_resources():
    resources = {}
    while True:
        line = input()
        if line == 'END':
            break
        (url, method) = parse_url_and_method(line)
        if url not in resources:
            resources[url] = set()

        resources[url].add(method)

    return resources


def read_request():
    (method, url, _) = input().split()
    return (method.lower(), url)


def error_message():
    return '''HTTP/1.1 404 Not Found
Content-Length: 9
Content-Type: text/plain

Not Found
'''


def succes_message():
    return '''HTTP/1.1 200 OK
Content-Length: 2
Content-Type: text/plain

OK
'''


def solve():
    resources = reguster_resources()
    (method, url) = read_request()

    if url not in resources:
        return error_message()

    if method not in resources[url]:
        return error_message()

    return succes_message()


print(solve())
