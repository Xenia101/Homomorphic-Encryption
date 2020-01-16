# Homomorphic Encryption

Homomorphic Encryption in python

<p align=center>
  <img src="https://github.com/Xenia101/Homomorphic-Encryption/blob/master/img/al.PNG?raw=true">
</p>

### Homomorphic Encryption란?
>Homomorphic encryption is a form of encryption that allows computation on ciphertexts, generating an encrypted result which, when decrypted, matches the result of the operations as if they had been performed on the plaintext.
[WIKIPEDIA](https://en.wikipedia.org/wiki/Homomorphic_encryption)

평문 m<sub>1</sub>, m<sub>2</sub>에 대한 암호문 c<sub>1</sub>, c<sub>2</sub>가 있을때, m<sub>1</sub>+m<sub>2</sub> 를 계산한다고 한다.
이때, 일반적인 방법으로는 암호문 c<sub>1</sub>과 c<sub>2</sub>를 복호화 하여 평문 m<sub>1</sub>,m<sub>2</sub>를 얻고 m<sub>1</sub>+m<sub>1</sub>을 계산한 다음 다시 암호화하여 m<sub>1</sub>+m<sub>2</sub>의 결과물을 얻을 수 있다. 하지만 Homomorphic Encryption의 경우 이러한 과정들을 비밀키 없이 계산을 수행할 수 있다. 즉, 복호화의 과정을 거치지않고 계산을 수행할 수 있다.

## EXAMPLE

1. 먼저 암호화를 위해 공개 키 쌍과 개인 키 쌍을 생성해야 한다

```python
public_key, private_key = paillier.generate_paillier_keypair()
```

2. 암호화를 원하는 평문을 넣고 암호화 수행

```python
secret_number_list = [3.141592653, 300, -4.6e-12]
encrypted_number_list = [public_key.encrypt(x) for x in secret_number_list]

# encrypted_number_list
[<phe.paillier.EncryptedNumber object at 0x000001BB6990AC88>, 
<phe.paillier.EncryptedNumber object at 0x000001BB6991D630>, 
<phe.paillier.EncryptedNumber object at 0x000001BB6991D7F0>]
```

3. 암호화된 상태에서 연산 수행 

```python
a = encrypted_number_list[0]-3  # 0.141592653
b = encrypted_number_list[1]+5  # 305
c = encrypted_number_list[2]*-2 # 9.2e-12
```

4. 복호화하여 결과 확인

```python
>>>private_key.decrypt(a)
0.141592653
>>>private_key.decrypt(b)
305
>>>private_key.decrypt(c)
9.2e-12
```

### References
[Python paillier](https://readthedocs.org/projects/python-paillier/downloads/pdf/1.4.0/)
