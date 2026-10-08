# GX Works2 - MX OPC Configurator - Factory I/O 연동

GX Works2에서 작성한 Mitsubishi PLC 레더 프로그램을 **MX OPC Configurator**를 이용해 OPC 서버와 연결하고, **Factory I/O에서 PLC의 입출력 데이터를 브라우징하여 사용하는 방법**을 정리한 실습 기록입니다.

## 1. 실습 목표

GX Works2에서 작성한 PLC 프로그램을 Factory I/O와 연동하여 실제 자동화 시스템과 유사한 환경에서 동작을 확인합니다.

전체 구성은 다음과 같습니다.

```text
GX Works2
    │
    │ PLC 프로그램
    ▼
Mitsubishi PLC
    │
    │ OPC 통신
    ▼
MX OPC Configurator
    │
    │ OPC Tag
    ▼
Factory I/O
```

핵심적으로 다음 과정을 수행합니다.

1. GX Works2에서 PLC 레더 프로그램 작성
2. MX OPC Configurator에서 PLC 장치 및 디바이스 설정
3. OPC를 통해 PLC의 디바이스를 Tag로 등록
4. Factory I/O에서 OPC 서버에 연결
5. Factory I/O에서 PLC Tag를 Browse
6. 센서 입력과 액추에이터 출력을 PLC와 연결
7. PLC 프로그램과 Factory I/O의 동작 확인

---

## 2. 사용 프로그램

| 프로그램                | 용도                    |
| ------------------- | --------------------- |
| GX Works2           | PLC 레더 프로그램 작성        |
| MX OPC Configurator | OPC 통신 및 PLC 디바이스 설정  |
| Factory I/O         | 가상 자동화 설비 구성 및 PLC 연동 |

> 실제 사용한 PLC 기종, GX Works2 버전, MX OPC Configurator 버전은 실습 환경에 맞게 추가합니다.

---

## 3. GX Works2 레더 프로그램 작성

먼저 GX Works2에서 Factory I/O와 연동할 PLC 프로그램을 작성합니다.

예를 들어 센서 입력을 받아 출력 장치를 제어하는 간단한 구조를 구성할 수 있습니다.

```text
입력
X0 ────────┐
           │
           ├──── Y0
           │
X1 ────────┘
```

실제 프로젝트에서는 Factory I/O의 센서와 액추에이터에 대응하도록 PLC 디바이스를 지정합니다.

예:

```text
X0 : Sensor Input
X1 : Start Input

Y0 : Motor
Y1 : Lamp
```

### 레더 프로그램

> 여기에 실제 GX Works2 레더 화면을 캡처해서 추가합니다.

![GX Works2 Ladder](screenshots/01_gxworks2_ladder.png)

---

## 4. MX OPC Configurator 설정

GX Works2에서 작성한 PLC 프로그램의 디바이스를 Factory I/O에서 사용하기 위해 MX OPC Configurator를 설정합니다.

먼저 MX OPC Configurator에서 PLC와 통신하기 위한 장치를 등록합니다.

> 여기에 MX OPC Configurator 설정 화면을 추가합니다.

![MX OPC Configurator](screenshots/02_mx_opc_configurator.png)

### 주요 설정

실습 환경에 따라 다음 항목을 설정합니다.

* PLC 종류
* 통신 방식
* PLC IP 주소 또는 통신 설정
* PLC Station
* 디바이스 영역
* OPC Tag

---

## 5. PLC 디바이스와 OPC Tag 연결

Factory I/O에서 사용할 PLC 디바이스를 OPC Tag로 등록합니다.

예를 들어 다음과 같이 구성할 수 있습니다.

| PLC Device | 역할    | Factory I/O |
| ---------- | ----- | ----------- |
| X0         | 센서 입력 | Sensor      |
| X1         | 시작 입력 | Start       |
| Y0         | 모터 출력 | Motor       |
| Y1         | 램프 출력 | Lamp        |

OPC 서버에서 해당 디바이스가 정상적으로 등록되었는지 확인합니다.

![OPC Device Setting](screenshots/03_opc_device_setting.png)

---

## 6. Factory I/O OPC 연결

Factory I/O를 실행한 뒤 PLC 연결을 설정합니다.

Factory I/O의 Driver 설정에서 OPC 서버를 선택합니다.

```text
Factory I/O
   ↓
Drivers
   ↓
OPC
   ↓
OPC Server 선택
```

