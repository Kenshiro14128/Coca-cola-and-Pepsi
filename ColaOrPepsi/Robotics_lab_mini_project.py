# Imported Libaries
import cv2
from datetime import datetime
from ultralytics.yolo.engine.model import YOLO

# Import model
model = YOLO('best.pt')

# Run model and run camera
results = model.predict(source='0', show=True, conf=0.5, save_conf = True, stream = True)

# Count number of boxes deteced
for r in results:
    print("Num of detected: ",len(r))