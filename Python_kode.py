import numpy as np

planes = 200
lanes = 1
t = 0
wait = [0]

landing = np.random.randint(0, 200, planes)
arrival = np.random.randint(0, 200, planes)


interval_0_59 = np.random.randint(0, 60, int(planes//(200/44)))
interval_60_119 = np.random.randint(60, 120, int(planes//(200/34)))
interval_120_179 = np.random.randint(120, 180, int(planes//(200/27)))
interval_180_239 = np.random.randint(180, 240, int(planes//(200/22)))
interval_240_299 = np.random.randint(240, 300, int(planes//(200/16)))
interval_300_359 = np.random.randint(300, 360, int(planes//(200/13)))
interval_360_419 = np.random.randint(360, 420, int(planes//(200/10)))
interval_420_479 = np.random.randint(420, 480, int(planes//(200/8)))
interval_480_539 = np.random.randint(480, 540, int(planes//(200/6)))
interval_540_599 = np.random.randint(540, 600, int(planes//(200/5)))
interval_600_659 = np.random.randint(600, 660, int(planes//(200/4)))
interval_660_719 = np.random.randint(660, 720, int(planes//(200/3)))
interval_720_779 = np.random.randint(720, 780, int(planes//(200/2)))
interval_780_839 = np.random.randint(780, 840, int(planes//(200/2)))
interval_840_899 = np.random.randint(840, 900, int(planes//(200/1)))
interval_900_959 = np.random.randint(900, 960, int(planes//(200/1)))
interval_960_1019 = np.random.randint(960, 1020, int(planes//(200/1)))
interval_1020_1079 = np.random.randint(1020, 1080, 0)
interval_1080_1139 = np.random.randint(1080, 1140, int(planes//(200/1)))
interval_1140_1199 = np.random.randint(1140, 1200, 0)

arrival_test = [0 for i in range(planes)]

arrival_test[:44] = interval_0_59
arrival_test[43:78] = interval_60_119
arrival_test[77:105] = interval_120_179
arrival_test[104:127] = interval_180_239

print(arrival_test)
# =============================================================================
# for i in range(1, planes):
#     V = (landing[i-1] - arrival[i]) + wait[i-1]
#     
#     if V < 0:
#         V = 0
#     
#     wait.append(V)
# 
# average_wait_time = sum(wait)/len(wait)
# total_wait_time = sum(wait)
# print(total_wait_time, '\n', average_wait_time)
# =============================================================================
