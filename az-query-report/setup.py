from setuptools import setup

setup(
    name='azure-query-report',
    version='0.1',
    py_modules=['make_report'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        make_report=make_report:cli
    ''',
)