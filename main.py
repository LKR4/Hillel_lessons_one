import urllib.parse


def parse(url: str) -> dict:
    fragment = urllib.parse.urlparse(url).query
    params = dict(urllib.parse.parse_qsl(fragment))
    return params


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/') == {}
    assert parse('https://example.com/?') == {}
    assert parse('https://example.com/?name=Dima') == {'name': 'Dima'}
    assert parse('https://example.com/path/to/page?cars=bmw&serial=m3') == {'cars': 'bmw', 'serial': 'm3'}
    assert parse('https://example.com/path/to/page?cars=mercedes&serial=G63') == {'cars': 'mercedes', 'serial': 'G63'}
    assert parse('https://example.com/path/to/page?cars=ferrari&serial=alpha') == {'cars': 'ferrari', 'serial': 'alpha'}
    assert parse('https://example.com/path/to/page?cars=chevrolet') == {'cars': 'chevrolet'}
    assert parse('https://example.com/path/to/page?icons=jpg') == {'icons': 'jpg'}
    assert parse('https://example.com/path/to/page?') == {}
    assert parse('https://example.com/path/to/') == {}
    assert parse('https://example.com/path&') == {}
    assert parse('https://example.com/path/to/page?school=Hillel') == {'school': 'Hillel'}
    assert parse('https://example.com/path?lessons=3') == {'lessons': '3'}


def parse_cookie(query: str) -> dict:
    return {}


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
