import glob
import os
import time
import re
import sys
import ADC_function
import json
import shutil
import core

# dirname = os.path.join(os.getcwd(),'testdir')
dirname = "Z:\PTDownload\movie\电影"


def movie_lists():
    total = []
    for maindir, subdir, file_name_list in os.walk(dirname):
        for filename in file_name_list:
            if filename.endswith("mkv") or filename.endswith("iso"):
                apath = os.path.join(maindir, filename)  # 合并成一个完整路径
                total.append(apath)
    return total


def lists_from_test(custom_nuber): #电影列表

    a=[]
    a.append(custom_nuber)
    return a


def CEF(path):
    files = os.listdir(path)  # 获取路径下的子文件(夹)列表
    for file in files:
        try:    # 试图删除空目录,非空目录删除会报错
            os.removedirs(path + '/' + file)  # 删除这个空文件夹
            print('[+]Deleting empty folder', path + '/' + file)
        except:
            a=''


def rreplace(self, old, new, *max):
    # 从右开始替换文件名中内容，源字符串，将被替换的子字符串， 新字符串，用于替换old子字符串，可选字符串, 替换不超过 max 次
    count = len(self)
    if max and str(max[0]).isdigit():
        count = max[0]
    return new.join(self.rsplit(old, count))

def getMovieName(filepath):
        try:
            filepath = filepath[filepath.rfind('\\')+1:]
            movie_name = re.findall(r'(.+)\.(\d{4})\..+\w{3}$', filepath)[0]
            return movie_name
        except Exception as e:
            print(e)


if __name__ =='__main__':
    print('[*]===========DouBanMovie Data Capture===========')
    print('[*]=====================================')
    os.chdir(os.getcwd())
    count = 0
    count_all = str(len(movie_lists()))
    for i in movie_lists(): #遍历电影列表 交给core处理
        count = count + 1
        percentage = str(count/int(count_all)*100)[:4]+'%'
        print('[!] - '+percentage+' ['+str(count)+'/'+count_all+'] -')
        movieInfo = getMovieName(i)
        print("[!]正在处理\t" + i + ",\n电影名:\t" + movieInfo[0] + "\n年份:\t" + movieInfo[1])
        core.run(i, movieInfo)
        print("[*]=====================================")

    print("[+]All finished!!!")
    input("[+][+]Press enter key exit, you can check the error messge before you exit.\n[+][+]按回车键结束，你可以在结束之前查看和错误信息。")