import datetime as dt, unittest
from cashwindow import build
class ScreeningTests(unittest.TestCase):
    def test_evidence_not_revenue(self):
        result=build([{'title':'Prize','link':'https://example.org','snippet':'deadline 2026-11-15'},{'link':'https://example.org'},{'link':'javascript:alert(1)'}],dt.date(2026,10,29),'test')
        self.assertEqual(len(result['entries']),1)
        self.assertEqual(result['entries'][0]['cash_status'],'No cleared cash evidenced')
        self.assertIn('after experiment',result['entries'][0]['window_note'])
    def test_restrictions(self):
        result=build([{'link':'https://example.org','snippet':'registration fee, in-person, no AI'}],dt.date(2026,10,29),'test')
        self.assertEqual(len(result['entries'][0]['flags']),3)
if __name__=='__main__': unittest.main()
