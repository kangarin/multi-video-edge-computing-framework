import docker
import psutil
import time

# 创建一个Docker客户端
client = docker.from_env()

# 启动容器
container = client.containers.run("nginx", detach=True, command="tail -f /dev/null")

# 获取容器ID
container_id = container.id

try:
    while True:
        # 获取容器的状态信息
        # container_stats = container.stats(stream=False)
        # print(container_stats)

        # # 获取 CPU 使用率的详细信息
        # cpu_usage = container_stats["cpu_stats"]["cpu_usage"]

        # # 获取总使用时间和用户模式使用时间
        # total_usage = cpu_usage["total_usage"]
        # usage_in_usermode = cpu_usage["usage_in_usermode"]

        # # 计算 CPU 使用率
        # cpu_percent = (usage_in_usermode / total_usage) * 100

        # print(f"Container CPU Utilization: {cpu_percent:.2f}%")

        docker_stats = container.stats(stream=False)
        cpuDelta = docker_stats.get("cpu_stats").get("cpu_usage").get("total_usage") - docker_stats.get("precpu_stats").get(
            "cpu_usage").get("total_usage")
        print(cpuDelta)

        systemDelta = docker_stats.get("cpu_stats").get("system_cpu_usage") - docker_stats.get("precpu_stats").get(
            "system_cpu_usage")
        print(systemDelta)
        result = cpuDelta / systemDelta * 100
        print("cpu % =",result)

        
        time.sleep(5)






except KeyboardInterrupt:
    # 在键盘中断时（Ctrl+C），停止获取状态并关闭容器
    container.stop()
    container.remove()
