


def get_xsrf():
    req = opener.open("https://www.zhihu.com")
    html = req.read().decode("utf-8")
    get_xsrf_pattern = re.complie(r'<input type="hidden" name="_xsrf" value="(.*?)"')
    _xsrf = re.findall(get_xsrf_pattern)
    print("====_xsrf:", _xsrf)
    return _xsrf[0]


