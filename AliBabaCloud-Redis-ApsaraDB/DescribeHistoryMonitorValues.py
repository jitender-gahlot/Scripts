#!/usr/bin/env python
#coding=utf-8

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkr_kvstore.request.v20150101.DescribeHistoryMonitorValuesRequest import DescribeHistoryMonitorValuesRequest

# Create an AcsClient object.
client = AcsClient(
   "LTAI4G7UPfmEfNcidYdYUgkU", 
   "Y1BV6h0G1XiP872gc0tWDkwRt6dcXG",
   "ap-south-1"
);

request = DescribeHistoryMonitorValuesRequest()
request.set_accept_format('json')

request.set_StartTime("2020-04-01T00:00:00Z")
request.set_EndTime("2020-04-02T16:00:00Z")
request.set_IntervalForHistory("01m")
request.set_InstanceId("r-6gjrc9vf30rgi6bb4a")

response = client.do_action_with_exception(request)
# python2:  print(response) 
print(str(response, encoding='utf-8'))