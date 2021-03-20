# -*- coding:utf-8 -*-
from setdown import Fixture


class TestFrame(Fixture):
    def test_frame(self):
        self.driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
        # frame 切换
        self.driver.switch_to.frame('iframeResult')
        print(self.driver.find_element_by_id('draggable').text)
        # 切回默认frame
        self.driver.switch_to.default_content()
        print(self.driver.find_element_by_id('submitBTN').text)
