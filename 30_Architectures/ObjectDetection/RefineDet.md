# RefineDet (Single-Shot Refinement Neural Network for Object Detection)

---

This is a placeholder document for the **RefineDet** architecture.

**RefineDet** is an object detection model that aims to combine the merits of both one-stage and two-stage detectors. It consists of two interconnected modules: the Anchor Refinement Module (ARM) and the Object Detection Module (ODM).

You can add more content here explaining:
- How the **Anchor Refinement Module (ARM)** filters out negative anchors to reduce the search space for the classifier and refines the locations of the remaining anchors.
- How the **Object Detection Module (ODM)** takes the refined anchors as proposals to further improve regression and predict multi-class labels.
- The **Transfer Connection Block (TCB)** which connects the ARM and ODM.
- How this architecture helps to overcome the class imbalance problem and improve accuracy, especially for small objects.

---

## 연관 개념

- [[SSD]]
- [[Faster R-CNN]]
- [[Two-stage detectors]]
- [[One-stage detectors]]
