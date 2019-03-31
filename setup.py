from setuptools import setup, find_packages
from pie_chart.version import get_version


setup(
    name='pie-chart-js-plugin',
    version=get_version(),
    description='An choppy plugin to draw an interactive pie chart.',
    long_description='The pie chart plugin will draw an interactive pie chart by using echarts library.',
    keywords='choppy plugin pie-chart interactive',
    url='https://choppy.3steps.cn/go-choppy/pie-chart-plugin/',
    author='Jingcheng Yang',
    author_email='yjcyxky@163.com',
    license='MIT',
    python_requires='>=3.4',
    include_package_data=True,
    install_requires=[
        'mk-media-extension>=0.1.0'
    ],
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
        'choppy.plugins': [
            'pie-chart-js = pie_chart.pie_chart:PieChartJSPlugin'
        ]
    }
)
