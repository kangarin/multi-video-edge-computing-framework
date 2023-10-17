# import redis   # 导入redis 模块
# import time
# import random

# if __name__ == '__main__':
#     r = redis.Redis(host='localhost', port=6379, decode_responses=True)  
#     for i in range(100):
#         print(r.get("count"))
#         randTime = random.randint(1, 5)
#         time.sleep(randTime)


import json
import redis
import time

# 连接到 Redis
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

old_data = {}

# 循环读取数据
while True:
    # 从 Redis 中读取数据
    data = redis_client.get('data_key')
    
    if data:
        # 将 JSON 数据解析成字典
        data_dict = json.loads(data)
        if data_dict == old_data:
            continue
        
        # 输出 count 值
        for node, services in data_dict["nodes"].items():
            for service_info in services:
                service = service_info["svc"]
                count = service_info["count"]
                nowTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                print(f'Node: {node}, Service: {service}, Count: {count} at {nowTime}')
        old_data = data_dict
    # 休眠一段时间，以免频繁读取
    time.sleep(2)
