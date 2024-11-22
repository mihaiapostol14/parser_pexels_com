def f(value=''):
    s = 'https://www.pexels.com/search/hd%20desktop%20backgrounds/'
    value = value.replace(' ', '%20')

    return f'https://www.pexels.com/search/{value}/'

print(f(value='car'))