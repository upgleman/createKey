from AESCipher import *


def saveFile(filename, encrypt):
    with open(filename, 'w') as f:
        f.write(encrypt)


# 스크립트를 실행하려면 여백의 녹색 버튼을 누릅니다.
if __name__ == '__main__':
    # print_hi('PyCharm')
    user_id = "0000000300"
    aesKey = "4j8ksxNNXQc2ihsaJgqdih64XgchWBAi"
    pwSaltCode = "$2a$10$sbQ6Ww5/zzXewrA0mgUSA."

    aes = AESCipher(aesKey)
    encrypt = aes.encrypt(pwSaltCode)
    print("암호화:", encrypt)

    decrypt = aes.decrypt(encrypt)
    print("복호화:", decrypt)

    # 파일저장
    filename = user_id + ".txt"
    saveFile(filename,encrypt)
