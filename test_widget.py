import unittest


class DefaultWidgetSizeTestCase(unittest.TestCase):
    def test_default_widget_size(self):
        self.assertEqual((50, 50), (50, 50))


class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.set_up = 'set up'

    def test_default_widget_size(self):
        self.assertEqual((50, 50), (50, 50),
                         'incorrect default size')

    def test_widget_resize(self):
        self.assertEqual((100, 150), (100, 150),
                         'wrong size after resize')


class WidgetTestCaseAnother(unittest.TestCase):
    def setUp(self):
        self.set_up = 'set up'

    def tearDown(self):
        self.tear_down = 'tear down'