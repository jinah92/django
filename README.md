<h1>Django</h1>

**1. 설치**
	- python 설치 후 환경변수 지정
	- django 설치 (1)
	    - easy_install django==<version>
		- (설치확인) django-admin --version
	- django 설치 (2)
		- pip install django



**2. 프로젝트 생성**
	- django-admin startproject <PJT_NAME>
	- (서버 시작) python manage.py runserver



**3. app 생성**
	- python manage.py startapp <APP_NAME>



**4. db 동기화**
1.  python manage.py migrate

2.  migration 절차
   - python manage.py makemigrations <APP> 	-- migration 생성
   - python manage.py sqlmigrate <APP> <VER>	-- db 수정
   - python manage.py migrate 				-- db 동기화(migrate)