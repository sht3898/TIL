# TIL(Today I Learnd)

* 매일 배운 것 정리하기
* Everyday commit to Github



## Python

* python 실습 내용 정리
* [python](./python)  



## Startcamp

* startcamp 때 내용 정리
* [startcamp](./startcamp)

## 생활코딩

* [생활코딩](https://opentutorials.org/course/1)에서 공부한 내용 정리
* [생활코딩](./생활코딩)



## 기술면접

* 기술면접 대비

* [기술면접](./기술면접)  





## Git

> github 저장소 최초 생성 시 안내 메시지

```bash
echo "# abc" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/sht3898/abc.git
git push -u origin main
```

* origin

  * 원격 저장소의 이름
  * 기본적으로는 origin 이고 새롭게 추가하고 싶은 위치의 이름을 정해서 추가해도 됨

  ```bash
  git remote add origin https://github.com/sht3898/abc.git
  
  git remote add second
  https://github.com/sht3898/zyx.git
  ```

* main
  * 브랜치의 이름
  * 기본적으로는 main이고 자신이 설정한 branch 명에 따라 달라짐

