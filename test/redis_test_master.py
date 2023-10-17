# import redis   # 导入redis 模块
# import time
# import random

# if __name__ == '__main__':
#     r = redis.Redis(host='localhost', port=6379, decode_responses=True)  
#     for i in range(100):
#         r.set("count", i)
#         randTime = random.randint(1, 5)
#         time.sleep(randTime)

import json
import random
import redis
import time

# 连接到 Redis
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

# 初始的 JSON 数据
data = {
    "nodes": {
        "node1": [{"svc": "svc1", "count": "3"}],
        "node2": [{"svc": "svc2", "count": "2"}]
    }
}

# 50次循环
for i in range(50):
    # 随机选择要改变的节点和服务
    node = random.choice(list(data["nodes"].keys()))
    service = data["nodes"][node][0]["svc"]

    # 生成随机数作为新的count值
    new_count = random.randint(1, 10)
    
    # 更新数据
    data["nodes"][node][0]["count"] = str(new_count)
    
    # 将更新后的数据写入 Redis
    redis_client.set('data_key', json.dumps(data))
    nowTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(f'Updated: Node {node}, Service {service}, New Count: {new_count} at {nowTime}')
    
    # 休眠一段时间，模拟实际场景中的变化
    time.sleep(10)

