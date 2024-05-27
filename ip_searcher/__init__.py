#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : AI.  @by PyCharm
# @File         : __init__.py
# @Time         : 2024/5/27 10:56
# @Author       : betterme
# @WeChat       : meutils
# @Software     : PyCharm
# @Description  : 

from meutils.pipe import *
from meutils.request_utils.crawler import Crawler

from ip2region.xdbSearcher import XdbSearcher as _XdbSearcher

searcher = _XdbSearcher(dbfile=get_resolve_path(__file__, 'data/ip2region.xdb'))


# is_open()

@lru_cache()
def search(ip: str, enhance: Optional[bool] = None):
    region = searcher.searchByIPStr(ip) or []
    searcher.close()
    if is_open('baidu.com:80') if enhance is None else enhance:
        region = enhance_search(ip) + region
    return region  # 可能出现多个候选


@lru_cache()
def enhance_search(ip: str):
    xpath = """//*[@id="tab0_address"]//text()"""
    region = Crawler(f"https://www.ip.cn/ip/{ip}.html").html.xpath(xpath)
    return region


if __name__ == '__main__':
    ip = "117.136.66.223"
    # xpath = """//*[@id="tab0_address"]//text()"""
    #
    # print(Crawler(f"https://www.ip.cn/ip/{ip}.html").html.xpath('/html/body/div[3]/div[2]//text()'))
    #
    # print(Crawler(f"https://www.ip.cn/ip/{ip}.html").html.xpath(xpath))

    print(search(ip))

    # print(is_open('baidu.com:80'))
