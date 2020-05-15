
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkr_kvstore.request.v20150101.DeleteAccountRequest import DeleteAccountRequest

client = AcsClient(
   "LTAI4G7UPfmEfNcidYdYUgkU", 
   "Y1BV6h0G1XiP872gc0tWDkwRt6dcXG",
   "ap-south-1"
);

request = DeleteAccountRequest()
request.set_accept_format('json')

request.set_AccountName("r-6gjrc9vf30rgi6bb4a")
request.set_InstanceId("r-6gjrc9vf30rgi6bb4a")

response = client.do_action_with_exception(request)
# python2:  print(response) 
print(str(response, encoding='utf-8'))