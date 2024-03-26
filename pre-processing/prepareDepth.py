WeChat: cstutorcs
QQ: 749389476
Email: tutorcs@163.com
import os
for i in range(9999):
    try:
        os.popen(f"Ren {i}.png depth{i}.png").read()
    except:
        break