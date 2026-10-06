# Mosquitto MQTT + IoT MQTT Panel + Indy7 로봇 제어 시스템

본 프로젝트는 **Mosquitto MQTT Broker**, 스마트폰 **IoT MQTT Panel 앱**, 그리고 **Python(IndyDCP3)** 기반의 로봇 제어 클라이언트를 연동하여 산업용 협동로봇(Indy7)을 무선(Wi-Fi)으로 원격 제어 및 모니터링하는 통합 실습 가이드입니다.

---

## 1. 시스템 아키텍처 (System Architecture)

```
[ 스마트폰 (IoT MQTT Panel) ]
           │
           │ Wi-Fi (MQTT Pub/Sub, Port: 1883)
           ▼
[ 컴퓨터 1 (Mosquitto MQTT Broker) ] (예: 192.168.0.10:1883)
           ▲
           │ Wi-Fi (MQTT Pub/Sub)
           │
[ 컴퓨터 2 (Python Gateway / Robot Controller) ]
           │
           │ Ethernet (TCP/IP IndyDCP3, 192.168.3.2)
           ▼
[ 뉴로메카 협동로봇 (Indy7) ]
```

- **스마트폰 ↔ 컴퓨터 1 ↔ 컴퓨터 2**: 동일한 공유기(Wi-Fi) 망에서 MQTT 프로토콜(TCP 1883)로 통신.
- **컴퓨터 2 ↔ Indy7 협동로봇**: 유선 이더넷(Ethernet) 분리 네트워크로 통신.

---

## 2. 역할 및 담당 기기 (System Components)

| 장치 | 주요 역할 | 요구 소프트웨어/라이브러리 |
| :--- | :--- | :--- |
| **스마트폰** | 제어 명령 발행(Publish) 및 로봇 상태 수신(Subscribe) | `IoT MQTT Panel` 앱 (Android/iOS) |
| **컴퓨터 1** | MQTT Broker 구동, 장치 간 메시지 라우팅 중계 | `Mosquitto Broker (mosquitto.exe)` |
| **컴퓨터 2** | MQTT 명령 수신 → Indy7 로봇 구동 → 상태 회신 게이트웨이 | `Python 3.x`, `paho-mqtt`, `neuromeka (IndyDCP3)` |
| **Indy7** | 협동로봇 본체 및 제어기 (직접 모션 및 IO 구동) | Indy Framework 3.x |

---

## 3. MQTT Topic 및 Payload 설계

### 3.1 명령 전송 (Command: App → Broker → Python Controller)
- **Topic**: `indy7/command`

| Payload (명령어) | 설명 | 동작 |
| :--- | :--- | :--- |
| `HOME` | 로봇 초기 위치 이동 | `indy.move_home()` |
| `POS1` | 작업 위치 1 이동 | 사전 티칭된 관절/공간 좌표로 이동 |
| `POS2` | 작업 위치 2 이동 | 사전 티칭된 관절/공간 좌표로 이동 |
| `VACUUM_ON` | 진공 그리퍼 흡착 ON | 디지털 출력(DO) 활성화 (`set_do`) |
| `VACUUM_OFF` | 진공 그리퍼 해제 OFF | 디지털 출력(DO) 비활성화 (`set_do`) |

### 3.2 상태 회신 (Status: Python Controller → Broker → App)
- **Topic**: `indy7/status`

| Payload (상태값) | 설명 |
| :--- | :--- |
| `ROBOT_READY` | 파이썬 게이트웨이가 준비되어 명령 수신 대기 상태 |
| `HOME_MOVING` / `HOME_DONE` | 홈 위치 이동 중 / 이동 완료 |
| `POS1_MOVING` / `POS1_DONE` | 1번 위치 이동 중 / 이동 완료 |
| `POS2_MOVING` / `POS2_DONE` | 2번 위치 이동 중 / 이동 완료 |
| `VACUUM_ON_DONE` / `VACUUM_OFF_DONE` | 그리퍼 작동 완료 |
| `ROBOT_ERROR` | 로봇 제어 실패 또는 통신 예외 발생 |

---

## 4. 단계별 설치 및 실행 가이드

