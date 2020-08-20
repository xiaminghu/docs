import re
import os
import sys
import json
import base64
import random

import rsa
import requests

CONFIG_FILE_NAME = '.auto-pages.json'
IGNORE_FILE_NAME = '.gitignore'

PUBLIC_KEY = """
-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDIrn+WB2Yi4ABAL5Tq6E09tumY
qVTFdpU01kCDUmClczJOCGZriLNMrshmN9NJxazpqizPthwS1OIK3HwRLEP9D3GL
7gCnvN6lpIpoVwppWd65f/rK2ewv6dstN0fCmtVj4WsLUchWlgNuVTfWljiBK/Dc
YkfslRZzCq5Fl3ooowIDAQAB
-----END PUBLIC KEY-----
""".strip('\n')

USER_AGENTS = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; "
    "SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; "
    "SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; "
    "Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; "
    "Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; "
    ".NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; "
    "Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; "
    ".NET CLR 3.5.30729; .NET CLR 3.0.30729; "
    ".NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; "
    "Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; "
    "InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) "
    "AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) "
    "Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ "
    "(KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; "
    "rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) "
    "Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) "
    "Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) "
    "Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 "
    "(KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) "
    "AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) "
    "Presto/2.9.168 Version/11.52",
]


class AutoPages:
    def __init__(self):
        # support one scripts to deploy multiple pages
        self.base_dir = self.get_base_dir_from_argv()
        os.chdir(self.base_dir)
        # initialize
        data = self.get_config()
        self.username = data.get('username')
        self.password = data.get('password')
        self.repo = data.get('repo')
        self.branch = data.get('branch')
        self.directory = data.get('directory')
        self.https = data.get('https')
        # print(data)
        # spider actions
        self.session = requests.session()
        self.run()

    @staticmethod
    def get_base_dir_from_argv():
        """get second paramter as base_dir so that user could use one script to deploy multiple pages"""
        if len(sys.argv) >= 2:
            # if the second param is passed
            rel_path = sys.argv[1]
            if os.path.exists(rel_path):
                base_dir = os.path.abspath(rel_path)
            else:
                raise AssertionError("Directory does not exists, please checkout your second parameter.")
        else:
            base_dir = os.getcwd()

        return base_dir

    def ensure_ignored(self):
        """
        user data shouldn't be uploaded to git repos,
        this function is create to ensure ${CONFIG_FILE_NAME} is added into .gitignore
        :return:
        """
        try:
            with open(IGNORE_FILE_NAME) as f:
                return any([line for line in f.read().split('\n') if line.strip() == CONFIG_FILE_NAME])
        except FileNotFoundError:
            raise AssertionError(
                "Couldn't find %s in directory %s, please check it out" % (IGNORE_FILE_NAME, self.base_dir))

    def get_config(self) -> dict:
        """
        here we'll do all the validations of parameters
        :return:
        """
        default_data = {
            'username': '',
            'password': '',
            'repo': '',
            'branch': 'gh-pages',
            'directory': '',
            'https': True
        }
        if not self.ensure_ignored():
            raise AssertionError("%s hasn't been added into %s" % (CONFIG_FILE_NAME, IGNORE_FILE_NAME))

        try:
            with open(CONFIG_FILE_NAME) as f:
                data = json.load(f)
        # actually here we do a useless action because it would raise an exception automatically if file doesn't exists
        # but I'm doing this to remind me that I've already catch this exception
        # and would be easier in future if I'm going to handle this exception in another way
        except FileNotFoundError:
            raise AssertionError(
                "Couldn't find %s in directory %s, please check it out" % (CONFIG_FILE_NAME, self.base_dir))

        if not (data.get('username') and data.get('password') and data.get('repo')):
            raise AssertionError(
                "Please make sure that `username`, `password`, `repo` is configured in %s" % CONFIG_FILE_NAME)

        default_data.update(data)
        return default_data

    def validate_repo(self):
        help_text = '''
        suppose the full url of your repo is: https://gitee.com/xiaminghu/project
        then the parameter `repo` should like `xiaminghu/project`
        with no prefix `https://gitee.com/` and no suffix `.git`
        please modify `repo` before you retry next time
        '''

        # replace repo so that we also support config full url of repo
        self.repo = self.repo.replace('https://gitee.com/', '').replace('.git', '')
        full_url = 'https://gitee.com/%s' % self.repo
        response = self.session.get(full_url)
        if response.status_code != 200:
            print(response.status_code)
            raise AssertionError("parameter `repo` is not correctly configured!\n\n%s" % help_text)

    @staticmethod
    def get_csrf_token(html):
        return re.search(
            '<meta content="authenticity_token" name="csrf-param" />(.*?)'
            '<meta content="(.*?)" name="csrf-token" />', html, re.S).group(2)

    def login(self):
        login_index_url = 'https://gitee.com/login'
        check_login_url = 'https://gitee.com/check_user_login'
        form_data = {'user_login': self.username}

        index_headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;'
                      'q=0.9,image/webp,image/apng,*/*;'
                      'q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Host': 'gitee.com',
            'User-Agent': random.choice(USER_AGENTS)
        }

        # request login page to get csrf token
        resp = self.session.get(login_index_url, headers=index_headers, timeout=5)
        csrf_token = self.get_csrf_token(resp.text)
        headers = {
            'Referer': 'https://gitee.com/login',
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRF-Token': csrf_token,
            'User-Agent': random.choice(USER_AGENTS)
        }
        self.session.post(check_login_url, headers=headers, data=form_data, timeout=5)
        data = '%s$gitee$%s' % (csrf_token, self.password)
        pubkey = rsa.PublicKey.load_pkcs1_openssl_pem(PUBLIC_KEY.encode())
        encrypt_data = rsa.encrypt(data.encode(), pubkey)
        encrypt_data = base64.b64encode(encrypt_data).decode()

        form_data = {
            'encrypt_key': 'password',
            'utf8': '✓',
            'authenticity_token': csrf_token,
            'redirect_to_url': '',
            'user[login]': self.username,
            'encrypt_data[user[password]]': encrypt_data,
            'user[remember_me]': 1
        }
        resp = self.session.post(login_index_url, headers=index_headers, data=form_data, timeout=5)
        return '个人主页' in resp.text or '我的工作台' in resp.text

    def rebuild_pages(self):
        # verify the configuration of repo
        self.validate_repo()
        pages_url = 'https://gitee.com/%s/pages' % self.repo
        rebuild_url = '%s/rebuild' % pages_url

        pages = self.session.get(pages_url)
        csrf_token = self.get_csrf_token(pages.text)
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Referer': pages_url,
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRF-Token': csrf_token,
            'User-Agent': random.choice(USER_AGENTS)
        }
        form_data = {
            'branch': self.branch,
            'build_directory': self.directory,
            'force_https': self.https
        }
        resp = self.session.post(rebuild_url, headers=headers, data=form_data, timeout=5)
        return resp.status_code == 200

    def run(self):
        if not self.login():
            raise AssertionError("Login Failed! Please checkout your username and password.")
        if not self.rebuild_pages():
            raise AssertionError("Rebuild Pages Failed! Please checkout `branch`, `directory` ensuring it exists")
        print("deployed successfully, repo link: https://gitee.com/%s" % self.repo)
        self.session.close()


if __name__ == '__main__':
    AutoPages()
