# Caesar Cipher Brute-Force Tool / 凯撒密码暴力破解工具

A simple Python tool that attempts to decrypt Caesar cipher messages by trying multiple shift keys.

一个简单的 Python 工具，通过尝试多个移位密钥来暴力破解凯撒密码。

---

## English Version

### Description

This program is a **Caesar cipher brute-force decoder**.  
It takes an encrypted message as input and tries every possible key from 0 to 6 (or more, depending on your version), printing the decrypted result for each key. You can then visually inspect which result looks like meaningful English text.

### Features

- Converts the input to uppercase automatically
- Tries multiple shift keys
- Preserves non-letter characters (spaces, punctuation, etc.)
- Simple and educational — good for learning how Caesar ciphers work

### How to Run

```bash
python caesar.py
```

Then type (or paste) the encrypted message and press Enter.

### Example

**Input:**
```
QIIX QI FC XLI VSWI FYWLIW XSRMKLX.
```

**Output (partial):**
```
Key #0: 
QIIX QI FC XLI VSWI FYWLIW XSRMKLX.
Key #1: 
PHHW PH EB WKH URVH EXVKHV WRQLJKW.
Key #2: 
OGGV OG DA VJG TQUG DWUJGU VQPKIJV.
Key #3: 
NFFU NF CZ UIF SPTF CVTIFT UPOJHIU.
Key #4: 
MEET ME BY THE ROSE BUSHES TONIGHT.
...
```

In this case, **Key #4** produces the correct plaintext.

### Notes

- The classic Caesar cipher has 26 possible keys (0–25).  
  The current version only tries a limited range for simplicity.
- Only English letters are shifted. Other characters are left unchanged.
- This is a **brute-force** approach — it tries every key rather than using frequency analysis.

### Requirements

- Python 3.x
- Only uses the standard library (`string` module)

---

## 中文版本

### 简介

这是一个**凯撒密码暴力破解工具**。  
程序会接收一段加密后的英文句子，然后依次尝试多个密钥（当前版本是 0～6），把每种密钥解密后的结果都打印出来。你只需要观察哪一行看起来像正常的英文，就能找到正确的密钥。

### 功能特点

- 自动把输入转成大写
- 尝试多个移位密钥
- 保留空格、标点等非字母字符
- 代码简单，适合学习凯撒密码原理

### 运行方法

```bash
python caesar.py
```

运行后输入（或粘贴）加密的句子，然后按回车即可。

### 运行示例

**输入：**
```
QIIX QI FC XLI VSWI FYWLIW XSRMKLX.
```

**输出（部分）：**
```
Key #0: 
QIIX QI FC XLI VSWI FYWLIW XSRMKLX.
Key #1: 
PHHW PH EB WKH URVH EXVKHV WRQLJKW.
Key #2: 
OGGV OG DA VJG TQUG DWUJGU VQPKIJV.
Key #3: 
NFFU NF CZ UIF SPTF CVTIFT UPOJHIU.
Key #4: 
MEET ME BY THE ROSE BUSHES TONIGHT.
...
```

可以看到 **Key #4** 解出了正确的明文。

### 注意事项

- 标准凯撒密码共有 26 种可能的密钥（0～25）。  
  当前版本为了简洁只尝试了有限范围。
- 程序只对英文字母进行移位，其他字符保持原样。
- 这是**暴力破解**方法，通过穷举所有密钥来找到正确答案，而不是使用频率分析。

### 运行环境

- Python 3.x
- 仅使用标准库（`string` 模块）

---

## Author / 作者

Written for learning purposes.  
用于学习目的。
