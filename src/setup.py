from setuptools import setup

setup(name='ccssm',
    version='0.2',
    description='Candihub Chip Seq Snow Make',
    url='https://github.com/biorosetics/chipseq-snakemake',
    author='Charles Hebert',
    author_email='charles@biorosetics.com',
    license='MIT',
    packages=['ccssm'],
    include_package_data=True,
    zip_safe=False,
    entry_points = {
        'console_scripts': ['ccssm=ccssm.cli:main'],
    }
)