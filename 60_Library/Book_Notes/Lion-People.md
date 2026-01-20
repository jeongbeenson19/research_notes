
[[ANN]]

[[CNN]]

[[LeNet]]
- 최초의 CNN 중 하나, MNIST에 사용됨
- Conv -> Pool -> Conv -> Pool -> FC
-  후속 CNN 구조의 기초가 됨

[[AlexNet]]
- LeNet 구조를 크게 확장
	- 더 깊은 레이어, ReLU 활성화 함수, Dropout, GPU 병렬화
- 딥러닝 부흥의 시작
- convolutional layer 바로 뒤에 convolutional layer가 연결됨

[[ZFNet]]
- AlexNet의 개선 버전(hyper-parameter를 수정, convolutional layer의 크기를 늘림)
- 커널 크기 및 스트라이드 최적화
- CNN 내부 시각화 기법 도입 -> 어떤 feature를 보는지 이해 가능

[[VGGNet]]
- 단순한 구조: 3x3 conv, 2x2 max-pooling 반복
- 깊이를 16~19층까지 증가
- GoogLeNet에 비해 분류 성능은 약간 떨어졌지만 다중 전달 학습 과제에서는 더 좋은 결과가 나옴
- 구조가 단순해서 후속 네트워크들의 baseline으로 많이 사용됨

[[OverFeat]]
- 분류 + 위치 예측 + 탐지까지 수행한 초기 멀티태스크 CNN
- classification + localization 학습을 통합적으로 처리

[[GoogLeNet]]
- Inception 모듈 도입 -> 다양한 크기의 conv 병렬 적용
- 효율성과 성능을 동시에 챙김
- depth는 깊지만 연산량은 절감

[[ResNet]]
- Residual Connection으로 gradient vanishing 문제 해결
- 수백 개 레이어까지도 학습 -> CNN 깊이의 한계를 뛰어넘음
- 이후 대부분의 구조가 ResNet 기반을 따름

---

[[SIFT]]
- CNN은 아니지만, 이미지에러 로컬 특징을 추출하는 대표적인 전통적 방법
- CNN 기반 이전에는 이미지 분류나 물체 익식에서 주로 사용
- 이후 CNN 기반이 SIFT를 대체하게 됨

---

[[R-CNN]]
- CNN을 object detection에 처음 적용
- 과정: selective search -> region proposal -> 각각 CNN 적용 -> SVM 분류
- 느림

[[SPPNet]]
- Fast R-CNN의 전신
- RoI Pooling의 아이디어 기반: 다양한 크기의 입력을 처리 가능(Spatial Pyramid Pooling)
- 이후 Fast R-CNN에 통합됨

[[30_Architectures/ObjectDetection/Fast R-CNN|Fast R-CNN]]
- R-CNN 개선: 이미지 전체 CNN 한 번 적용 + RoI Pooling
- 속도와 정확도 향상

[[Faster R-CNN]]
- 후보 영역을 추천하기 위한 RPN(Region Proposal Network)가 존재