### [Step 1] 컴퓨터 1 — Mosquitto Broker 실행
1. `mosquitto.conf` 설정 파일 생성 (외부 접속 및 익명 접속 허용):
   ```text
   listener 1883
   allow_anonymous true
   ```
2. Windows 방화벽 인바운드 1883 포트 오픈:
   ```powershell
   New-NetFirewallRule -DisplayName "Mosquitto MQTT 1883" -Direction Inbound -Protocol TCP -LocalPort 1883 -Action Allow
   ```
3. Mosquitto Broker 실행:
   ```cmd
   cd "C:\Program Files\mosquitto"
   mosquitto.exe -c "C:\Program Files\mosquitto\mosquitto.conf" -v
   ```
4. 컴퓨터 1의 Wi-Fi IPv4 주소 확인 (`ipconfig` 실행, 예: `192.168.0.10`).

---

### [Step 2] 로컬 통신 기본 검증 (컴퓨터 1 자체 테스트)
- **Subscriber 대기 (수신창)**:
  ```cmd
  mosquitto_sub.exe -h localhost -p 1883 -t indy7/command -v
  ```
- **Publisher 전송 (발신창)**:
  ```cmd
  mosquitto_pub.exe -h localhost -p 1883 -t indy7/command -m HOME
  ```
- 결과: 수신창에 `indy7/command HOME` 메시지가 출력되면 기본 브로커 구동 성공.

---

### [Step 3] 스마트폰 IoT MQTT Panel 앱 설정
1. 스마트폰을 컴퓨터 1과 **동일한 Wi-Fi** 망에 연결.
2. **Connection 추가**:
   - **Broker IP/Host**: 컴퓨터 1의 Wi-Fi IP (예: `192.168.0.10`)
   - **Port**: `1883`
   - **Network Protocol**: `TCP`
3. **위젯(Panels) 배치**:
   - **Button (HOME)**: Topic = `indy7/command`, Payload = `HOME`
   - **Button (POS1)**: Topic = `indy7/command`, Payload = `POS1`
   - **Button (POS2)**: Topic = `indy7/command`, Payload = `POS2`
   - **Switch (VACUUM)**: Topic = `indy7/command`, On Payload = `VACUUM_ON`, Off Payload = `VACUUM_OFF`
   - **Text / Log (STATUS)**: Topic = `indy7/status` (구독 설정)

---

### [Step 4] 컴퓨터 2 — Python 게이트웨이 구동

1. 의존성 패키지 설치:
   ```bash
   pip install paho-mqtt
   ```
2. 네트워크 연결 확인:
   ```powershell
   ping 192.168.0.10
   Test-NetConnection 192.168.0.10 -Port 1883
   ```
3. 게이트웨이 스크립트 실행:
   - 처음에는 `SIMULATION_MODE = True`로 실행하여 스마트폰 위젯 조작 시 콘솔 로그와 MQTT 상태 회신을 검증합니다.
   - Indy7 로봇과 이더넷 연결(`192.168.3.2`)이 완료되면 `SIMULATION_MODE = False`로 변경하고 실제 로봇을 제어합니다.

---

## 5. 트러블슈팅 (Troubleshooting)

1. **Broker가 시작되지 않는 경우**:
   - 이미 백그라운드 윈도우 서비스가 포트를 점유하고 있을 수 있습니다. 관리자 권한 CMD에서 `net stop mosquitto`를 실행한 후 다시 시작합니다.
2. **스마트폰/컴퓨터 2에서 브로커 접속 불가 (Connection Timeout)**:
   - 스마트폰과 컴퓨터 1이 동일한 AP(공유기)에 물려 있는지 확인합니다.
   - 컴퓨터 1의 윈도우 방화벽 인바운드 규칙(포트 1883)이 활성화되어 있는지 확인합니다.
   - 설정 파일에 `listener 1883`과 `allow_anonymous true`가 올바르게 적용되었는지 점검합니다.
3. **로봇이 움직이지 않는 경우**:
   - MQTT 통신 문제와 로봇 모션 문제를 분리하여 점검합니다.
   - 파이썬 콘솔에 명령 수신 로그가 뜨는지 먼저 확인한 후, `IndyDCP3` 단독 모션 예제 코드로 로봇 비상정지 해제 및 이더넷 연결 상태를 점검합니다.
