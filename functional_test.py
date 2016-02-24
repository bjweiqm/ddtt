#! /usr/bin/env python3
#encoding:utf-8

from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        
    def tearDown(self):
        self.driver.quit()
        
    def test_can_start_a_list_and_retrieve_it_later(self):
        #光头强说有一个很酷的在线待办事项应用
        #他去看了这个应用的首页
        self.driver.get("http://localhost:8000")

        #他注意到网页到标题都包含 “To-Do”这个词
        print(self.driver.title)
        self.assertIn("To-Do",self.driver.title)
        self.fail("finish the test !")

        #应用邀请他输入了一个待办事项

        #他在一个文本中输入了“Buy peacock feathers"(购买孔雀羽毛)
        #光头强到爱好是使用假蝇做饵钓鱼

        #他按回车后，页面更新了
        #待办事项表格中显示了”1. Buy peacock feathers“

        #页面又显示了一个文本框，可以输入其他的待办事项
        #他又输入了' Use peacock feathers to make a fly'(使用孔雀羽毛做假蝇)
        #光头强做事很有条理

        #页面再次更新，他的清单中显示了两条待办事项

        #光头强想知道这个网站是否能记住他的清单

        #他看到网站为他生成了一个唯一到url
        #而且页面中又一些文字解说这个功能

        #他访问那个url，发现她的待办事项列表还在

        #他很满意，去睡觉了。

if __name__ == "__main__":
    unittest.main(warnings = 'ignore')


