import sys
print('LKF: ⬇')
print('模块搜索路径', end = '\n\n')
sys.path.append('/home/JYF2')
for p in sys.path:
    print(p)