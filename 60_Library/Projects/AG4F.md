
## Auto-Graphic 4 Football
---
```python
import cv2


# 사람 검출기 초기화
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
threshold = 0.6  

# 비디오 열기
cap = cv2.VideoCapture("sample2.mp4")
paused = False
frame = None
ellipses = [] # [(center, axes)]
selected_points = []
lines = []


# 마우스 콜백 함수
def click_event(event, x, y, flags, param):
global selected_points, lines, ellipses

margin = 50 # 중심 주변 10픽셀 여유 추가

if event == cv2.EVENT_LBUTTONDOWN:
for center, axes in ellipses:
cx, cy = center
ax, ay = axes

# 타원 내부 판단 + margin 적용
if ((x - cx)**2) / ((ax + margin)**2) + ((y - cy)**2) / ((ay + margin)**2) <= 1:
	cv2.ellipse(display, center, axes, 0, 0, 360, (0, 0, 0), -1)
	selected_points.append(center)	
	break

if len(selected_points) == 2:
	pt1, pt2 = selected_points
	lines.append((pt1, pt2))
	selected_points = []
elif event == cv2.EVENT_RBUTTONDOWN:
	lines.clear()
	selected_points.clear()

# 윈도우 설정 및 콜백 등록
cv2.namedWindow("Video")
cv2.setMouseCallback("Video", click_event)

while cap.isOpened():
	if not paused:
		ret, frame = cap.read()
	if not ret:
		print("영상이 끝났거나 오류 발생")
		break

display = frame.copy()

# 타원 다시 그림
for center, axes in ellipses:
cv2.ellipse(display, center, axes, 0, 0, 360, (50, 50, 50), -1)

# 선 다시 그림
for pt1, pt2 in lines:
cv2.line(display, pt1, pt2, (0, 0, 255), 5)

# 출력
cv2.imshow("Video", display)
key = cv2.waitKey(30) & 0xFF

if key == 27: # ESC
	break
elif key == ord(' '): # 스페이스바
	paused = not paused
	if paused:
	# 사람 검출 수행
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
	eq = clahe.apply(gray)
	color_eq = cv2.cvtColor(eq, cv2.COLOR_GRAY2BGR)
	boxes, weights = hog.detectMultiScale(
	color_eq, winStride=(4, 4), padding=(8, 8), scale=1.03
	)
	
	ellipses.clear()
	
	for (box, weight) in zip(boxes, weights):
		if weight < threshold:
			continue
		x, y, w, h = box
		center = (x + w // 2, y + h)
		axes = (w // 3, h // 15)
		ellipses.append((center, axes))

cap.release()
cv2.destroyAllWindows()
```


## 코드 해석
---

### 🔧 1. 초기 설정

```python
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
threshold = 0.6
```

#### 🧩 2. `cv2.HOGDescriptor_getDefaultPeopleDetector()`

- OpenCV가 제공하는 **사람(Human)** 전용 HOG + SVM 모델입니다.
    
- 구체적으로는, 사람 전신을 탐지하기 위해 사전 학습된 SVM의 **weight vector**를 반환합니다.
    

즉, 이 함수는 아래처럼 생긴 **numpy 배열 형태의 SVM weight 벡터**를 리턴합니다:

``` python
array([ 0.034, -0.025, ..., 0.067], dtype=float32)`
```
이는 HOG 특징을 입력했을 때 사람인지 아닌지를 판단해주는 **linear SVM의 weight 값**입니다.

---

#### 🧩 3. `hog.setSVMDetector(...)`

- HOG 특징을 추출한 후, 어떤 방식으로 사람인지 아닌지를 판단할지를 결정합니다.
    
- 여기서 `cv2.HOGDescriptor_getDefaultPeopleDetector()`를 넘겨줌으로써,  
    → HOG 특징 + 사전학습된 SVM 조합으로 **사람 검출**이 가능해집니다.
    

즉, 이 함수 호출로 **"이 HOG 객체는 사람을 찾을 수 있게 준비됐어!"** 라고 세팅하는 것입니다.
    
- `threshold` : 검출된 사람의 신뢰도 필터링 임계값입니다.
    

---

### 🎥 2. 비디오 열기

```python
cap = cv2.VideoCapture("sample2.mp4")
```

- 지정한 동영상 파일(`sample2.mp4`)을 프레임 단위로 읽기 위해 열어줍니다.
    

---

### 🖱️ 3. 마우스 콜백 함수 (`click_event`)

```python
cv2.setMouseCallback("Video", click_event)
```

- 사용자가 프레임 위 타원을 클릭하면, 해당 인물의 중심점을 저장합니다.
    
- 두 점이 선택되면 선이 그려지고, 우클릭 시 모든 선과 선택 초기화.
    

내부 구조:

```python
if ((x - cx)**2) / ((ax + margin)**2) + ((y - cy)**2) / ((ay + margin)**2) <= 1:
```

- 마우스 좌표가 타원 안에 있는지 확인하는 수식 (타원 방정식).
    

---

### ⏸️ 4. 스페이스바 누르면 일시정지 & 사람 검출

```python
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
clahe = cv2.createCLAHE(...)
eq = clahe.apply(gray)
color_eq = cv2.cvtColor(eq, cv2.COLOR_GRAY2BGR)
boxes, weights = hog.detectMultiScale(...)
```

- 프레임을 흑백으로 변환하고, CLAHE(적응적 히스토그램 평활화)를 적용해 **명암 대비 향상**.
    
- `hog.detectMultiScale(...)` : 보행자 검출 수행.
    
- 검출된 사람의 위치에 타원을 그림 (`cv2.ellipse`) → 바닥 중심을 기준으로 작고 납작한 타원.
    

---

### 🖼️ 5. 타원 및 선 시각화

```python
for center, axes in ellipses:
    cv2.ellipse(display, center, axes, ...)

for pt1, pt2 in lines:
    cv2.line(display, pt1, pt2, ...)
```

- 감지된 사람들마다 회색 타원을 그립니다.
    
- 사용자가 선택한 두 인물 간 빨간 선을 그림.
    

---

### ⌨️ 6. 키 입력 처리

```python
key = cv2.waitKey(30) & 0xFF
```

- `ESC` : 종료
    
- 스페이스바 (`' '`) : 재생/일시정지 전환 및 검출 수행 트리거
    

---

### 📤 7. 종료 처리

```python
cap.release()
cv2.destroyAllWindows()
```

- 비디오 파일 닫고 모든 창 제거.
    

---

### 📌 요약

|기능|설명|
|---|---|
|HOG 검출기|기본 사람 검출기 사용|
|CLAHE|명암 대비 개선으로 검출 정확도 향상|
|마우스 클릭|인물 선택 및 연결선 그리기|
|일시정지 상태에서만 검출|퍼포먼스 최적화|
|타원으로 사람 표시|시각적으로 인물 위치 명확화|

---
