#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/9/17 16:14
# @Author  : Dawnnnnnn
# @Contact: 1050596704@qq.com
from framework.attack_framework import Session, Attack, Utils, logger

target_file = "web1.txt"
attack = Attack(target_file)
session = Session()
utils = Utils()


def payload(ip):
    """
    攻击流程和flag获取流程
    # flag = re.findall(r"([a-fA-F\d]{32})", res.text) 匹配32位字符串
    # flag = re.findall(r"\{.*\}",res.text) 匹配花括号
    # attack.trans_flag(ip, flag)
    :return:
    """
    pass


attack.attack(func=payload)
