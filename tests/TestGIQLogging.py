import unittest

import GIQLogging
from logstash_formatter import LogstashFormatterV1


class TestGIQLogging(unittest.TestCase):
    def test_basic_init_is_debug_level(self):
        logger = GIQLogging.init(logstash_type='unittest', logger_name='test1')
        self.assertEqual(logger.level, GIQLogging.DEBUG)

    def test_basic_init_formatter_is_LogstashFormatterV1(self):
        logger = GIQLogging.init(logstash_type='unittest', logger_name='test2')
        self.assertIsInstance(logger.handlers[0].formatter, LogstashFormatterV1)

    def test_init_with_extra_fields(self):
        extra_fields = {'foo': 'bar', 'zip': 'zap'}
        logger = GIQLogging.init(logstash_type='unittest', extra_fields=extra_fields, logger_name='test3')
        for key in extra_fields.keys():
            self.assertIsNotNone(logger.handlers[0].formatter.defaults.get(key))


if __name__ == '__main__':
    unittest.main()
