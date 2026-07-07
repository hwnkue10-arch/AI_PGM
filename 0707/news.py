from datetime import datetime


# 경기 결과 입력받기
place = input("경기가 열린 곳은? ")
time = input("경기가 열린 시간은? ")
opponent = input("상대팀은? ")

goals = int(input("손흥민은 몇 골을 넣었나요? "))
aids = int(input("도움은 몇 개인가요? "))

score_me = int(input("손흥민 팀이 넣은 골 수는? "))
score_you = int(input("상대팀이 넣은 골 수는? "))


# 기사 작성
news = f"[프리미어리그 속보 ({datetime.now()})]\n"

news += f"손흥민 선수는 {place}에서 {time}에 열린 경기에 출전하였습니다.\n"

news += f"상대팀은 {opponent}입니다.\n"


# 경기 결과
if score_me > score_you:
    news += f"손흥민 선수의 팀이 {score_me}골을 넣어 {score_you}골을 넣은 상대팀을 이겼습니다.\n"

elif score_me < score_you:
    news += f"손흥민 선수의 팀이 {score_me}골을 넣었지만 {score_you}골을 넣은 상대팀에게 졌습니다.\n"

else:
    news += f"두 팀은 {score_me}대 {score_you}로 비겼습니다.\n"


# 손흥민 기록
if goals > 0 and aids > 0:
    news += f"손흥민 선수는 {goals}골과 {aids}개의 도움으로 승리를 크게 이끌었습니다.\n"

elif goals > 0 and aids == 0:
    news += f"손흥민 선수는 {goals}골을 기록하며 승리를 이끌었습니다.\n"

elif goals == 0 and aids > 0:
    news += f"손흥민 선수는 골은 없지만 {aids}개의 도움으로 승리에 기여했습니다.\n"

else:
    news += "아쉽게도 이번 경기에서 손흥민 선수의 공격 포인트는 없었습니다.\n"


# 기사 출력
print("\n===== 생성된 기사 =====")
print(news)
import subprocess

subprocess.run([
    "powershell",
    "-Command",
    f"""
    Add-Type -AssemblyName System.Speech;
    $speak = New-Object System.Speech.Synthesis.SpeechSynthesizer;
    $speak.Speak('{news}');
    """
])

print("음성 재생 완료!")
# PowerShell을 실행하여 Windows 음성 엔진 사용
# System.Speech.Synthesis.SpeechSynthesizer 객체를 생성하고
# news 변수에 저장된 기사를 음성으로 출력함
