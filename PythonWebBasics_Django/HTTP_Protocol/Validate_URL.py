from urllib import parse


def get_host(netloc):
    if '.' not in netloc:
        return None
    if ':' in netloc:
        return netloc.split(':')[0]
    return netloc


def get_port(netloc, scheme):
    if ':' in netloc:
        return netloc.split(':')[1]
    if scheme == 'http':
        return 80
    elif scheme == 'https':
        return 443
    return None


def get_path(path):
    return path or '/'


def get_protocol(scheme):
    if scheme in ('http', 'https'):
        return scheme
    return None


def validate_url(url):
    components = parse.urlparse(url)
    result = {
        'Protocol': get_protocol(components.scheme),
        'Host': get_host(components.netloc),
        'Port': get_port(components.netloc, components.scheme),
        'Path': get_path(components.path),
        'Query': components.query,
        'Fragment': components.fragment
    }
    required_components_names = [
        'Protocol',
        'Host',
        'Port',
        'Path'
    ]
    optional_component_names = [
        'Fragment',
        'Query'
    ]

    are_required_components_present = all(result[name] for name in required_components_names)
    if are_required_components_present:
        for component_name in (required_components_names + optional_component_names):
            if result[component_name]:
                print(f'{component_name}: {result[component_name]}')
    else:
        print('Invalid URL')


# validate_url('http://mysite.com:80/demo/index.aspx')

valid_tests = [
    'http://mysite.com:80/demo/index.aspx',
    'https://my-site.bg',
    'https://mysite.bg/demo/search?id=22o#go',
]

invalid_tests = [
    'https://mysite:80/demo/index.aspx',
    'https/mysite.bg?id=2',
    'somesite.com:80/search?',
]

[validate_url(url) for url in valid_tests + invalid_tests]
