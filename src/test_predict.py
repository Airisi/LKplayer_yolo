from ultralytics import YOLO, settings

# View all settings
print(settings)

yolo = YOLO("weights/yolo26n.pt", task="detect")
result = yolo(source="datasets/lk_dataset/images/test/person_2.jpg", save=True)
