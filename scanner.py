# coding=utf-8
'''
@Author：XingSongYan
@CreateDate： Tue Jan 19 16:32:19 HKT 2016
@FileName：
@Description：个人练手写的网站后台扫描器
'''
import requests
from multiprocessing.dummy import Pool as ThreadPool
from optparse import OptionParser

TIMEOUT = 5


def _get_args():
    parser = OptionParser(usage="usage: %prog [options] args")
    parser.add_option("-u", "--url", help="Target URL", dest='url')
    parser.add_option("-n", "--number", help="Number of Thread,Default 5",
                      dest="num", type="int", default=5)
    parser.add_option("-t", "--timeout", help="Timeout,Default 5",
                      dest="timeout", type="int", default=5)
    opts, args = parser.parse_args()
    return opts


def _mult_getdata(alist, pro_num):
    '''开启多线程探测
       alist = [(url,dir),(url,dir)...]
    '''
    pool = ThreadPool(processes=pro_num)
    result = pool.map(_check, alist)
    pool.close()
    pool.join()
    return result


def _check(target_list):
    url, dirstr = target_list
    if dirstr.startswith('/'):
        dirstr = dirstr[1:]  # 字典中某些路径开头包括/，这里进行统一
    dirstr = dirstr.replace("\r\n", "")
    final_url = "%s/%s" % (url, dirstr)
    print final_url
    try:
        r = requests.head(final_url, timeout=TIMEOUT)
        if r.status_code not in [404, 500]:
            return final_url
    except Exception as e:
        print e
    return ''


def main():
    opts = _get_args()
    url = opts.url
    if url.startswith("http") is False:
        url = "http://%s" % url
    if url.endswith("/"):
        url = url[:-1]
    num = opts.num
    global TIMEOUT
    TIMEOUT = opts.timeout
    if url:
        f = open("all.txt").read()
        dirs = f.split("\r\n")
        tempdirs = []
        for r in dirs:
            r = r.strip()
            #r = r.replace("\\","/")
            tempdirs.append((url, r))
        result = _mult_getdata(tempdirs, num)
        print "find dirs:", [x for x in result if x]
    else:
        print "Missing a mandatory option -u,use -h for help."
        return 0


if __name__ == "__main__":
    main()
