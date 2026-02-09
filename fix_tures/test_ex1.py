import pytest

# @pytest.fixture()
# def greet():
#     print("good morning sanju")
#     yield
#     print("good night sanju")
#
# def test_login(greet):
#     print("login executing")
#
# def test_signup(greet):
#     print("signup executing")
#
# def test_logout(greet):
#     print("logout executing")

# @pytest.fixture(autouse=True)
# def greet():
#     print("good morning sanju")
#     yield
#     print("good night sanju")
#
# def test_login():
#     print("login executing")
#
# def test_signup():
#     print("signup executing")
#
# def test_logout():
#     print("logout executing")


# @pytest.fixture(autouse=True)
# def greet():
#     print("good morning sanju")
#     yield
#     print("good night sanju")
#
# class TestSample:
#     def test_login(self):
#         print("login executing")
#
#     def test_signup(self):
#         print("signup executing")
#
#     def test_logout(self):
#         print("logout executing")

@pytest.fixture(autouse=True,scope='class')
def greet():
    print("good morning sanju")
    yield
    print("good night sanju")

class TestSample:
    def test_login(self):
        print("login executing")

    def test_signup(self):
        print("signup executing")

    def test_logout(self):
        print("logout executing")