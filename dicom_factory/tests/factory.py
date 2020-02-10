import unittest

from dicom_factory.factory import DicomFactory


class TestFactory(unittest.TestCase):

    def test_create_factory_with_custom_data_size_works_properly(self):
        data_size = (100, 100)
        factory_args = {'Rows': data_size[0], 'Columns': data_size[1]}

        dicom = DicomFactory.build(factory_args)

        self.assertEqual(data_size, dicom.pixel_array.shape)

    def test_create_factory_with_custom_series_adds_series_description(self):
        expected_series = 'leg'
        factory_args = {'SeriesDescription': expected_series}

        dicom = DicomFactory.build(factory_args)

        self.assertEqual(expected_series, dicom.SeriesDescription)

    def test_create_factory_with_unsupported_arguments_raises_value_error(self):
        with self.assertRaises(ValueError):
            factory_args = {'FakeArg': 123}
            DicomFactory.build(factory_args)
