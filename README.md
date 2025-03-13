- 도커이미지를 생성하기 위한 코드 집합  
-- nginx  
-- python-web  
-- nodehs-web  
-- python-kafka-producer


- 도커 명령어
```
# 이미지 빌드(dockerfile 사용)
docker build -t [생성할 이미지명] -f [dockerfile 파일명] .
$ docker build -t nginx-basic .


# 이미지 빌드(실행중인 이미지)
컨테이너 내부에서 작업을 변경한후 변경내용을 반영하고 싶을 때
docker commit [options] container [repository[:tag]]
$ docker commit -m "modify nginx.conf" test-container commit_test:latest


# 이미지 실행
docker run -d -p {호스트포트}:{컨테이너포트} --name {컨테이너 이름} {컨테이너 이미지 이름}
$ docker run -d -p 8080:80 --name nginx-web nginx-basic:latest
