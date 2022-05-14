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

# ngrok 설치
choco install ngrok
ngrok config add-authtoken <인증 토큰>

# 포트와 ngrok 도메인 연결
ngork http 8080

# gradlew가 644로 되어있는 경우 755로 변경
git update-index --add --chmod=+x gradlew