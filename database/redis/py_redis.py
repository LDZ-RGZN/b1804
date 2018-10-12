from rediscluster import *

if __name__ == '__main__':
    try:
        startup_nodes = [
                {'host':'10.114.12.242','port':'7000'},
                {'host':'10.114.12.242','port':'7001'},
                {'host':'10.114.12.242','port':'7002'},
            ]
        src = StrictRedisCluster(startup_nodes=startup_nodes,decode_responses=True)
        result = src.set('name','100cxy')
        print(result)
        name = src.get('name')
        print(name)
    except Exception as e:
        print(e)
















































