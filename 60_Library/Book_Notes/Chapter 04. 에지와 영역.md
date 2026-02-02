
에지 검출 알고리즘은 물체 내부는 명암이 서서히 변하고 물체 경계는 명암이 급격히 변하는 특성을 활용한다.

### 영상의 미분

$$
f'(x) = \lim_{\delta x \rightarrow 0} \frac{f(x+\delta x)-f(x)}{\delta x}
$$

정수 좌표를 쓰는 디지털 영상에서는 $x$의 최소 변화량이 1이므로 $\delta x$로 한다.

이 식을 필터 $u$로 컨볼루션하여  영상 $f$에 적용한다.
필터 $u$의 중심점은 왼쪽 화소다. 필터 $u$를 에지 연산자라고한다.

## [[Edge Operator]]
## [[Canny Edge Detection]]

## [[Hough Transform]]
## [[RANSAC]]
## [[Region Segmentation]]
## [[Interactive Segmentation]]
## [[Region Features]]
