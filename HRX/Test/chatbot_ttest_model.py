# from HRX.Test.chatbot_model import models
import sys,os
loader_path = '../../classifier/loader/'
sys.path.append(loader_path)
from loader import load_all
# model_dict=load_all()
import unittest
import HTMLTestRunner     # 导入HTMLTestRunner模块
import pandas as pd

class chatBotModel(unittest.TestCase):
    """Test chatbot_ttest_model.py"""

    @classmethod
    def setUpClass(self):
        print("This setUpClass() method only called once.")
        model = load_all()
        self.model_IfKnowDebtor = model['IfKnowDebtor']
        self.model_CutDebt = model['CutDebt']
        self.model_IDClassifier = model['IDClassifier']
        self.model_WillingToPay = model['WillingToPay']
        self.model_Installment = model['Installment']
        self.model_ConfirmLoan = model['ConfirmLoan']
        self.df=pd.read_excel('ConfirmLoan.xls')


    @classmethod
    def tearDownClass(self):
        print("This tearDownClass() method only called once too.")

    def test_IfKnowDebtor(self):
        df=self.df[self.df['classifier'] == 'IfKnowDebtor']
        data_ifkonwdebtor=zip(df['index'],df['label'],df['split_text'])
        for each in data_ifkonwdebtor:
            with self.subTest(index=each[0],):  # 注意这里subTest的用法
                self.assertEqual(each[1], self.model_IfKnowDebtor.classify(each[2])['label'],msg='debtor_answer:'+each[2])

    def test_CutDebt(self):
        # self.assertEqual(0,self.model_CutDebt.classify("可以没问题")['label'])
        df = self.df[self.df['classifier'] == 'CutDebt']
        data_CutDebt = zip(df['index'], df['label'], df['split_text'])
        for each in data_CutDebt:
            with self.subTest(index=each[0]):  # 注意这里subTest的用法
                self.assertEqual(each[1], self.model_CutDebt.classify(each[2])['label'],msg='debtor_answer:'+each[2])

    def test_IDClassifier(self):
        df = self.df[self.df['classifier'] == 'IDClassifier']
        data_IDClassifier = zip(df['index'], df['label'], df['split_text'])
        for each in data_IDClassifier:
            with self.subTest(index=each[0]):  # 注意这里subTest的用法
                self.assertEqual(each[1], self.model_IDClassifier.classify(each[2])['label'],msg='debtor_answer:'+each[2])
        # self.assertEqual(1, self.model_IDClassifier.classify("他是我哥哥")['label'])

    def test_WillingToPay(self):

        df = self.df[self.df['classifier'] == 'WillingToPay']
        data_WillingToPay = zip(df['index'], df['label'], df['split_text'])
        for each in data_WillingToPay:
            with self.subTest(index=each[0]):  # 注意这里subTest的用法
                self.assertEqual(each[1], self.model_WillingToPay.classify(each[2])['label'],msg='debtor_answer:'+each[2])
        # self.assertEqual(11, self.model_WillingToPay.classify("我真的还不起")['label'])

    def test_Installment(self):
        # self.assertEqual(0, self.model_Installment.classify("好呀，这样我就可以处理了")['label'])
        df = self.df[self.df['classifier'] == 'Installment']
        data_Installment = zip(df['index'], df['label'], df['split_text'])
        for each in data_Installment:
            with self.subTest(index=each[0]):  # 注意这里subTest的用法
                self.assertEqual(each[1], self.model_Installment.classify(each[2])['label'],msg='debtor_answer:'+each[2])

    def test_ConfirmLoan(self):
        # self.assertEqual(0, self.model_ConfirmLoan.classify("我不想还了")['label'],msg='confirmloan_msg')#如果这条错了，下面的子测试就不执行了
        df = self.df[self.df['classifier'] == 'ConfirmLoan']
        data_ConfirmLoan = zip(df['index'], df['label'], df['split_text'])
        for each in data_ConfirmLoan:
            # print(each[0],each[1],self.model_ConfirmLoan.classify(each[2])['label'],each[2])
            with self.subTest(index=each[0]):  # 注意这里subTest的用法
                self.assertEqual(each[1], self.model_ConfirmLoan.classify(each[2])['label'],msg='debtor_answer:'+each[2])

if __name__ == '__main__':
    unittest.main()

