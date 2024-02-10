from roboflow import Roboflow
rf = Roboflow(api_key="LoxY7TYMujj5dhGJQAvN")
project = rf.workspace("telkom-university-surabaya-6o94q").project("ternakpark")
dataset = project.version(5).download("yolov8")
