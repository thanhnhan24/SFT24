from roboflow import Roboflow
rf = Roboflow(api_key="tuyh4U9leBSteYuOM0SF")
project = rf.workspace("main-orgu1").project("thnhan_facedetection")
version = project.version(1)
dataset = version.download("yolov8")
