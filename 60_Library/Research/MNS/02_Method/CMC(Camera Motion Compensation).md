
CMC(Camera Motion Compensation)은 연속 프레임 사이의 전역 2D 유사변환(스케일·회전)과 평행이동을 추정해, 카메라 움직임으로 인한 겉보기 이동을 추정하고 이를 추적 파이프라인에 명시적으로 보정하는 모듈입니다. 핵심 목적은 탐지-기반 칼만 예측과 관측 보정이 “고정 카메라” 가정에 끌려가지 않도록, 프레임 간 카메라 변화를 먼저 제거해 물체 자체의 운동 신호를 더 깨끗하게 쓰게 만드는 것입니다. <alphaxiv-paper-citation title="CMC Intro" page="2" first="As OC-SORT is" last="in moving scenes." />

구현 측면에서, 매 프레임 t에 대해 전역 유사변환 M_t = s_t R_t(스케일·회전)과 평행이동 T_t를 추정한 뒤, 이를 OC-SORT의 세 구성요소(OOS, OCM, OCR)에 동일하게 적용합니다. 이렇게 하면 관측 궤적 보정, 모멘텀 추정, 마지막 관측 위치가 모두 “카메라 보정 좌표계”에서 일관되게 계산됩니다. <alphaxiv-paper-citation title="Transform Scope" page="2" first="Given a scaled" last="components respectively:" />

OOS(online smoothing)에서는 “마지막으로 관측된 박스”의 중심을 변환해 보정된 시작점에서 보간 궤적을 만들고, 그 궤적으로 칼만 상태를 업데이트합니다. 이렇게 하면 카메라가 이동했더라도 궤적의 시작점이 실제 물체 이동에 맞춰집니다. <alphaxiv-paper-citation title="OOS Step" page="2" first="The center of" last="camera corrected measurement." />

OCM(momentum)에서는 최근 Δt 프레임의 박스 코너 점들을 각 프레임의 추정 변환으로 보정해가며, 그 시퀀스에서 박스의 각속도(방향 변화)를 계산합니다. 이때 각 시점 t마다 코너 점에 변환을 적용해 누적하면서, t−Δt부터 t까지의 변화량으로 모멘텀을 얻습니다. <alphaxiv-paper-citation title="OCM Step" page="2" first="At each timestep" last="during OCM." />

OCR(recovery)에서는 “마지막으로 본 박스”의 위치를 프레임마다 동일한 변환으로 갱신해, 가려짐 이후 재등장시 보정된 기준점을 사용해 복구 결합을 더 안정적으로 만듭니다. <alphaxiv-paper-citation title="OCR Step" page="2" first="For the last-seen" last="under CMC." />

이 보정은 칼만 필터의 내부 상태에도 직접 들어갑니다. 위치 상태(x_c, y_c)와 속도 상태(ẋ_c, ẏ_c) 및 해당 공분산 블록을 전역 회전·스케일 M_t와 평행이동 T_t로 선형 변환하여, 예측 이전 단계에서 상태 자체를 “카메라-보정 상태”로 재정렬합니다. <alphaxiv-paper-citation title="KF State" page="2" first="For OC-SORT, the" last="Kalman state:" />

적용 타이밍은 칼만 예측(extrapolation) 전에 수행합니다. 이렇게 해야 이후의 예측이 이미 카메라 보정된 상태공간에서 진행되어, 연속 프레임 간 정합 비용(예: IoU, 거리)이 카메라 이동이 아닌 물체 이동을 더 순수하게 반영합니다. <alphaxiv-paper-citation title="Timing" page="2" first="We apply this" last="corrected states." />

중요한 설계로, 영역(a)과 종횡비(s)는 변환으로 직접 갱신하지 않습니다. 회전된 물체의 외접 박스는 선형 근사가 잘 맞지 않고, 칼만 필터가 이런 근사 오차에 민감하기 때문입니다. 대신 중심·속도와 그 공분산만 신뢰성 있게 보정합니다. <alphaxiv-paper-citation title="Design Choice" page="2" first="We note that" last="aspect ratio s." />

실제 변환 추정은 OpenCV contrib의 VidStab을 사용해 특징점 추출, 옵티컬 플로우, RANSAC으로 강건한 전역 유사변환을 얻는 방식입니다. 이 접근은 다수의 기존 작업에서 검증된 전역 카메라 모션 추정 파이프라인을 그대로 따르며, 별도의 학습 없이 빠르게 적용할 수 있습니다. <alphaxiv-paper-citation title="Estimation" page="4" first="For CMC, we" last="works [3] choose." />

효과는 데이터셋 특성에 따라 달라집니다. 카메라 이동이 잦은 MOT17, DanceTrack에서는 유의한 향상을 보였고, 고정 카메라로 촬영된 MOT20에서는 개선이 거의 없었습니다. 즉, CMC는 샷 전환 감지나 컷 경계를 다루는 모듈이 아니라, 같은 샷 내 전역 카메라 모션을 상쇄해 트랙 결합을 안정화하는 역할에 최적화되어 있습니다.