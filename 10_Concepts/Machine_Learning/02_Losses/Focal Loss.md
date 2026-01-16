# Focal Loss

---

This is a placeholder document for **Focal Loss**.

**Focal Loss** is a loss function designed to address the problem of class imbalance in single-stage object detectors like RetinaNet. It is a dynamically scaled cross-entropy loss, where the scaling factor decays to zero as confidence in the correct class increases.

You can add more content here explaining:
- The limitations of standard Cross-Entropy loss in the presence of extreme class imbalance.
- The mathematical formulation of Focal Loss:
  `FL(p_t) = -α_t * (1 - p_t)^γ * log(p_t)`
- The roles of the focusing parameter `γ` (gamma) and the balancing parameter `α` (alpha).
- How it effectively down-weights the loss from easy examples (well-classified negatives), allowing the model to focus on learning hard examples.

---

## 연관 개념

- [[RetinaNet]]
- [[Class Imbalance]]
- [[Cross-Entropy Loss]]
- [[Object Detection]]
