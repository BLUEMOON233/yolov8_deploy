from ultralytics import YOLO

model = YOLO('yolov8x.pt')

model.export(format='onnx')