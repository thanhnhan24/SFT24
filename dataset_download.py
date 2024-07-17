from roboflow import Roboflow
def ver5():
    rf = Roboflow(api_key="tuyh4U9leBSteYuOM0SF")
    project = rf.workspace("main-orgu1").project("sft24-facedetect")
    version = project.version(5)
    dataset = version.download("yolov8")

def ver6_grayscale():
    rf = Roboflow(api_key="tuyh4U9leBSteYuOM0SF")
    project = rf.workspace("main-orgu1").project("sft24-facedetect")
    version = project.version(6)
    dataset = version.download("yolov8")

def thnhan():

    rf = Roboflow(api_key="tuyh4U9leBSteYuOM0SF")
    project = rf.workspace("main-orgu1").project("thnhan_facedetection")
    version = project.version(2)
    dataset = version.download("yolov8")

thnhan()