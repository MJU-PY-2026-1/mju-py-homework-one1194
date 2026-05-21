# 파일이름 :
# 작 성 자 :
manager_name = ""
team_budget = 0.0
add_count = 0
target_player = ""
is_signed = False

my_team = []

market_players = [
    ["리오넬 메시", "FW", 95, 95, 80, 65, 30, 95, 1500.0],
    ["크리스티아누 호날두", "FW", 98, 80, 90, 90, 35, 90, 1200.0],
    ["킬리안 음바페", "FW", 95, 80, 98, 80, 35, 97, 1800.0],
    ["엘링 홀란드", "FW", 97, 75, 92, 95, 45, 78, 1800.0],
    ["손흥민", "FW", 91, 87, 95, 76, 42, 86, 800.0],
    ["케빈 더브라위너", "MF", 85, 96, 80, 78, 60, 80, 1200.0],
    ["로베르트 레반도프스키", "FW", 93, 78, 76, 88, 40, 78, 700.0],
    ["카림 벤제마", "FW", 90, 88, 78, 82, 38, 82, 850.0],
    ["루카 모드리치", "MF", 80, 93, 75, 65, 70, 90, 600.0],
    ["모하메드 살라", "FW", 92, 82, 95, 75, 45, 92, 1100.0],
    ["해리 케인", "FW", 92, 90, 70, 83, 45, 75, 1200.0],
    ["비니시우스 주니오르", "FW", 86, 80, 97, 70, 30, 97, 1400.0],
    ["주드 벨링엄", "MF", 82, 88, 82, 85, 82, 88, 1700.0],
    ["로드리", "MF", 75, 90, 65, 86, 94, 75, 1300.0],
    ["알리송 베케르", "GK", 10, 85, 50, 80, 93, 95, 800.0],
    ["버질 반 다이크", "DF", 60, 75, 85, 97, 94, 70, 1000.0],
    ["후벵 디아스", "DF", 40, 70, 80, 92, 92, 60, 950.0],
    ["티보 쿠르투아", "GK", 10, 75, 45, 85, 92, 97, 850.0],
    ["마누엘 노이어", "GK", 15, 90, 50, 80, 90, 95, 500.0],
    ["카세미루", "MF", 75, 83, 70, 88, 90, 75, 700.0],
    ["토니 크로스", "MF", 82, 98, 70, 70, 70, 70, 700.0],
    ["네이마르", "FW", 85, 88, 88, 60, 35, 96, 900.0],
    ["앙투안 그리즈만", "FW", 86, 90, 80, 70, 60, 87, 850.0],
    ["니콜로 바렐라", "MF", 78, 87, 80, 75, 80, 85, 900.0],
    ["페데리코 발베르데", "MF", 84, 86, 90, 82, 80, 85, 1100.0],
    ["부카요 사카", "FW", 86, 82, 92, 70, 55, 91, 1100.0],
    ["마르틴 외데고르", "MF", 80, 90, 78, 65, 60, 86, 1000.0],
    ["페드리", "MF", 75, 94, 78, 60, 65, 95, 1100.0],
    ["라우타로 마르티네스", "FW", 94, 75, 84, 86, 45, 85, 1000.0],
    ["흐비차 크바라츠헬리아", "FW", 86, 80, 88, 72, 60, 93, 1100.0]
]

def calculate_ovr(stats, position) :
    calculated_ovr = 0.0

    if position == "FW" :
        calculated_ovr = (stats[0]*0.35) + (stats[2]*0.2) + (stats[5]*0.15) + (stats[1]*0.15) + (stats[3]*0.1) + (stats[4]*0.05)
    elif position == "MF":
        ovr = (stats[1]*0.35) + (stats[5]*0.2) + (stats[2]*0.15) + (stats[0]*0.1) + (stats[4]*0.1) + (stats[3]*0.1)
    elif position == "DF":
        ovr = (stats[4]*0.4) + (stats[2]*0.2) + (stats[3]*0.2) + (stats[1]*0.1) + (stats[0]*0.05) + (stats[5]*0.05)
    elif position == "GK":
        ovr = (stats[4]*0.4) + (stats[5]*0.25) + (stats[1]*0.15) + (stats[3]*0.15) + (stats[2]*0.05)
    else : 
        calculated_ovr = sum(stats) / len(stats)

    return calculated_ovr

