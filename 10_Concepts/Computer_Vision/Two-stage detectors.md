# Two-stage detectors

---

This is a placeholder document for **Two-stage detectors**.

**Two-stage detectors** are a class of object detection models that break the detection process into two distinct stages:

1.  **Region Proposal**: In the first stage, the network generates a sparse set of candidate object locations (region proposals) where objects are likely to be.
2.  **Classification and Refinement**: In the second stage, these proposals are classified into foreground classes (or background), and their bounding box coordinates are regressed to more accurately fit the object.

You can add more content here explaining:
- The typical architecture, including a Region Proposal Network (RPN).
- Key examples like the R-CNN family (R-CNN, Fast R-CNN, Faster R-CNN, Mask R-CNN).
- **Advantages**: Generally higher accuracy, especially for small objects and precise localization.
- **Disadvantages**: Typically slower than one-stage detectors due to the two-step process.

---

## 연관 개념

- [[One-stage detectors]]
- [[Faster R-CNN]]
- [[R-CNN]]
- [[Region Proposal Network]]
