---
title: TimeSformer (facebookresearch 코드 구조)
aliases:
  - TimeSformer 코드베이스
  - TimeSformer 구현 정리
  - TimeSformer 모델 구조 (코드)
tags:
  - computer-vision
  - video
  - transformer
  - implementation
  - pytorch
topics:
  - timesformer
  - divided-space-time
  - video-classification
source:
  - https://github.com/facebookresearch/TimeSformer
---
# TimeSformer (facebookresearch) 모델 구조

## 개요
- TimeSformer 구현의 중심은 ViT 기반 토큰화와 분리된 시공간 어텐션이며, 핵심 모듈은 `timesformer/models/vit.py:VisionTransformer`와 `timesformer/models/vit.py:Block`에 있다.
- 학습/추론 흐름은 `tools/run_net.py:main`에서 설정을 로드한 뒤 `tools/train_net.py:train` 또는 `tools/test_net.py:test`로 분기한다.
이 구성요소들이 어떻게 조립되는지 다음 섹션에서 모듈 관점으로 정리한다.

## 아키텍처
- 패치 임베딩은 입력 비디오를 프레임 단위로 펼친 뒤 Conv2d로 패치화하며, 구현은 `timesformer/models/vit.py:PatchEmbed`에 있다.
- 위치/시간 임베딩과 CLS 토큰 결합, 임베딩 리사이즈 로직은 `timesformer/models/vit.py:VisionTransformer.forward_features`에서 처리된다.
- 분리 시공간 어텐션은 temporal → spatial 순서로 적용되며, CLS 토큰을 프레임별로 평균내는 로직까지 포함되어 `timesformer/models/vit.py:Block.forward`에 구현되어 있다.
- 분류 헤드는 `timesformer/models/vit.py:VisionTransformer`의 `head`와 `forward`에서 로짓을 생성하며, 외부에서 감싸는 래퍼는 `timesformer/models/vit.py:TimeSformer`이다.
- 모델 선택은 레지스트리 기반으로 동작하며, `timesformer/models/build.py:build_model`이 `timesformer/models/vit.py:vit_base_patch16_224`(및 `TimeSformer`)로 매핑한다.
위 구조가 실제 입력을 어떻게 통과하는지 데이터 흐름으로 이어서 본다.

## 데이터 흐름
- 데이터셋은 비디오를 디코딩해 `channel x num_frames x height x width` 프레임 텐서를 반환하며, Kinetics 기준 동작은 `timesformer/datasets/kinetics.py:Kinetics.__getitem__`에 정의되어 있다.
- 로더는 split에 맞는 데이터셋을 구성하고 배치/샘플러를 조합하며, 진입 함수는 `timesformer/datasets/loader.py:construct_loader`이다.
- 학습 루프에서 입력은 GPU로 이동한 뒤 `model(inputs)`로 전달되며, 믹스업/손실 계산을 포함한 핵심 스텝은 `tools/train_net.py:train_epoch`에 있다.
- 모델 내부에서는 `timesformer/models/vit.py:PatchEmbed.forward`가 패치 토큰을 만들고, `timesformer/models/vit.py:VisionTransformer.forward_features` → `timesformer/models/vit.py:Block.forward`를 거쳐 CLS 토큰을 산출한다.
- 최종 로짓은 `timesformer/models/vit.py:VisionTransformer.forward`에서 head를 통과해 출력된다.
이 흐름을 호출하는 학습/추론 엔트리포인트를 다음에 정리한다.

## 학습/추론 엔트리포인트
- 실행 진입은 `tools/run_net.py:main`이며, 설정 로드는 `timesformer/utils/parser.py:load_config`, 멀티 GPU 실행은 `timesformer/utils/misc.py:launch_job`에서 처리한다.
- 학습 진입점은 `tools/train_net.py:train`이고, 모델 생성은 `timesformer/models/build.py:build_model`, 체크포인트 로드는 `timesformer/utils/checkpoint.py:load_train_checkpoint`에서 수행한다.
- 추론/테스트 진입점은 `tools/test_net.py:test`이며, 가중치 로드는 `timesformer/utils/checkpoint.py:load_test_checkpoint`, 멀티뷰 평가 루프는 `tools/test_net.py:perform_test`에 있다.
이 엔트리포인트가 읽는 설정 파일 구성을 이어서 살펴본다.

## 설정 파일
- 기본 설정 스키마는 `timesformer/config/defaults.py:get_cfg`로 로드되며, TimeSformer 전용 옵션은 `_C.TIMESFORMER`에 정의되어 있다(확인 필요: `timesformer/config/defaults.py:get_cfg` 주변).
- 대표 실험 설정은 `timesformer/utils/parser.py:load_config`가 YAML을 병합하며, 예시는 `configs/Kinetics/TimeSformer_divST_8x32_224.yaml`, `configs/SSv2/TimeSformer_divST_8_224.yaml`이다.
설정이 기대하는 의존성을 다음 섹션에서 정리한다.

## 의존성
- 핵심 런타임 의존성은 `setup.py:setup`의 `install_requires`에 있는 `torch`, `einops`이며, 모델 구현에서도 해당 패키지를 직접 사용한다(`timesformer/models/vit.py:VisionTransformer`).
- 믹스업은 `tools/train_net.py:train_epoch`에서 `timm`을 사용하므로 활성화 시 별도 설치가 필요할 수 있다(확인 필요: 배포 환경에서 `timm` 포함 여부).
의존성을 충족했다면, 확장 가능한 지점을 마지막으로 정리한다.

## 확장 포인트
- 신규 모델은 레지스트리에 등록하는 방식으로 확장하며, 흐름은 `timesformer/models/build.py:build_model`과 예시 구현인 `timesformer/models/vit.py:vit_base_patch16_224`를 참고한다.
- 어텐션 변형은 `timesformer/models/vit.py:Block`의 `attention_type` 분기에서 확장할 수 있고, 설정은 `timesformer/config/defaults.py:get_cfg` 및 각 YAML에 추가하면 된다.
- 데이터셋 추가는 `timesformer/datasets/build.py:build_dataset` 레지스트리 패턴을 따르며, 기존 구현은 `timesformer/datasets/kinetics.py:Kinetics`, `timesformer/datasets/ssv2.py:Ssv2`에 있다.
마지막으로 참고 링크를 정리한다.

## 참고
- GitHub: https://github.com/facebookresearch/TimeSformer
