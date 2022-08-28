<div align="center">

  <!--<img src="assets/logo.png" alt="logo" width="200" height="auto" />-->
  <h1>SeizeBot</h1>
  
  
  <p>
    :bangbang: 아직 개발 중입니다.
  </p>
  <p>
    유튜브 뮤직비디오 조회수를 업데이트하고 게시하는 자동화 봇
  </p>

  
<!-- Badges -->
<p>
  <!--<a href="https://github.com/Louis3797/awesome-readme-template/graphs/contributors">
    <img src="https://img.shields.io/github/contributors/Louis3797/awesome-readme-template" alt="contributors" />
  </a>-->
  <a href="">
    <img src="https://img.shields.io/github/last-commit/Louis3797/awesome-readme-template" alt="last update" />
  </a>
  <!--<a href="https://github.com/Louis3797/awesome-readme-template/network/members">
    <img src="https://img.shields.io/github/forks/Louis3797/awesome-readme-template" alt="forks" />
  </a>-->
  <!--<a href="https://github.com/Louis3797/awesome-readme-template/stargazers">
    <img src="https://img.shields.io/github/stars/Louis3797/awesome-readme-template" alt="stars" />
  </a>-->
  <a href="https://github.com/asheswook/SeizeBotV3/issues/">
    <img src="https://img.shields.io/github/issues/asheswook/SeizeBotV3" alt="open issues" />
  </a>
  <a href="https://github.com/asheswook/SeizeBotV3/blob/master/LICENSE">
    <img src="https://img.shields.io/github/license/asheswook/SeizeBotV3" alt="license" />
  </a>
</p>
   
<h4>
    <!--<a href="https://github.com/Louis3797/awesome-readme-template/">View Demo</a>
  <span> · </span>-->
    <a href="https://github.com/asheswook/SeizeBotV3/blob/master/README.md">문서</a>
  <span> · </span>
    <a href="https://github.com/asheswook/SeizeBotV3/issues/">오류 리포트</a>
  <span> · </span>
    <a href="https://github.com/asheswook/SeizeBotV3/issues/">기능 요청</a>
  </h4>
</div>

<br />

<!-- Table of Contents -->
# :notebook_with_decorative_cover: 목차

- [이 프로젝트에 대해](#star2-이-프로젝트에-대해)
  * [스택](#space_invader-스택)
  * [기능](#dart-기능)
  * [환경변수](#key-환경변수)
- [시작하기](#toolbox-시작하기)
  * [요구사항](#bangbang-요구사항)
  * [실행](#running-실행)
- [커스텀](#eyes-커스텀)
- [라이선스](#warning-라이선스)
- [외부 라이브러리](#gem-외부-라이브러리)
  

<!-- About the Project -->
## :star2: 이 프로젝트에 대해

<!-- TechStack -->
### :space_invader: 스택

<details>
  <summary>Script</summary>
  <ul>
    <li><a href="https://www.python.org">Python</a></li>
    <li>HTML/CSS</li>
  </ul>
</details>

<details>
  <summary>Database</summary>
  <ul>
    <li><a href="https://www.typescriptlang.org/">MariaDB</a></li>
  </ul>
</details>

<details>
<summary>DevOps</summary>
  <ul>
    <li><a href="https://www.docker.com/">Docker</a></li>
  </ul>
</details>

<!-- Features -->
### :dart: 기능

- SeizeBot은 지정한 시간에 각종 게시판 (커뮤니티)에 유튜브 뮤직비디오 조회수 통계를 업로드합니다.
  - DB에 이전 뮤직비디오 조회수 정보를 저장하여, 다음 날 업로드할 때 참조하고 증감 수치를 같이 표시합니다.
  - 여러 뮤직비디오들의 통계를 한꺼번에 이미지로 만들어 게시합니다.

<!-- Env Variables -->
### :key: 환경변수

이 프로젝트를 실행하려면 프로젝트의 최상단 폴더의 .env에 다음과 같은 환경변수가 설정되어야 합니다.
해당 프로젝트의 [_env](_env) 파일에 기본값이 지정되어 있습니다. 해당 파일의 이름을 .env로 변경하여 사용할 수 있습니다.

`TWICENEST_ID`: 업로드할 때 사용할 트둥닷컴 계정 아이디

`TWICENEST_PW`: 업로드할 때 사용할 트둥닷컴 계정 비밀번호

`WANT_ID`: 업로드할 때 사용할 원트 계정 아이디

`WANT_PW`: 업로드할 때 사용할 원트 계정 비밀번호



MySQL/MariaDB 접속에 사용되는 환경변수는 다음과 같습니다.
 - :bangbang: 주의: 외부 DB를 사용하는 경우를 제외하면 해당 변수들은 다음과 같은 기본값을 가져야합니다.
 - DB는 docker-compose로 스크립트와 통합되어 관리됩니다.

`DB_HOST=db`: 사용할 DB의 호스트네임

`DB_PORT=3306`: 사용할 DB의 포트

`DB_USER=root`: 접속에 사용할 유저

`DB_PASSWORD=root!Seize`: 접속에 사용할 비밀번호

`DB_DATABASE=SeizeBot`: DB의 Database 이름


<!-- Getting Started -->
## 	:toolbox: 시작하기

<!-- Prerequisites -->
### :bangbang: 요구사항

이 프로젝트는 Docker-compose 및 Docker을 사용합니다.
먼저 Docker-compose 및 Docker를 설치해주세요.


<!-- Run -->
### :running: 실행

프로젝트를 클론합니다.

```bash
  git clone https://github.com/asheswook/SeizeBotV3.git
```

프로젝트 디렉토리로 이동해 Docker-compose를 실행합니다. 
모든 종속성과 패키지들이 자동으로 설치되고 이미지가 빌드되면 스크립트가 실행됩니다.

```bash
  cd SeizeBotV3-master
  docker-compose up
```

<!-- Usage -->
## :eyes: 커스텀
업로드 할 사이트, 업로드 시간 등을 커스텀 할 수 있습니다.

Not yet
개발 중

```python
None
```


<!-- License -->
## :warning: 라이선스

이 프로젝트는 MIT 라이선스에 따라 배포됩니다. 해당 프로젝트의 코드르 사용할 때는 라이선스를 준수하여야 합니다. 자세한 내용은 LICENSE 파일을 참고하세요.


<!-- Acknowledgments -->
## :gem: 외부 라이브러리

이 프로젝트에는 아래와 같은 라이브러리 및 리소스를 사용했습니다.

 - [pafy](https://github.com/mps-youtube/pafy)
 - [PyMySQL](https://github.com/PyMySQL/PyMySQL)
