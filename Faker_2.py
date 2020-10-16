from faker import Faker


class GenerateRandomTestData:
    '''
    生成随机测试数据
    '''
    def __init__(self):
        self.f = Faker(locale='zh_CN')  # zh_CN代表中文，不传locale默认值为en_US

    def random_name(self):
        '''
        随机姓名
        :return:
        '''
        return self.f.name()

    def random_username(self):
        '''
        随机用户名
        :return:
        '''
        return self.f.user_name()

    def random_password(self, length=10, special_chars=True, digits=True, upper_case=True, lower_case=True):
        '''
        随机密码
        :param length: 密码长度
        :param special_chars: 是否可使用特殊字符
        :param digits: 是否包含数字
        :param upper_case: 是否包含大写字母
        :param lower_case: 是否包含小写字母
        :return:
        '''
        return self.f.password(length=length,
                               special_chars=special_chars,
                               digits=digits,
                               upper_case=upper_case,
                               lower_case=lower_case)

    def random_mobile_phone_num(self):
        '''
        随机手机号
        :return:
        '''
        return self.f.phone_number()

    def random_id_card_num(self):
        '''
        随机身份证号
        :return:
        '''
        return self.f.ssn()

    def random_email(self):
        '''
        随机邮箱
        :return:
        '''
        return self.f.email()

    def random_address(self):
        '''
        随机地址
        :return:
        '''
        return self.f.address()

    def random_url(self):
        '''
        随机url
        :return:
        '''
        return self.f.url()

    def random_ipv4(self):
        '''
        随机ipv4（IP号）
        :return:
        '''
        return self.f.ipv4()

    def random_md5(self):
        '''
        随机MD5加密串
        :return:
        '''
        return self.f.md5()

f =GenerateRandomTestData()
x =GenerateRandomTestData
print(x.random_name(f))

