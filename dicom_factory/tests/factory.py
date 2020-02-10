import unittest

from dicom_factory.factory import DicomFactory


class TestFactory(unittest.TestCase):

    def test_create_factory_allows_access_to_pixel_array(self):
        dicom = DicomFactory.build()
        self.assertEqual((50, 50), dicom.pixel_array.shape)
