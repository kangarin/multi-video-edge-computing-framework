import sys

# 应用原型，各个阶段可能需要多个线程实例执行
class AppPrototype:
    def __init__(self, config):
        self.config = config
        self.video_streams = []
        self.stages = []
        self.generators = []
        self.integrator = None
        
        self.load_video_streams()
        self.load_stages()
        self.bind_generators_to_video_streams()
        self.integrator = self.load_integrator()

    
    def load_stages(self):
        base_path = self.config["code_base_path"]
        sys.path.append(base_path)
        for stage_config in self.config["stages"]:
            stage_module = __import__(stage_config["module"])
            stage_class = getattr(stage_module, stage_config["class"])
            stage_args = stage_config["init_args"]
            stage = stage_class(stage_args)
            self.stages.append((stage_config["stage_name"] , stage))
        print(self.stages)

    def load_video_streams(self):
        for video_stream_config in self.config["video_streams"]:
            name = video_stream_config["name"]
            url = video_stream_config["url"]
            type = video_stream_config["type"]
            edge_id = video_stream_config["edge_id"]
            self.video_streams.append((name, url, type, edge_id))
        print(self.video_streams)

    def load_generator(self):
        generator_config = self.config["generator"]
        base_path = self.config["code_base_path"]
        sys.path.append(base_path)
        generator_module = __import__(generator_config["module"])
        generator_class = getattr(generator_module, generator_config["class"])
        generator_args = generator_config["init_args"]
        return generator_class(generator_args)

    def load_integrator(self):
        integrator_config = self.config["integrator"]
        base_path = self.config["code_base_path"]
        sys.path.append(base_path)
        integrator_module = __import__(integrator_config["module"])
        integrator_class = getattr(integrator_module, integrator_config["class"])
        integrator_args = integrator_config["init_args"]
        return integrator_class(integrator_args)

    def bind_generators_to_video_streams(self):
        for video_stream in self.video_streams:
            gen = self.load_generator()
            gen.bind(video_stream)
            self.generators.append(gen)

    def run(self):
        for generator in self.generators:
            generator()
        for stage in self.stages:
            print(stage[0])
            stage[1](None)
        self.integrator()
