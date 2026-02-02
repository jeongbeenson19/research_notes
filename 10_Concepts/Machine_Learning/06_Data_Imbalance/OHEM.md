# OHEM (Online Hard Example Mining)

---

This is a placeholder document for **Online Hard Example Mining (OHEM)**.

**OHEM** is a training strategy used in machine learning, particularly in object detection, to handle class imbalance more effectively. Instead of using all examples in a mini-batch, OHEM selects "hard" examples—those on which the model performs poorly (i.e., have high loss)—to be used for backpropagation.

You can add more content here explaining:
- The problem of class imbalance in object detection (e.g., the vast number of background proposals vs. few object proposals).
- How OHEM works:
    1. Forward pass for all RoIs.
    2. Sort RoIs by their loss.
    3. Select the top-K RoIs with the highest loss.
    4. Perform the backward pass only on this selected subset.
- Its advantages over simpler negative mining strategies.
- Its use in models like Faster R-CNN.

---

## 연관 개념

- [[Faster R-CNN]]
- [[Hard Negative Mining]]
- [[Class Imbalance]]
