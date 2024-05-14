# 기반 이미지로 Python 5.0.6 적합한 버전 사용
FROM python:3.10

# 컨테이너 내에서 작업 디렉토리 설정
WORKDIR /app

# 의존성 파일 복사
COPY requirements.txt .

# 의존성 설치
RUN pip install -r requirements.txt

# 나머지 프로젝트 파일 복사
COPY . .

# 포트 8000 열기
EXPOSE 8000

# 서버 실행
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