def register_rookie() :
    print("\n" + "-"*15 + "신인 선수 등록 시스템" + "-"*15)
    add_count = int(input("새로 등록할 신인 선수는 몇 명입니까? (정수) : "))
    stat_names = ["슈팅", "패스", "스피드", "피지컬", "수비", "민첩성"]

    for i in range(add_count) :
        new_name = input(f"\n[{i+1}번째 신인 선수] 이름을 입력하세요 : ")
        new_pos = input(f"[{new_name}] 포지션 선택(FW/MF/DF/GK) (대문자로 입력): ").upper()

        new_stats = []
        print(f"--- {new_name}의 6개 능력치 입력 ---")
        for s_name in stat_names :
            new_stats.append(int(input(f"{s_name} : ")))

        ovr = calculate_ovr(new_stats, new_pos)
        new_price = ovr * 9.0

        market_players.append([new_name, new_pos, new_stats[0],new_stats[1], new_stats[2], new_stats[3], new_stats[4], new_stats[5], new_price])   
        print(f"▶ {new_name} 등록 완료! (OVR : {ovr:.1f} / 가치 : {new_price:.1f}억 원)")

def enter_transfer_market() : 
    global team_budget 
    global is_signed
    global target_player
    i = 0

    try_count = int(input("최대 몇 번의 영입 시도를 하시겠습니까? (숫자 입력): "))

    for i in range(try_count):
        is_signed = False 
    
        print(f"\n--- [영입 기회: {i+1} / {try_count}] ---")
        target_player = input("영입할 선수의 이름을 정확히 입력하세요 (조기 종료: 'exit'): ")
    
        if target_player.lower() == 'exit':
            print("이적 시장 쇼핑을 조기 종료하고 메인 메뉴로 돌아갑니다.")
            break # for 반복문을 즉시 빠져나감
        
    # 시장 데이터베이스 탐색
        found_player = None
        for p in market_players:
            if p[0] == target_player:
                found_player = p
                break
            
        if found_player:
            p_name, p_pos = found_player[0], found_player[1]
            s = found_player[2:8] 
            p_price = found_player[8]

            ovr = calculate_ovr(s,p_pos)
        
            print(f"🔍 선수 발견: {p_name} ({p_pos}) | 이적료: {p_price:.1f}억 원")
            print("▶스카우터 예상 등급 : ", end = "")

            if ovr >= 90 :
                print("S등급(월드클래스)")
            elif ovr >= 80 :
                print("A등급(즉시 전력감)")
            elif ovr >= 70 :
                print("B등급(유망주)")
            else : 
                print("C등급(영입 보류 권장)")

        if team_budget >= p_price:
            confirm = input(f"✅ 예산 충분! {p_name}을(를) 영입하시겠습니까? (y/n): ")
            if confirm.lower() == 'y':
                team_budget -= p_price
                my_team.append(f"{p_name} ({p_pos})")
                is_signed = True
                print(f"🎊 영입 성공! 스쿼드에 등록되었습니다.")
            else:
                print("영입을 취소했습니다.")
                is_signed = True
        else:
            print(f"❌ 예산 부족! (부족 금액: {p_price - team_budget:.1f}억 원)")
            is_signed = True
    else:
        print(f"⚠️ '{target_player}' 선수를 찾을 수 없습니다.")

    if is_signed:
        display_squad_info()

def display_squad_info() :
    print(f"\n--- 현재 {manager_name} 감독의 스쿼드 ---")
    if not my_team : 
        print("(영입된 선수 없음)")
    else : 
        for idx, member in enumerate(my_team) :
            print(f"{idx+1}. {member}")
    print(f"💰 현재 잔여 예산 : {team_budget:.1f}억 원")

print("=" * 40)
print(" ⚽ 방구석 명장 스카우트 시스템 ⚽")
print("=" * 40)

manager_name = input("감독님의 이름을 입력하세요 : ")
team_budget = float(input("구단 초기 예산을 입력하세요(단위 : 억 원, 실수형으로 숫자만 입력하세요, ex : 4000) : "))

print(f"\n환영합니다, {manager_name} 감독님!")
print(f"현재 구단 예산은 {team_budget:.1f}억 원이며, 이적 시장에는 {len(market_players)}명의 선수가 있습니다.")

while True : 
    print("\n" + "="*25)
    print("📌 [구단 관리 메인 메뉴]")
    print("1. 신인 선수 등록 (입력)")
    print("2. 이적 시장 오픈 (영입/분석)")
    print("3. 내 스쿼드 조회 (조회)")
    print("4. 시스템 종료")
    print("="*25)

    menu_choice = input("원하시는 메뉴 번호를 선택하세요 (1~4) : ")

    if menu_choice == "1" : 
        register_rookie()
    elif menu_choice == "2" : 
        enter_transfer_market()
    elif menu_choice == "3" :
        display_squad_info() 
        input("\n(엔터 키를 누르면 메인 메뉴로 돌아갑니다...)")
    elif menu_choice == "4" :
        print("\n" + "=" * 40)
        print(f"이적 시장 종료! {manager_name} 감독님의 영입 결과")
        display_squad_info()
        print("방구석 명장 시스템을 이용해 주셔서 감사합니다.")
        print("=" * 40)
        break 
    else : 
        print("잘못된 입력입니다. 1번부터 4번 사이의 숫자를 입력해 주세요.")
        input("\n(엔터 키를 누르면 메인 메뉴로 돌아갑니다...)")
