# Bootstrap

* `materailize`, `sematic ui`와 같이 웹사이트를 쉽게 만들 수 있게 도와주는 프레임워크
* `css`(1줄)는 head 닫는 곳 위에
* `javascript`(3줄)는 body 닫는 곳 바로 위에

![1564980618860](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1564980618860.png)

## CDN

* `Content Delivery(Distrbution) Network`
* 컨텐츠(CSS, JS, Image, Text)을 효율적으로 전달하기 위해 여러 노드에 가진 네트워크에 데이터를 제공하는 시스템.
* 가까운 서버에 접근하기 때문에 미국에 있는 자료를 접근할 때 미국 서버까지 갈 필요 없음 => 지리적 이점, 서버의 부하가 적어짐



spacer(1rem) * 0.25 = 16px * 0.25   <=> 1rem = 16px

camel case

snake-case

kebab-case



## Spacing

* `margin`이나 `padding` 설정을 통해 여백을 만듦
* ex) mt-1 : margin-top

![1565064963450](./b1.png)

* 음수도 가능

![1565065020036](./b2.png)

* auto => 자동으로 위치 설정

  ex) mx-auto



## Color

* 활용법 => .bg-primary(background-color:primary)
* div
  * 박스 형태로 설정되고 정렬
  * width, height 지정 가능
  * 하나 입력할 때마다 줄바꿈 처리

* span
  * 줄 단위로 영역이 설정
  * width, height 지정 불가(inline 속성)
  * 입력해도 같은 줄에서 표시 됨