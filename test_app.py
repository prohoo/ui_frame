# a = 1
# globals()["a"] = 2
# print(a)



# i = 0
#
#
# for a in [1, 2, 3, 4]:
#     # 改成atest后，就不会生成test本身而是atest，用例就少了本身的test，则不需要再test = None干掉
#     i = i + 1
#     globals()[f'bb_{i}'] = a
#     print(a)


# tt()
# list = {"name1":"a" ,"name2":"b"}
# i = 0
# for test in list:
#     i = i+1
#     # print(test)
#     globals()[f'test_{i}'] = test
#     print(test)
# print(test)

#
# list = [{"name":"a","name":"b"}]
# print(list[1]['name'])

# list = [{
# 	'name': 'Sheet1',
# 	'case_list': [{
# 		'name': '用例1',
# 		'steps': [(1, '切换到顶部框架', 'iframe_enter', '"/html/frameset/frame[1]"', None), (2, '点击贷款管理连接', 'click', '"贷款管理;;;LINK_TEXT"', None), (3, '退出框架', 'iframe_exit', "/html/body/div[2]/form/table[1]/tbody/tr[4]/td[2]/input'", 'beifan')]
# 	}, {
# 		'name': '用例2',
# 		'steps': [(1, '切换到顶部框架', 'iframe_enter', '"/html/frameset/frame[1]"', None), (2, '点击贷款管理连接', 'click', '"贷款管理;;;LINK_TEXT"', None), (3, '退出框架', 'iframe_exit', "/html/body/div[2]/form/table[1]/tbody/tr[4]/td[2]/input'", 'beifan')]
# 	}, {
# 		'name': '用例3',
# 		'steps': [(1, '切换到顶部框架', 'iframe_enter', '"/html/frameset/frame[1]"', None), (2, '点击贷款管理连接', 'click', '"贷款管理;;;LINK_TEXT"', None), (3, '退出框架', 'iframe_exit', "/html/body/div[2]/form/table[1]/tbody/tr[4]/td[2]/input'", 'beifan')]
# 	}, {
# 		'name': '用例4',
# 		'steps': [(1, '切换到顶部框架', 'iframe_enter', '"/html/frameset/frame[1]"', None), (2, '点击贷款管理连接', 'click', '"贷款管理;;;LINK_TEXT"', None), (3, '退出框架', 'iframe_exit', "/html/body/div[2]/form/table[1]/tbody/tr[4]/td[2]/input'", 'beifan')]
# 	}]
# }, {
# 	'name': 'Sheet2',
# 	'case_list': [{
# 		'name': '用例5',
# 		'steps': [(1, '切换到顶部框架', 'iframe_enter', '"/html/frameset/frame[1]"', None), (2, '点击贷款管理连接', 'click', '"贷款管理;;;LINK_TEXT"', None), (3, '退出框架', 'iframe_exit', "/html/body/div[2]/form/table[1]/tbody/tr[4]/td[2]/input'", 'beifan')]
# 	}, {
# 		'name': '用例6',
# 		'steps': [(1, '切换到顶部框架', 'iframe_enter', '"/html/frameset/frame[1]"', None), (2, '点击贷款管理连接', 'click', '"贷款管理;;;LINK_TEXT"', None), (3, '退出框架', 'iframe_exit', "/html/body/div[2]/form/table[1]/tbody/tr[4]/td[2]/input'", 'beifan')]
# 	}, {
# 		'name': '用例7',
# 		'steps': [(1, '切换到顶部框架', 'iframe_enter', '"/html/frameset/frame[1]"', None), (2, '点击贷款管理连接', 'click', '"贷款管理;;;LINK_TEXT"', None), (3, '退出框架', 'iframe_exit', "/html/body/div[2]/form/table[1]/tbody/tr[4]/td[2]/input'", 'beifan')]
# 	}, {
# 		'name': '用例4',
# 		'steps': [(1, '切换到顶部框架', 'iframe_enter', '"/html/frameset/frame[1]"', None), (2, '点击贷款管理连接', 'click', '"贷款管理;;;LINK_TEXT"', None), (3, '退出框架', 'iframe_exit', "/html/body/div[2]/form/table[1]/tbody/tr[4]/td[2]/input'", 'beifan')]
# 	}]
# }]
# print(*list[2]["case_list"])
