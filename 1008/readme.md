# MX OPC Configurator를 이용한 GX Works2 - Factory I/O 연동

## 1. 개요

GX Works2에서 작성한 PLC 프로그램을 **Factory I/O와 연동**하기 위해 MX OPC Configurator를 사용하였다.

이번 실습에서는 실제 PLC 장비 대신 **GX Simulator2**를 사용하여 PLC 프로그램을 실행하고, MX OPC Configurator에서 PLC 디바이스를 OPC Data Tag로 등록한 뒤 Factory I/O에서 해당 Tag를 Browse하여 연결하였다.

전체적인 구성은 다음과 같다.

```text
GX Works2
   │
   │ PLC Program
   ▼
GX Simulator2
   │
   │
   ▼
MX OPC Configurator
   │
   │ OPC Data Tag
   ▼
Factory I/O
```

핵심은 **MX OPC Configurator에서 PLC의 디바이스를 OPC Tag로 구성하는 것**이다.

---

# 2. Address Space 생성

MX OPC Configurator를 실행한 후 먼저 PLC Simulator와 연결하기 위한 Address Space를 생성한다.

## 2.1 New MX Device

`Address Space`에서 우클릭한 후

```text
New MX Device
```

를 선택한다.

이후 `Configure`에 들어가 PLC Simulator와 연결할 설정을 진행한다.

### PC Side I/F 설정

`PC Side I/F`에서 다음과 같이 설정한다.

```text
PC Side I/F
└─ GX Simulator2
```

GX Works2에서 실행할 Simulator와 OPC Configurator를 연결하기 위한 설정이다.

### Target Simulator 설정

Target Simulator에서는

```text
Target Simulator
└─ SimulatorA
```

를 선택한다.

설정을 완료한 후 `Next`를 누르고 `Finish`를 선택한다.

마지막으로 설정 확인 창에서 모두 확인하여 Address Space를 생성한다.

---

# 3. Data Tag 생성

Address Space가 생성되면 해당 공간에서 PLC 디바이스를 OPC Tag로 등록한다.

생성된 Address Space에서 우클릭 후

```text
New Data Tag
```

를 선택한다.

Data Tag를 생성할 때 주요하게 설정하는 항목은 다음과 같다.

| 항목          | 설명               |
| ----------- | ---------------- |
| Name        | OPC에서 사용할 Tag 이름 |
| I/O Address | PLC 디바이스 주소      |
| Data Type   | 해당 데이터의 자료형      |
| Poll Method | PLC 값을 읽어오는 주기   |

예를 들어 PLC에서 사용하는 X, Y, D, M 등의 디바이스를 각각 Data Tag로 추가할 수 있다.

```text
X
Y
D
M
```

### 예시

```text
Name       : Sensor_X0
I/O Address: X0
Data Type  : Boolean
```

실제 사용하는 PLC 디바이스에 맞춰 Name과 I/O Address를 설정한다.

---

# 4. Data Polling 설정

Data Tag를 생성한 후 `Data Polling` 설정을 확인한다.

여기에서 `Poll Method`를 설정하여 PLC 데이터를 주기적으로 읽어오도록 한다.

예를 들어:

```text
Poll Method
└─ 100 ms
```

로 설정하면 약 100 ms 주기로 해당 PLC 데이터를 Polling하는 방식으로 구성할 수 있다.

따라서 Factory I/O에서 PLC의 상태 변화를 확인할 때 OPC를 통해 주기적으로 데이터를 읽을 수 있다.

---

# 5. Multiply를 이용한 Data Tag 복제

동일한 형식의 PLC 디바이스를 여러 개 사용하는 경우 각각의 Data Tag를 일일이 생성하는 대신 `Multiply` 기능을 이용하여 복제할 수 있다.

예를 들어 다음과 같이 여러 PLC 디바이스를 사용하는 경우:

```text
X0
X1
X2
X3
...
```

하나의 Tag를 기준으로 Multiply를 사용하여 여러 Tag를 생성할 수 있다.

