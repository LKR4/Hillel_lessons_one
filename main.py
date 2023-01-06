from http.cookies import SimpleCookie


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
    assert parse_cookie(':::;;;;;;;') == {}
