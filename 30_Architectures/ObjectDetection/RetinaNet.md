# RetinaNet

---

This is a placeholder document for the **RetinaNet** architecture.

**RetinaNet** is a single-stage object detector that addresses the extreme class imbalance between foreground and background classes during training. It introduces a novel loss function called **Focal Loss** to solve this problem, enabling it to achieve the accuracy of two-stage detectors while maintaining the speed of single-stage detectors.

You can add more content here explaining:
- The problem of class imbalance in single-stage detectors.
- How **Focal Loss** works by down-weighting the loss assigned to well-classified examples, allowing the model to focus on hard, misclassified examples.
- The network architecture, which typically combines a backbone network (like ResNet) with a Feature Pyramid Network (FPN).
- Its impact on the development of subsequent object detection models.

---

## 연관 개념

- [[SSD]]
- [[YOLOv1]]
- [[Feature Pyramid Network]]
- [[Class Imbalance]]
- [[Focal Loss]]
