"""
    自动提交代码
"""
import time
from subprocess import PIPE, Popen

import paramiko


def localSsh(command):
    data_form = """***********************************************************************************\n{}执行结果:\n-----------------------------------------------------------------------------------\n{}***********************************************************************************"""
    start_data = f"开始在本地服务器上执行指令:{command}"
    print(start_data)
    try:
        p = Popen(command,
                  stdin=None,
                  stdout=PIPE,
                  stderr=PIPE, shell=True)
        # out, err = p.communicate()
        out = p.stdout.read().decode("utf-8")
        err = p.stderr.read().decode("utf-8")
        if err != "":
            result_data = data_form.format("本地服务器", err)
            print(result_data)
            return False, start_data + "\n" + result_data
        result_data = data_form.format("本地服务器", out)
        print(result_data)
        return True, start_data + "\n" + result_data
    except Exception as e:
        print(e)
        return False, start_data + "\n" + str(e)


# 远程登陆操作系统
def remoteSsh(sys_ip, username, command, password='', port=22):
    data_form = """***********************************************************************************\n{}执行结果:\n-----------------------------------------------------------------------------------\n{}***********************************************************************************"""
    result_data = ""
    try:
        # 创建ssh客户端
        client = paramiko.SSHClient()
        # 第一次ssh远程时会提示输入yes或者no
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        client.connect(sys_ip, port=port, username=username, password=password, timeout=20)
        start_data = f"开始在远程服务器上执行指令:{command}"
        print(start_data)
        # 执行查询命令
        stdin, stdout, stderr = client.exec_command(f"""{command}""", get_pty=True)
        # 获取查询命令执c行结果,返回的数据是一个list
        result = stdout.read().decode('utf-8')
        print(data_form.format(sys_ip, result))
        result_data = start_data + "\n" + data_form.format(sys_ip, result)
        error = stderr.read().decode('utf-8')
        if error != "":
            err_data = data_form.format(sys_ip, error)
            print(err_data)
            result_data = start_data + "\n" + data_form.format(sys_ip, result) + "\n" + err_data
    except Exception as e:
        print(e)
        result_data = e
    finally:
        client.close()
        return result_data


# 批量执行同一命令
def batchExecuteRemoteCommand(host_list, command):
    import threading
    thread_list = []
    for ip, username, password in host_list:
        thread = threading.Thread(target=remoteSsh, args=(ip, username, password, command))
        thread_list.append(thread)  # 将生成的线程添加到列表里
    for t in thread_list:
        t.start()  # 开始执行线程
    for t in thread_list:
        t.join()  # 挂起线程，到所有线程结束


def write_log(data):
    with open("autocommit.log", "a+", encoding="utf-8") as f:
        f.write(data)


def main(start_time, local_command, remote_ip, remote_port, remote_user, remote_password, remote_command):
    local_result = localSsh(local_command)
    print("------测试代码------")
    print(local_result)
    print("------测试代码------")
    if local_result[0]:
        remote_result = remoteSsh(sys_ip=remote_ip, username=remote_user,
                                  command=remote_command, password=remote_password,
                                  port=remote_port)
        result = start_time + "\n" + local_result[1] + "\n" + remote_result
    else:
        print(start_time + "\n" + "执行失败")
        result = start_time + "\n" + "执行失败" + "\n" + local_result[1]
    write_log(result)


if __name__ == '__main__':
    start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    local_command = f'D: && cd D:\Code\Py\my_api\my_api && git add . && git commit -m "{start_time}commit" && git pull orgin master && git push orgin master'
    remote_ip = "82.157.9.233"
    remote_port = 1128  # 默认22
    remote_user = "root"
    remote_password = "Concon95"
    remote_command = "cd /home/project/my_api;git pull origin master"
    main(start_time, local_command, remote_ip, remote_port, remote_user, remote_password, remote_command)
