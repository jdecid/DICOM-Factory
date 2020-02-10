import setuptools

with open('README.md', mode='r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='dicom-factory',
    version='0.0.3',
    author='Josep de Cid',
    author_email='josep.de.cid@gmail.com',
    description='DICOM data generator for (mainly) testing purposes',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/jdecid/DICOM-Factory',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6'
)
