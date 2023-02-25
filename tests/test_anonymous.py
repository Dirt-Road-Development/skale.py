from src.pow.anonymous import AnonymousPow
from eth_typing.encoding import HexStr

def test_case_anonymous_1():
    pow = AnonymousPow("http://staging-v3.skalenodes.com/v1/staging-utter-unripe-menkar", None)
    res = pow.send("0xa9eC34461791162Cae8c312C4237C9ddd1D64336", HexStr("0c11dedd000000000000000000000000D99c39BB76D284D21FDEB1364Ae3F1d6F6874050"))
    print("RES: ", res)
    assert True is False