이 기능을 이용하면 Factory I/O와 연결할 PLC 디바이스가 많아졌을 때 설정 작업을 줄일 수 있다.

---

# 6. PLC Simulator 실행

MX OPC Configurator에서 필요한 Data Tag 설정을 완료한 후 GX Works2로 이동한다.

GX Works2에서 작성한 PLC 프로그램을 **GX Simulator2**에서 실행한다.

```text
GX Works2
   ↓
Simulation Start
   ↓
GX Simulator2
```

이제 실제 PLC 대신 Simulator에서 PLC 프로그램이 동작하게 된다.

따라서 GX Simulator2에서 X, Y, M, D 등의 디바이스 값을 확인하거나 변경할 수 있다.

---

# 7. OPC 실행

GX Simulator2가 정상적으로 실행된 상태에서 MX OPC Configurator의 OPC 기능을 실행한다.

이제 앞에서 생성한 Address Space와 Data Tag를 통해 GX Simulator2의 PLC 데이터를 OPC에서 사용할 수 있게 된다.

전체 데이터 흐름은 다음과 같다.

```text
GX Works2
    │
    ▼
GX Simulator2
    │
    ▼
MX OPC Configurator
    │
    ├── X
    ├── Y
    ├── M
    └── D
```

여기서 MX OPC Configurator가 **GX Simulator2의 PLC 디바이스를 OPC를 통해 외부 프로그램에서 접근할 수 있도록 연결하는 역할**을 한다.

---

# 8. Factory I/O Driver 설정

OPC 설정이 완료되면 Factory I/O에서 PLC와 연결하기 위한 Driver를 설정한다.

Factory I/O의 Driver 설정으로 이동하여 OPC 관련 Driver를 선택한다.

```text
Factory I/O
    ↓
Drivers
    ↓
OPC
```

이후 OPC Server에 연결한다.

연결이 정상적으로 이루어지면 Factory I/O에서 OPC Server에 등록되어 있는 Data Tag를 **Browse**할 수 있다.

예를 들어 MX OPC Configurator에서 등록한 Tag가 다음과 같다면:

```text
X0
X1
X2
Y0
Y1
M0
D0
```

Factory I/O에서 해당 Tag를 Browse하여 센서나 액추에이터에 연결할 수 있다.

---

# 9. 전체 구성

이번 실습의 전체적인 데이터 흐름은 다음과 같다.

```text
┌─────────────────┐
│    GX Works2    │
│  Ladder Program │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ GX Simulator2   │
│  SimulatorA     │
└────────┬────────┘
         │
         ▼
┌──────────────────────┐
│ MX OPC Configurator  │
│                      │
│     Address Space    │
│          │           │
│      Data Tag        │
│   X / Y / M / D      │
└──────────┬───────────┘
           │
           │ OPC
           ▼
┌─────────────────┐
│   Factory I/O   │
│                 │
│ Sensor/Actuator │
└─────────────────┘
```

---

# 10. 핵심 정리

이번 실습에서 MX OPC Configurator는 **GX Simulator2에서 동작하는 PLC 디바이스와 Factory I/O 사이를 연결하는 OPC 기반의 중간 계층**으로 사용하였다.

특히 다음 과정을 이해하는 것이 중요하다.

```text
1. Address Space 생성
        ↓
2. New MX Device
        ↓
3. GX Simulator2 선택
        ↓
4. SimulatorA 선택
        ↓
5. Data Tag 생성
        ↓
6. Name / I/O Address / Data Type 설정
        ↓
7. Data Polling 설정
        ↓
8. Multiply를 이용하여 필요한 Tag 복제
        ↓
9. GX Works2에서 Simulation 실행
        ↓
10. OPC 실행
        ↓
11. Factory I/O Driver 설정
        ↓
12. OPC Tag Browse
        ↓
13. Factory I/O의 Sensor / Actuator와 연결
```

이 과정을 통해 실제 PLC가 없어도 **GX Works2에서 작성한 PLC 제어 로직을 GX Simulator2에서 실행하고, OPC를 통해 Factory I/O와 연결하여 가상 자동화 시스템을 구성**할 수 있다.
