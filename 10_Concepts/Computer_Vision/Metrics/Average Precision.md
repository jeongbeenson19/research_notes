
AP는 **Average Precision**의 약자로, **객체 탐지(Object Detection)**, **정보 검색(Information Retrieval)**, **분류(Classification)** 등의 분야에서 **정밀도(Precision)** 와 **재현율(Recall)** 의 관계를 종합적으로 평가하는 **단일 수치의 지표**입니다.

---

### 📌 정의

AP는 보통 **[[Evaluation Metrics#^941fcf|Precision]]-[[Evaluation Metrics#^1d4e7f|Recall]] 곡선의 아래 면적 (Area Under Curve, AUC)** 을 의미하며, 다음과 같이 정의됩니다:

$$\text{AP} = \int_{0}^{1} \text{Precision}(r) \, dr$$

여기서 $r$은 Recall 값입니다. 즉, Recall 값이 0부터 1까지 변할 때 Precision이 어떻게 변하는지의 **전체적인 평균을 계산**한 것입니다.

---

### 📌 주요 특징

- **객체 탐지**에서는 보통 클래스별로 AP를 계산한 후, 이를 평균 낸 **mAP (mean Average Precision)** 를 사용합니다.
    
- AP는 **모델이 얼마나 정확하게 탐지했는지**를 종합적으로 보여줍니다.
    
- P-R 커브가 **우상향 형태**를 띨수록 높은 AP를 가지게 됩니다.
    

---

### 📌 예시: 객체 탐지에서의 AP

객체 탐지에서 AP는 일반적으로 **IoU (Intersection over Union)** 기준을 두고 계산됩니다. 예:

- **AP@0.5**: IoU가 0.5 이상인 경우를 TP로 간주
    
- **AP@0.5:0.95**: IoU를 0.5부터 0.95까지 0.05 간격으로 10단계로 계산한 평균값
    

---

### 📌 옵시디언 카테고리 추천

```
MILAB
└── Computer Vision
    └── Metrics
        └── Average Precision.md
```

혹은 `Evaluation Metrics`라는 폴더를 따로 만드는 것도 적절합니다.

---

필요하면 수식, P-R 커브 도식, AP 계산 알고리즘도 예시로 보여줄 수 있습니다.