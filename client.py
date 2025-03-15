import requests


def call_add_api(a, b):
    response = requests.get('http://0.0.0.0:8000/add', params={'a': a, 'b': b})
    if response.status_code == 200:
        print(f"Addition Result: {response.json()['result']}")
    else:
        print(f"Error: {response.json()['detail']}")


def call_subtract_api(a, b):
    response = requests.get('http://0.0.0.0:8000/subtract',
    params={
        'a': a,
        'b': b
    })
    if response.status_code == 200:
        print(f"Subtraction Result: {response.json()['result']}")
    else:
        print(f"Error: {response.json()['detail']}")


if __name__ == '__main__':
    call_add_api(10, 5)
    call_subtract_api(10, 5)
