from datetime import datetime

def calculate_year_progress(date_str):
    # 문자열을 datetime 객체로 변환
    current_time = datetime.strptime(date_str, '%B %d, %Y %H:%M')
    
    # 올해의 시작과 끝 날짜 설정
    start_of_year = datetime(current_time.year, 1, 1)
    end_of_year = datetime(current_time.year + 1, 1, 1)
    
    # 총 초 계산 (연도의 총 초 수)
    total_seconds = (end_of_year - start_of_year).total_seconds()
    
    # 현재까지 경과한 초 계산
    elapsed_seconds = (current_time - start_of_year).total_seconds()
    
    # 진행률 계산
    progress_percentage = (elapsed_seconds / total_seconds) * 100
    
    return progress_percentage 

# 입력 예시
date_str = input()  # 입력: "Month DD, YYYY HH:MM"
progress_percentage = calculate_year_progress(date_str)
print(f"{progress_percentage:.9f}")
