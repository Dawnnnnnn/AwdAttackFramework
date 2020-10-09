#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/9/28 21:41
# @Author  : Dawnnnnnn
# @Contact: 1050596704@qq.com
from framework.attack_framework import Session, Attack, Utils, logger
from pwn import *

target_file = "pwn1.txt"
attack = Attack(target_file)
session = Session()
utils = Utils()


def payload(ip):
    url = ip.split(":")[0]
    port = ip.split(":")[1]
    conn = remote(url, port)
    conn.send(b'USER anonymous\r\n')
    # conn.recvuntil(b' ', drop=True)
    conn.recvline()
    conn.close()


attack.attack(func=payload)
