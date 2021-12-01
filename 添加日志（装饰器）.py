# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 10:40:43 2021

@author: admin_yl
"""
import datetime,time
import sys

def log(func):
    file_road = sys.argv[0]    #读取当前程序名称及路径
    def inner():        
        start_time = datetime.datetime.now()
        with open("python.log","a") as f:
            f.write("="*20+'\n')
            f.write('[run_file]:{0}'.format(file_road) +'\n')
            try:
                end_time = datetime.datetime.now()
                func()
                info = 'Run Successful'
                f.write("[start]:{0};[end]:{1}".format(start_time,end_time)+'\n')
                f.write("[info]:{0}".format(info)+'\n')                
            except Exception as ex:
                end_time = datetime.datetime.now()
                info = ex
                f.write("[start]:{0};[end]:{1}".format(start_time,end_time)+'\n')
                f.write("[info]:{0}".format(info)+'\n')                
                sys.exit(0)  #结束程序
    return inner

@log
def test_func():
    print('123')
    time.sleep(10)
    

if __name__ == "__main__":
    
    for i in range(5):
        test_func()
        