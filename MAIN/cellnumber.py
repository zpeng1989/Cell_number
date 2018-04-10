#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 17:31:52 2018

@author: zhangp
"""

import cv2
import numpy as np
import os



def total_number_function(input_path, cut_off, area_data, screen_ratio):
    input_file_path = os.path.dirname(input_path)
    input_file_name = os.path.basename(input_path)
    img = cv2.imread(input_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gauss  = cv2.GaussianBlur(gray, (5,5), 0)
    _, threshed = cv2.threshold(gauss, cut_off, 255, cv2.THRESH_BINARY_INV )
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
    morphed = cv2.morphologyEx(threshed, cv2.MORPH_OPEN, kernel, None, (-1,-1), 1)
    _, cnts, _ = cv2.findContours(morphed, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    canvas = img.copy()
    cv2.drawContours(canvas,cnts, -1,  (0,200,200), 1)
    canvasl = canvas
    xcnts = []
    number = 0
    new_area = 0
    for cnt in cnts:
        area = cv2.contourArea(cnt)
        x,y,w,h = cv2.boundingRect(cnt)
        if area < area_data or area/(w*h) < screen_ratio:
            continue
        number = number + 1
        new_area = new_area + area
        xcnts.append(cnt)
        text = str(number)
        cv2.putText(canvas,text,(x,y), cv2.FONT_HERSHEY_SIMPLEX,  .3, (0, 0, 255), 1, 2)
        cv2.putText(morphed,text,(x,y), cv2.FONT_HERSHEY_SIMPLEX,  .3, (255, 255, 255), 1, 2)
    cv2.drawContours(canvas, xcnts, -1,  (100,20,200),1)

    all_total = len(cnts)
    part_total = len(xcnts)
    number_bty = len(xcnts)/(len(cnts)+1)
    area_bty = new_area/(canvas.shape[1]*canvas.shape[0])
    src_path = input_file_path + '/src_' + input_file_name + '.png'
    dst_path = input_file_path + '/dst_' + input_file_name + '.png'
    one_two_path = input_file_path + '/one_two_' + input_file_name + '.png'
    edge_path = input_file_path + '/edge_' + input_file_name + '.png'
    if os.path.exists(src_path):
        os.remove(src_path)
    if os.path.exists(dst_path):
        os.remove(dst_path)
    if os.path.exists(one_two_path):
        os.remove(one_two_path)
    if os.path.exists(edge_path):
        os.remove(edge_path)

    cv2.imwrite(src_path, img)
    cv2.imwrite(dst_path, canvas)
    cv2.imwrite(one_two_path, threshed)
    cv2.imwrite(edge_path, morphed)
    return [all_total, part_total, number_bty, area_bty,src_path,dst_path,one_two_path,edge_path]
'''
input_path = 'C:/Users/zhangp/.spyder-py3/workspace/20180409/cells.jpg'
cut_off = 150
area_data = 7
screen_ratio = 0.3
[one,two,three,four] = total_number_function(input_path, cut_off, area_data, screen_ratio)
'''
