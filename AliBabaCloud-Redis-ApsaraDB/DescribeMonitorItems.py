#!/usr/bin/env python
#coding=utf-8

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkr_kvstore.request.v20150101.DescribeMonitorItemsRequest import DescribeMonitorItemsRequest
from aliyunsdkr_kvstore.request.v20150101.DescribeHistoryMonitorValuesRequest import DescribeHistoryMonitorValuesRequest

# Create an AcsClient object.
client = AcsClient(
   "LTAI4G7UPfmEfNcidYdYUgkU", 
   "Y1BV6h0G1XiP872gc0tWDkwRt6dcXG",
   "ap-south-1"
);

#request = DescribeHistoryMonitorValuesRequest()
request = DescribeMonitorItemsRequest()
request.set_accept_format('json')


response = client.do_action_with_exception(request)
# python2:  print(response) 
print(str(response, encoding='utf-8'))
#pprint(response) 