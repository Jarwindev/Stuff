import encrypt as e

tests = ["hello", "", "åäö", "This is a longer test! 12345"]
for t in tests:
    c = e.algo4(t)
    d = e.dealgo4(c)
    print('plain:', repr(t))
    print('cipher:', c)
    print('decrypted:', repr(d))
    print('ok:', d == t)
    print('---')
