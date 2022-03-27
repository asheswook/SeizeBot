# SeizeBot
매일 아침 8시 트둥닷컴과 원트, 트와이스 위키에 뮤비 조회수를 게시하는 봇입니다.

## V2 개선 점
안정성이 대폭 강화되었으며, Typescript로 다시 짜려고 했지만 개선 작업을 거치면서 그럴 필요가 없어졌습니다.
OS 단에서 문제가 발생하지 않는 한 몇달 간 실행해도 깔끔하게 작동합니다.

* 파일을 구조화
* webdriver를 재활용하도록 개선
* __웹 로드 프로세스로 인해 Element를 찾지 못하고 뻗는 점 개선__
* __Viewcount Loader 클래스 다각화를 통한 코드 경량화 및 사용성 향상__
* CKEditor의 iframe 오류 개선, 작성될 게시글 본문 메세지 커스텀 가능
* Logger 클래스 제거 및 Log 처리 단순화 (추후 다시 부활 예정)
* config 파일을 통한 편의성 향상

## Notice
__현재는 기본적으로 코드 그대로는 일반 유저분들이 정상 작동시키지 못하도록 설계되어 있습니다.
지속적으로 작업을 통하여 누구나 어느 곳에서든지 사용할 수 있도록 개선할 예정입니다.__

Pull request 및 Issue 제안은 언제든지 환영이며, 이 코드를 사용하실 경우 명시된 라이선스 (MIT)를 준수해주시기 바랍니다.

## Requires
* Python __3.9__ 이상
* Chrome 및 Chromedriver

## Usage
Python3, Chromedriver이 필요합니다.

Terminal에서 아래 커맨드를 실행합니다.
```
git clone https://github.com/asheswook/SeizeBot.git
cd SeizeBot
python3 app.py
```

기본적으로 Package import에 실패하면 ```pip3```를 통해 패키지를 설치하지만, 정상 작동하지 않을 경우 수동으로 수행하세요.
```
pip3 install -r requirements.txt
python3 app.py
```

----
이후 webdriver 경로 지정 및 .setting.json을 설정해 주세요.

webdriver 경로는 ```app.py```의 ```webdriver_path```에 지정되어 있습니다.
해당 변수를 수정하여 webdriver의 경로를 지정할 수 있습니다.
이 레포에 설정되어 있는 기본 webdriver 경로는 ```'/usr/local/share/chromedriver'``` 입니다.

참고로 webdriver 선언은 아래와 같은 형태로 할 수 있습니다.
```python
webdriver = loadWebdriver("YOUR WEBDRIVER PATH")
```
loadWebdriver() 함수의 인수를 지정하지 않을 시 자동으로 경로가 ```'/usr/local/share/chromedriver'``` 로 설정됩니다.


## .setting.json
```
{
  "mysql": {
    "username": "user",
    "password": "",
    "host": "localhost",
    "port": 3306,
    "dbname": "",
    "charset": "utf8"
  },

    "twicewiki": {
        "id": "",
        "password": ""
    },

    "twicenest": {
        "id": "",
        "password": ""
    },

    "want": {
        "id": "",
        "password": ""
    }
}
```
* mysql
  * username: DB에 접속할 때 사용하는 사용자명 입니다. (비권장: 루트 사용자)
  * password: DB에 접속할 때 사용하는 비밀번호 입니다.
  * host: 접속할 DB의 주소 입니다. 
  * port: 접속할 DB의 포트 입니다. Mysql의 기본 포트는 3306 입니다.
  * dbname: SeizeBot이 사용할 Mysql database의 이름 입니다.
  * charset: 문자 인코딩 방식을 지정합니다. (권장: utf8)

## Workflow
updateDB() 함수 실행 -> 모든 Viewcount 불러옴 -> 현재 조회수 및 변동 수치 불러옴 -> 위키 문법에 맞춰 내용을 작성, data 변수에 저장 -> 데이터베이스에 저장된 조회수 항목들을 최신 조회수로 업데이트 -> data 변수 return, editDocument 함수로 보냄

editDocument() 함수 실행 -> 트와이스 위키 접속 후 data를 문서에 작성, TWICE/뮤비 조회수 문서 업데이트

captureDocument() 함수 실행 -> 트와이스 위키 TWICE/뮤비 조회수 문서 접속 -> 화면 캡쳐, 저장

postImageToTN() 함수 실행 -> 트둥닷컴 접속, 캡쳐된 이미지 및 텍스트 업로드, 종료

postImageToWT() 함수 실행 -> 원트 접속, 캡쳐된 이미지 및 텍스트 업로드, 종료
