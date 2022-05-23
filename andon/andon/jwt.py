import base64
import copy
import hmac
import json
import time


class Jwt():
    def __init__(self):
        pass

    @staticmethod
    def encode(payload, key, exp=300):
        """exp为此时间戳过期时间"""
        # init header
        """JWT 三大组成
        1.header: 格式为字典， 元数据格式如下
        alg表示要使用的算法， typ代表该token的类别
        2.payload:格式为字典，此部分分为共有声明和私有声明
        公共声明：JWT使用了内置关键字用于描述常见问题，此部分为可选项，用户可以根据自己需求，按需添加key.
        私有声明：用户可根据自己的业务需求，添加自定义的key
        3.sign签名
        HS256(自定义的key， base64后的header+'.'+base64后的payload)
        即：用自定义的key，对base64后的header+ '.'+ base64后的payload进行hmac计算"""
        header = {'typ': 'JWT', 'alg': 'HS256'}
        header_json = json.dumps(header, separators=(',', ':'), sort_keys=True)
        # 生成b64header
        header_bs = Jwt.b64encode(header_json.encode())

        # 参数中的payload {'username': 'aaa'}
        payload = copy.deepcopy(payload)
        # 添加公有声明-exp且值为未来时间戳
        payload['exp'] = int(time.time()) + exp
        payload_json = json.dumps(payload, separators=(',', ':'), sort_keys=True)
        payload_bs = Jwt.b64encode(payload_json.encode())

        # 签名
        # 判断传入的key的类型
        if isinstance(key, str):
            key = key.encode()
        hm = hmac.new(key, header_bs + b'.' + payload_bs, digestmod='SHA256')
        hm_bs = Jwt.b64encode(hm.digest())

        return header_bs + b'.' + payload_bs + b'.' +hm_bs

    @staticmethod
    def b64encode(j_s):
        # 替换生成出来的b64串中的占位符
        return base64.urlsafe_b64decode(j_s).replace(b'=', b'')

    @staticmethod
    def b64decode(b64_s):
        rem = len(b64_s) % 4
        if rem > 0:
            b64_s += b'=' * (4-rem)
            return base64.urlsafe_b64decode(b64_s)

    @staticmethod
    def decode(token, key):
        # 校验两次HMAC结果
        # 检查exp公有声明的有效性
        # header_b, payload_b, sign = token.split(b'.')
        if isinstance(key, str):
            key = key.encode()
        # 比较两次HMAC结果
        hm = hmac.new(key, header_b)