# One-stage detectors

---

This is a placeholder document for **One-stage detectors**.

**One-stage detectors** (also known as single-shot detectors) are a class of object detection models that predict object bounding boxes and class probabilities directly from the input image in a single pass. They do not have a separate region proposal stage.

You can add more content here explaining:
- How they work by treating object detection as a regression problem, directly predicting box coordinates and class labels from feature maps.
- Key examples like the YOLO family, SSD, and RetinaNet.
- **Advantages**: Generally much faster than two-stage detectors, making them suitable for real-time applications.
- **Disadvantages**: Historically, they have lagged behind two-stage detectors in accuracy, often struggling with small objects and precise localization (though this gap has narrowed significantly with models like RetinaNet).

---

## 연관 개념

- [[Two-stage detectors]]
- [[YOLOv1]]
- [[SSD]]
- [[RetinaNet]]
