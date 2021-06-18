import unittest
import test_widget


def suite():
    suite = unittest.TestSuite()
    suite.addTest(test_widget.WidgetTestCase('test_widget_resize'))
    suite.addTest(test_widget.DefaultWidgetSizeTestCase('test_default_widget_size'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
