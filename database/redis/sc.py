from redis import *
def main():
    sr = StrictRedis(decode_responses=True)
    sr.srem('name','lisi')
























if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)






























