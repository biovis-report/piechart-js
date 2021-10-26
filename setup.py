from setuptools import setup, find_packages
from pie_chart.version import get_version


setup(
    name='pie-chart-js',
    version=get_version(),
    description='An biovis plugin to draw an interactive pie chart.',
    long_description='The pie chart plugin will draw an interactive pie chart by using echarts library.',
    keywords='biovis-plugin, pie-chart, interactive',
    url='https://github.com/biovis-report/pie-chart-js',
    author='Jingcheng Yang',
    author_email='yjcyxky@163.com',
    license='MIT',
    python_requires='>=3.4',
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    packages=find_packages(),
    entry_points={
        'biovis.plugins': [
            'pie-chart-js = pie_chart.pie_chart:PieChartJSPlugin'
        ]
    }
)
