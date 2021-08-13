import os
import unittest
from common import HTMLTestReportCN

case_path = os.path.dirname(__file__)+'/testcases'
discover = unittest.defaultTestLoader.discover(
    start_dir=case_path,
    pattern='test_*.py',
    top_level_dir=case_path
)
all_case_suite = unittest.TestSuite()
all_case_suite.addTest(discover)

report_path = os.path.dirname(__file__)+'reports/'
report_dir = HTMLTestReportCN.ReportDirectory(report_path)
report_dir.create_dir('柒芮斯后台自动化测试项目')
report_html_path = HTMLTestReportCN.GlobalMsg.get_value('report_path')
html_report_file = open(report_html_path,'wb')
test_runner = HTMLTestReportCN.HTMLTestRunner(
    stream=html_report_file,
    title='柒芮斯后台自动化测试项目',
    description='testV1.0',
    tester='ZhouGan'
)
test_runner.run(all_case_suite)