연결 후 **Browse** 기능을 이용하여 OPC 서버에 등록된 PLC Tag를 확인합니다.

![Factory I/O Driver](screenshots/04_factory_io_driver.png)

---

## 7. Factory I/O에서 Tag Browse

OPC 서버와 정상적으로 연결되었다면 Factory I/O에서 PLC 디바이스를 Browse할 수 있습니다.

예:

```text
OPC Server
 ├─ X0
 ├─ X1
 ├─ Y0
 └─ Y1
```

각 Tag를 Factory I/O의 센서 및 액추에이터에 연결합니다.

예를 들어:

```text
Factory I/O Sensor
        │
        ▼
       X0
        │
        ▼
   PLC Ladder
        │
        ▼
       Y0
        │
        ▼
Factory I/O Motor
```

---

## 8. 동작 확인

모든 설정이 완료되면 Factory I/O를 실행하고 PLC 프로그램을 Monitor 상태로 확인합니다.

센서가 동작하면 Factory I/O에서 OPC를 통해 PLC 입력 디바이스가 변경되고, PLC 레더 프로그램의 조건에 따라 출력 디바이스가 변경됩니다.

최종적으로 다음과 같은 흐름을 확인할 수 있습니다.

```text
[Factory I/O Sensor]
        │
        │ Input
        ▼
      [PLC X0]
        │
        ▼
   [Ladder Logic]
        │
        ▼
      [PLC Y0]
        │
        │ Output
        ▼
[Factory I/O Actuator]
```

![Factory I/O Result](screenshots/05_factory_io_result.png)

---

## 9. 전체 통신 구조

```text
┌──────────────────┐
│    Factory I/O   │
│                  │
│ Sensor / Motor   │
└────────┬─────────┘
         │
         │ OPC
         ▼
┌──────────────────┐
│ MX OPC Config.   │
│                  │
│ PLC Device/Tag   │
└────────┬─────────┘
         │
         │ PLC Communication
         ▼
┌──────────────────┐
│      PLC         │
│                  │
│ X Input          │
│ Y Output         │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│    GX Works2     │
│                  │
│ Ladder Program   │
└──────────────────┘
```

## 10. 실습에서 확인한 내용

* GX Works2를 이용한 PLC 레더 프로그램 작성
* PLC 디바이스(X/Y 등)의 이해
* MX OPC Configurator를 이용한 PLC-OPC 연결
* PLC 디바이스의 OPC Tag 등록
* Factory I/O와 OPC 서버 연결
* Factory I/O에서 OPC Tag Browse
* PLC 입력과 출력의 가상 설비 연동
* PLC 프로그램의 실제 동작을 Factory I/O에서 시각적으로 확인

## 11. Troubleshooting

### Factory I/O에서 OPC Server가 보이지 않는 경우

다음 항목을 확인합니다.

* OPC 서버가 정상적으로 실행되어 있는지 확인
* MX OPC Configurator의 PLC 설정 확인
* PLC 통신 설정 확인
* 네트워크 연결 확인
* Factory I/O에서 올바른 Driver를 선택했는지 확인

### OPC Tag가 Browse되지 않는 경우

* OPC 서버에 PLC 디바이스가 정상적으로 등록되어 있는지 확인
* Tag의 Device 주소 확인
* PLC와 OPC 서버의 통신 상태 확인
* Factory I/O의 OPC 연결 상태 확인

### PLC 값이 Factory I/O에서 변경되지 않는 경우

PLC Monitor에서 해당 X/Y 디바이스의 값이 실제로 변경되는지 먼저 확인합니다.

```text
Factory I/O
     ↓
OPC
     ↓
PLC Device
     ↓
Ladder Logic
```

어느 단계에서 값이 변경되지 않는지 확인하면 문제의 위치를 좁힐 수 있습니다.

---

## 12. 정리

이번 실습에서는 **GX Works2 → MX OPC Configurator → Factory I/O**로 이어지는 PLC 연동 과정을 학습했습니다.

특히 단순히 PLC 레더 프로그램을 작성하는 것뿐만 아니라, PLC의 디바이스를 OPC Tag로 구성하고 Factory I/O에서 해당 Tag를 Browse하여 가상 자동화 설비와 연결하는 과정을 경험했습니다.

이를 통해 PLC 제어 로직과 상위 시스템 간의 데이터 연동 구조를 이해할 수 있었습니다.
