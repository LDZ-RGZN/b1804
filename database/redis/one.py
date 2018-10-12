from redis import *

if __name__ == '__main__':
    try:
        sr = StrictRedis()
        result = sr.get('name')
        print(result)
    except Exception as e:
        print(e)





















