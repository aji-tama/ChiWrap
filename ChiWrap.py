# coding: UTF-8

import re
import numpy

##def wrap(source_text,n):
##    
##    text_trim = [text_FW.strip() for text_FW in str(source_text)
##                 .replace('<br/>','').replace('<br','').replace(' ','').replace(':','：').replace('(','（').replace(')','）').splitlines() if text_FW]
##    text_trim_line = ''.join(text_trim)
##
##    hw = list(range(10,100))
##    text_trim_lines = []
##    m_list = [0]
##
##    hw_n = sum([text_trim_line.count(str(ele)) for ele in hw])
##
##    for i in range(0, len(text_trim_line), n): # i = starting int
##        m = sum([text_trim_line[i+sum(m_list[0:-1]):i+sum(m_list)+n].count(str(ele)) for ele in hw]) # m = no. of halfwidth chara
##        m_list.append(m)
##        text_trim_lines.append(text_trim_line[i+sum(m_list[0:-1]):i+sum(m_list)+n])
##                    
##    return ['\n'.join(text_trim_lines),len(text_trim_lines)]

def wrap3(source_text,n):
    
    text_trim = [text_FW.strip() for text_FW in str(source_text)
                 .replace('<br/>','').replace('<br','').replace(' ','').replace(':','：').replace('(','（').replace(')','）').splitlines() if text_FW]
    text_trim_line = [char for char in text_trim[0]]

    para = []
    count = 0
    ln_cnt = 1
    for i in range(len(text_trim_line)):
        if text_trim_line[i] in ['0','1','2','3','4','5','6','7','8','9']: # if half width
            count = count+0.5
            if count <= n:
                para.append(text_trim_line[i])
            else:
                para.append('\n')
                if text_trim_line[i] in ['0','1','2','3','4','5','6','7','8','9']: # reset count
                    count = 0.5
                    para.append(text_trim_line[i])
                    ln_cnt = ln_cnt + 1
                else:
                    count = 1
                    para.append(text_trim_line[i])
                    ln_cnt = ln_cnt + 1
        else: # if full width
            count = count + 1
            if count <= n:
                para.append(text_trim_line[i])
            else:
                para.append('\n')
                if text_trim_line[i] in ['0','1','2','3','4','5','6','7','8','9']:
                    count = 0.5
                    para.append(text_trim_line[i])
                    ln_cnt = ln_cnt + 1
                else:
                    count = 1
                    para.append(text_trim_line[i])
                    ln_cnt = ln_cnt + 1
                
    return [''.join(para),ln_cnt]

if __name__ == "__main__":
    text_sample0 = '一股西南氣流正影響廣東沿岸。本港今早有驟雨，九龍城、油尖旺及黃大仙區錄得約10毫29米雨量。本港地區今日天氣預測:部分時間有陽光，局部地區有驟雨。日間酷熱，最高氣溫約33度。吹和緩西南風。展望: 未來兩三日部分時間有陽光，天氣酷熱，但局部地區有驟雨。'
    text_sample1 = '一股西南氣流正影響廣東沿岸。同時，高空反氣旋正為南海北部帶來普遍晴朗的天氣。下午本港大部分地區氣溫上升至33度左右。本港地區今晚及明日天氣預測:大致天晴。明日有一兩陣驟雨，最低氣溫約29度。日間酷熱，市區最高氣溫約33度，新界再高一兩度。吹和緩西南風，離岸風勢間中清勁。展望: 隨後一兩日部分時間有陽光及酷熱，但有一兩陣驟雨。下週中期驟雨增多。'
    #print(wrap(text_sample1,18)[1])
    print(wrap3(text_sample1,21)[0])
    print(wrap3(text_sample1,21)[1])
