# 이중 for문 빠져나오기
# for 바깥조건:
#     바깥동작
#     for 안쪽조건:
#         안쪽동작
#         if 충돌하면:
#             break
#     else:
#         continue
#     break

balls = [1, 2, 3, 4]
weapons = [11, 22, 3, 44]

for ball_idx, ball_val in enumerate(balls):
    print("ball :", ball_val)
    for weapon_idx, weapon_val in enumerate(weapons):
        print("weapon :", weapon_val)
        if ball_val == weapon_val:  # 충돌 체크
            print("공과 무기가 충돌")
            break
    else:
        continue
    break
