import unittest

from dicom_factory.factory import DicomFactory


class TestFactory(unittest.TestCase):

    def test_create_factory_allows_access_to_pixel_array(self):
        dicom = DicomFactory.build()
        self.assertEqual((50, 50), dicom.pixel_array.shape)

    def test_create_factory_with_custom_series_adds_series_description(self):
        expected_series = 'leg'
        factory_args = {'SeriesDescription': expected_series}

        dicom = DicomFactory.build(factory_args)

        self.assertEqual(expected_series, dicom.SeriesDescription)
