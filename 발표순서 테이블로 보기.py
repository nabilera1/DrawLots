from prettytable import PrettyTable
import random


def random_order_table(N):
    # 1부터 N까지의 숫자 리스트 생성
    numbers = list(range(1, N + 1))

    # numbers 리스트에서 N개의 숫자를 랜덤하게 선택 (즉, 리스트를 랜덤하게 섞음)
    random_order = random.sample(numbers, N)

    # PrettyTable 객체 생성
    table = PrettyTable()

    # 테이블에 컬럼 이름 추가
    table.field_names = ["발표 순서", "학생 번호"]

    # 랜덤하게 섞인 순서대로 테이블에 학생 번호 추가
    for i, number in enumerate(random_order, 1):
        table.add_row([i, number])

    print(table)


# 예시로, N=20인 경우의 랜덤 순서를 표 형태로 출력
N = 20
random_order_table(N)
