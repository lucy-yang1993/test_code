# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 16:24:32 2021

@author: admin_yl
"""

import easyocr



# 创建reader对象
reader = easyocr.Reader(['ch_sim']) 
# 读取图像
result = reader.readtext('test_pic.png')
# 结果
print(result)

