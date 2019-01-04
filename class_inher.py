class RequestFactory(object):
    def __init__(self, **defaults):
        print("RequestFactory__start", defaults)
        super().__init__(**defaults)
        print("RequestFactory__end", defaults)

class RequestMockWithoutUser(RequestFactory):
    """docstring for RequestMockWithoutUser"""
    def __init__(self, **defaults):
        super().__init__(**defaults)


class RequestObjects(object):
    """docstring for RequestObjects"""
    def __init__(self, **kwargs):
        print("RequestObjects--->", kwargs)

class RequestMock(RequestMockWithoutUser, RequestObjects):
    """docstring for RequestMock"""
    def __init__(self, **kwargs):
        print("RequestMock___start", kwargs)
        super().__init__(**kwargs)
        print("RequestMock___end", kwargs)


if __name__ == '__main__':
    RequestMock(permissions=["aaaaaa"])
    print("==>", RequestMock.mro())
