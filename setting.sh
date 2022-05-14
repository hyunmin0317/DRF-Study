# docker-compose 파일로 Jenkins 설치
docker-compose up -d

# docker 실행 확인
docker ps -a

# docker 로그 확인
docker-compose logs

# Jenkins 비밀번호 확인
# Jenkins 컨테이너에 접속
docker exec -it jenkins /bin/bash

# Jenkins 비밀번호 찾기
cat /var/jenkins_home/secrets/initialAdminPassword
