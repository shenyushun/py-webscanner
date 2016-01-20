# py-webscanner
练手写的网站后台扫描器，字典在御剑基础上新增了一些，共1097802条不重复数据。

# 依赖
pip install requests

# 使用
Usage: scanner.py [options] args

Options:

  -h, --help            show this help message and exit
  
  -u URL, --url=URL     Target URL
  
  -n NUM, --number=NUM  Number of Thread,Default 5
  
  -t TIMEOUT, --timeout=TIMEOUT
                        
                        Timeout,Default 5
