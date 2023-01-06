import urllib.parse
from http.cookies import SimpleCookie


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
    ps = SimpleCookie()
    ps.load(query)
    pr_cook = {a: b.value for a, b in ps.items()}
    return pr_cook


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Marina;age=18;') == {'name': 'Marina', 'age': '18'}
    assert parse_cookie('work=NP;year=6;') == {'work': 'NP', 'year': '6'}
    assert parse_cookie('name=Artem;age=24;') == {'name': 'Artem', 'age': '24'}
    assert parse_cookie(';') == {}
    assert parse_cookie('///...????&&&;') == {}
    assert parse_cookie('left = right;') == {'left': 'right'}
    assert parse_cookie('1;1;1;1;3;3;3;3;3') == {}
    assert parse_cookie('1$ = 41UAN') == {'1$': '41UAN'}
    assert parse_cookie('cars=BMW;year=2007;') == {'cars': 'BMW', 'year': '2007'}
    assert parse_cookie('::::::;;;;;;;') == {}
