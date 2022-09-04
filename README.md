:bangbang: **주의) 해당 프로젝트는 개발 중이며 커스텀 및 구동이 불가능할 수 있습니다.**
# SeizeBot

유튜브 뮤직비디오 조회수를 업데이트하고 게시하는 자동화 봇

## Description

* SeizeBot은 각종 커뮤니티, 게시판에 유튜브 뮤직비디오 조회수 통계를 업데이트합니다.
* DB에 전일의 뮤직비디오 조회수를 저장하고 다음 날 통계를 업로드할 때 참조하여 증/감 수치를 표시합니다.
* 여러 뮤직비디오의 통계를 하나의 이미지로 만들어 게시합니다.

## Getting Started

### Dependencies

* 이 프로젝트는 Docker 및 Docker-Compose를 사용합니다. 설치 전 먼저 Docker 및 Docker-Compose를 설치해주세요.

### Installing & Executing

* 이 저장소에서 프로젝트를 Clone합니다.

```bash
  git clone https://github.com/asheswook/SeizeBotV3.git
```

* 프로젝트 디렉토리로 이동해 Docker-Compose를 실행합니다. 모든 패키지와 종속성이 자동으로 설치되고, 이미지가 빌드되면 스크립트와 MariaDB 서버가 실행됩니다.

```bash
  cd SeizeBotV3-master
  docker-compose up
```

#### Env Variables

* 실행을 위해서 프로젝트의 최상단 폴더의 .env 파일에 다음과 같은 환경변수가 설정되어야 합니다. 해당 프로젝트의 [_env](_env) 파일에 기본값이 지정되어 있습니다. 해당 파일의 이름을 .env로 변경하여 사용할 수 있습니다.

`TWICENEST_ID`: 업로드할 때 사용할 트둥닷컴 계정 아이디

`TWICENEST_PW`: 업로드할 때 사용할 트둥닷컴 계정 비밀번호

`WANT_ID`: 업로드할 때 사용할 원트 계정 아이디

`WANT_PW`: 업로드할 때 사용할 원트 계정 비밀번호

##### MySQL/MariaDB
 * **주의: DB는 Docker-Compose에 통합되어 관리되기 때문에, 외부 DB를 사용하는 경우를 제외하면 다음과 같은 기본값을 가져야 합니다.**
 
`DB_HOST=db`: 사용할 DB의 호스트네임

`DB_PORT=3306`: 사용할 DB의 포트

`DB_USER=root`: 접속에 사용할 유저

`DB_PASSWORD=root!Seize`: 접속에 사용할 비밀번호

`DB_DATABASE=SeizeBot`: DB의 Database 이름

## Authors

- asheswook

## Version History

* 0.1
    * Initial Release

## License

이 프로젝트는 MIT 라이선스에 따라 배포됩니다. 해당 프로젝트의 코드를 사용할 때는 라이선스를 준수하여야 합니다. 자세한 내용은 LICENSE 파일을 참고하세요.

## Acknowledgments

Inspiration, code snippets, etc.
* [pafy](https://github.com/mps-youtube/pafy)
* [PyMySQL](https://github.com/PyMySQL/PyMySQL)
