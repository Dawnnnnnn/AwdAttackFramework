#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/9/27 14:33
# @Author  : Dawnnnnnn
# @Contact: 1050596704@qq.com
import paramiko
import traceback
from loguru import logger
from config.config import *

logger.add('ssh_log.txt')


class SSHLogin:
    def __init__(self):
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def change_pwd(self, ip, port, login_user, modify_user, old_password, new_password):
        try:
            self.ssh = paramiko.SSHClient()
            self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh.connect(hostname=ip, port=port, username=login_user, password=old_password, timeout=5)
            if login_user == "root":
                command = f"passwd {modify_user}\n"
                stdin, stdout, stderr = self.ssh.exec_command(command)
                stdin.write(new_password + '\n' + new_password + '\n')
            else:
                command = f"passwd \n"
                stdin, stdout, stderr = self.ssh.exec_command(command)
                stdin.write(old_password + '\n' + new_password + '\n' + new_password + '\n')
            out, err = stdout.read(), stderr.read()
            logger.info(out, err)
            if "successfully" in str(out) or "successfully" in str(err):
                logger.info(f"{ip}密码修改成功")
            else:
                logger.error(f"{ip}密码修改失败{str(err)}")
            self.ssh.close()
        except paramiko.ssh_exception.AuthenticationException as e:
            logger.error(f"{ip}账号密码错误{e}")
        except:
            traceback.print_exc()

    def run(self):
        with open("ssh.txt", "r")as f:
            for ip in f.readlines():
                ip = ip.strip()
                port = ip.split(":")[1]
                ip = ip.split(":")[0]
                self.change_pwd(ip, port, login_user=LOGIN_USER, modify_user=MODIFY_USER,
                                old_password=OLD_PASSWORD,
                                new_password=NEW_PASSWORD)


SSHLogin().run()
