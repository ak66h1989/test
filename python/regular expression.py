import re
re.search('[\d][\D]', 'a') is None
re.search('^\d', '0a0') is None
re.search('[\D^\d]', 'abc') is None
re.search('\D|^0', '1203') is None
dealId = dealId['證券代號'].tolist()
[i if re.search('[\D^\d]', i) is None]
