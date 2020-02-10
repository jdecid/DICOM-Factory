import datetime

import numpy as np
import pydicom


class DicomFactory:
    @staticmethod
    def build(kwargs: dict = None) -> pydicom.FileDataset:
        if kwargs is None:
            kwargs = {}

        file_meta = pydicom.Dataset()
        file_meta.MediaStorageSOPClassUID = '1.2.840.10008.5.1.4.1.1.2'
        file_meta.MediaStorageSOPInstanceUID = '1.2.3'
        file_meta.ImplementationClassUID = '1.2.3.4'

        ds = pydicom.FileDataset('', {}, file_meta=file_meta, preamble=b"\0" * 128)

        # Add the data elements
        ds.PatientName = 'Fake Name'
        ds.PatientID = '123456'

        # Set transfer syntax
        ds.is_little_endian = True
        ds.is_implicit_VR = True

        # Set creation time
        dt = datetime.datetime.now()
        ds.ContentDate = dt.strftime('%Y%m%d')
        ds.ContentTime = dt.strftime('%H%M%S.%f')

        # Set transfer syntax
        ds.file_meta.TransferSyntaxUID = pydicom.uid.ExplicitVRBigEndian

        ds.BitsAllocated = 8
        ds.Rows = 50
        ds.Columns = 50
        ds.PixelRepresentation = 0
        ds.SamplesPerPixel = 1
        ds.PhotometricInterpretation = 'MONOCHROME1'
        ds.SeriesDescription = kwargs.get('SeriesDescription', '')
        ds.ViewPosition = ''

        np.random.seed(kwargs.get('seed', np.random.randint(0, 2 ** 32 - 1)))
        ds.PixelData = np.random.randint(0, 256, size=(50, 50), dtype=np.uint8).reshape(-1)

        return ds
