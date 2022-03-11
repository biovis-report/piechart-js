# -*- coding:utf-8 -*-
from __future__ import unicode_literals

import os
from biovis_media_extension.plugin import BasePlugin
from biovis_media_extension.utils import get_candidate_name


class PieChartJSPlugin(BasePlugin):
    """
    PieChartJSPlugin allows you to create pie chart which is a web reporting tool for data analysis and visualization.
    Plugin name: pie-chart-js.

    :Example:
    @pie-chart-js()
    """
    plugin_name = 'pie-chart-js'
    plugin_dir = os.path.dirname(os.path.abspath(__file__))
    is_server = False
    lib_dir = os.path.join(os.path.dirname(__file__), 'lib')

    def external_css(self):
        pass

    def external_javascript(self):
        echarts_js = os.path.join(self.lib_dir, 'echarts.min.js')
        return [{
            'echarts_js': echarts_js
        }]

    def check_plugin_args(self, **kwargs):
        pass

    def render(self, **kwargs):
        """
        Rendering and auto-generating js code.

        :param kwargs: plugin's keyword arguments.
        :return: rendered js code.
        """
        temp_div_id = 'pie-chart-' + get_candidate_name()

        csv_js = os.path.join(self.lib_dir, 'papaparse.min.js')
        lodash_js = os.path.join(self.lib_dir, 'lodash.js')
        pie_chart_wrapper = os.path.join(self.lib_dir, 'pie-chart-wrapper.js')
        js_lst = [
            {
                'csv_js': csv_js
            }, {
                'lodash_js': lodash_js
            }, {
                'pie_chart_wrapper': pie_chart_wrapper
            }
        ]

        # The arguments of function 'PieChartViewer' are position paraments, all paraments are defined in pie-chart-wrapper.js.
        # PieChartViewer(div_id, configs)
        configs = {
            "dataUrl": self.get_net_path('dataUrl'),
            "group": kwargs.get("group", "group"),
            "subgroup": kwargs.get("subgroup", "subgroup"),
            "value": kwargs.get("value", "value"),
            "title": kwargs.get("title", ""),
            "radius": kwargs.get("radius", 30),
            "chartName": kwargs.get("chartName", ""),
            "showItemBox": kwargs.get("showItemBox", True),
            "legendOrient": kwargs.get("legendOrient", "horizontal"),
            "legendPosition": kwargs.get("legendPosition", "right"),
            "selectedMode": kwargs.get("selectedMode", "single"),
            "richFormatter": kwargs.get("richFormatter", True)
        }
        codes = self.autogen_js(js_lst, 'PieChartViewer', configs=configs,
                                div_id=temp_div_id)

        return codes
