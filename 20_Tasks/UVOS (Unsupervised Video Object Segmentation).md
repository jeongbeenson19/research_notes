# UVOS (Unsupervised Video Object Segmentation)

**비지도 비디오 객체 분할(Unsupervised Video Object Segmentation, UVOS)** 은 비디오 내에서 가장 두드러지거나 움직이는 주요 객체(primary object)를 분할(segmentation)하는 컴퓨터 비전 태스크입니다. 이름에서 알 수 있듯이, 이 작업은 분할 마스크(mask)에 대한 어떠한 수동적인 레이블링(manual annotation) 없이, 즉 **비지도(unsupervised)** 방식으로 수행됩니다.

## 핵심 목표

- **자동 객체 발견**: 비디오의 첫 프레임 또는 전체 시퀀스에서 가장 핵심이 되는 객체를 자동으로 식별합니다. 일반적으로 전경(foreground)에 있거나 다른 배경 요소와 뚜렷한 움직임을 보이는 객체가 대상이 됩니다.
- **시간적 일관성 유지**: 비디오의 모든 프레임에 걸쳐 식별된 객체의 분할 마스크를 일관되게 추적하고 생성합니다. 객체가 움직이거나, 모양이 변하거나, 다른 객체에 의해 잠시 가려지는 경우에도 동일한 객체로 인식하고 추적해야 합니다.

## 주요 접근 방식

UVOS는 주로 다음과 같은 정보들을 활용합니다.

- **모션 정보 (Motion Cues)**: 옵티컬 플로우(Optical Flow)와 같은 움직임 정보를 분석하여 배경과 움직이는 객체를 분리합니다. 이는 UVOS에서 가장 핵심적인 단서 중 하나입니다.
- **외형 정보 (Appearance Cues)**: 객체의 색상, 질감 등 시각적 특징을 활용하여 프레임 내에서 객체를 식별하고, 프레임 간에 동일한 객체임을 인식합니다.
- **시간적 일관성 (Temporal Coherence)**: 인접한 프레임 간에는 객체의 위치나 모양이 크게 변하지 않는다는 가정을 기반으로, 이전 프레임의 분할 결과를 다음 프레임에 전파(propagate)하거나 정제(refine)합니다.
- **메모리 네트워크 (Memory Networks)**: [[Out of Sight, Still in Mind]]와 같은 최근 연구에서는 메모리 네트워크를 사용하여 비디오의 장기적인 컨텍스트를 저장하고, 이를 통해 객체가 오래 가려져도 추적할 수 있도록 합니다.

## 평가 지표

- **J&F (Region Similarity & Contour Accuracy)**: 영역의 유사도를 측정하는 Jaccard Index (IoU)와 경계선의 정확도를 측정하는 F-measure의 평균값으로, UVOS 성능을 종합적으로 평가하는 주요 지표입니다.

## 관련 논문
- [[Out of Sight, Still in Mind|Out of Sight, Still in Mind: Reasoning and Planning about Unobserved Objects with Video Tracking Enabled Memory Models]]

## 관련 링크
- [[Video Object Segmentation]]
- [[Optical Flow]]
- [[Computer Vision]]