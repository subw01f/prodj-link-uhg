import unittest
from prodj.network.packets import DBMessage

class DbclientTestCase(unittest.TestCase):
    def test_parsing_root_menu_rendering_request(self):
        raw_data = bytes([
            0x11, 0x87, 0x23, 0x49, 0xae, 0x11, 0x05, 0x80,
            0x00, 0x0f, 0x10, 0x30, 0x00, 0x0f, 0x06, 0x14,
            0x00, 0x00, 0x00, 0x0c, 0x06, 0x06, 0x06, 0x06,
            0x06, 0x06, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
            0x11, 0x02, 0x01, 0x04, 0x01,
            0x11, 0x00, 0x00, 0x00, 0x00,
            0x11, 0x00, 0x00, 0x00, 0x07,
            0x11, 0x00, 0x00, 0x00, 0x00,
            0x11, 0x00, 0x00, 0x00, 0x08,
            0x11, 0x00, 0x00, 0x00, 0x00,
        ])

        parsed = DBMessage.parse(raw_data)
