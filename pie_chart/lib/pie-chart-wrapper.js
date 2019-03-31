function PieChartViewer(divId, configs) {
    // configs: group, subgroup, value, title, chartName, selectedMode
    //          legendOrient, legendPosition, dataUrl, radius
    var chartInstance = document.getElementById(divId);

    setChartContainer();
    var pieChart = echarts.init(chartInstance);

    console.log("The configs for PieChartViewer: ", configs)

    function setChartContainer() {
        chartInstance.style.width = window.innerWidth != 0 ? window.innerWidth + 'px' : '100%';
        chartInstance.style.height = window.innerHeight != 0 ? window.innerHeight + 'px' : '500px';
    };

    function getItems(data) {
        var groups = _.flatMap(data, function(cls) {
            return cls[configs.group];
        });

        var subgroups = _.flatMap(data, function(cls) {
            return cls[configs.subgroup];
        });

        var items = _.sortedUniq(groups.concat(subgroups))
        console.log("All items fro PieChartViewer: ", items)
        return items
    }

    function getInnerData(data) {
        var output = _(data).groupBy(configs.group)
            .map((objs, key) => ({
                name: key,
                value: _.sumBy(objs, configs.value) 
        })).value();
        console.log("Inner data fro PieChartViewer: ", output)
        return output
    }

    function getOuterData(data) {
        var output = _.map(data, item => _.assign({
            name: item[configs.subgroup],
            value: item[configs.value]
        }));
        console.log("Outer data fro PieChartViewer: ", output)
        return output
    }

    function initPieChart(data, configs) {
        option = {
            title: {
                text: configs.title ? configs.title : ''
            },
            tooltip: {
                trigger: 'item',
                formatter: "{a} <br/>{b}: {c} ({d}%)"
            },
            legend: {
                orient: configs.legendOrient ? configs.legendOrient : 'horizontal',
                x: configs.legendPosition ? configs.legendPosition : 'right',
                data: getItems(data),
                top: '30px',
                left: 'center',
                type: 'scroll'
            },
            series: [
                {
                    name: configs.chartName,
                    type: 'pie',
                    selectedMode: configs.selectedMode ? configs.selectedMode : 'single',
                    radius: [0, configs.radius + '%'],
                    label: {
                        normal: {
                            position: 'inner'
                        }
                    },
                    labelLine: {
                        normal: {
                            show: false
                        }
                    },
                    data: getInnerData(data)
                }
            ]
        };
        
        if (configs.subgroup) {
            var simpleFormatter = {
                normal: {
                    formatter: "{b} : {c} ({d}%)"
                }
            }

            var richFormatter = {
                normal: {
                    formatter: '{a|{a}}{abg|}\n{hr|}\n  {b|{b}：}{c}  {per|{d}%}  ',
                    backgroundColor: '#eee',
                    borderColor: '#aaa',
                    borderWidth: 1,
                    borderRadius: 4,
                    // shadowBlur:3,
                    // shadowOffsetX: 2,
                    // shadowOffsetY: 2,
                    // shadowColor: '#999',
                    // padding: [0, 7],
                    rich: {
                        a: {
                            color: '#999',
                            lineHeight: 22,
                            align: 'center'
                        },
                        // abg: {
                        //     backgroundColor: '#333',
                        //     width: '100%',
                        //     align: 'right',
                        //     height: 22,
                        //     borderRadius: [4, 4, 0, 0]
                        // },
                        hr: {
                            borderColor: '#aaa',
                            width: '100%',
                            borderWidth: 0.5,
                            height: 0
                        },
                        b: {
                            fontSize: 16,
                            lineHeight: 33
                        },
                        per: {
                            color: '#eee',
                            backgroundColor: '#334455',
                            padding: [2, 4],
                            borderRadius: 2
                        }
                    }
                }
            }

            option.series.push({
                itemStyle : {
                    normal : {
                        label : {
                            show : configs.showItemBox
                        },
                        labelLine : {
                            show : configs.showItemBox
                        }
                    }
                },
                name: configs.chartName,
                type: 'pie',
                radius: [configs.radius + 10 + '%', configs.radius + 20 + '%'],
                label: configs.richFormatter ? richFormatter : simpleFormatter,
                data: getOuterData(data)
            })
        }

        if (configs.richFormatter) {

        }

        console.log('Echarts options: ', option)
        return(option)
    }

    Papa.parse(configs.dataUrl, {
        delimiter: "",
        download: true,
        header: true,
        comments: "#",
        skipEmptyLines: true,
        dynamicTyping: true,
        // when worker is true, Error: Can't load PapaParse with a script loader.
        // see https://github.com/mholt/PapaParse/issues/148 for more details.
        worker: false,
        complete: function(results) {
            var pieChartData = results.data
            console.log('The results from Papa parse: ', pieChartData)
            pieChart.setOption(initPieChart(pieChartData, configs));
            window.onresize = function () {
                setChartContainer();
                pieChart.resize();
            };
        }
    })
}
