## `pie-chart-js[biovis-report-plugin]`
### Description
Interactive pie chart. It is based on echarts.

### Example Data
```
group,subgroup,value
Marketing Advertising,Email Marketing,310
Marketing Advertising,Affiliate Advertising,234
Marketing Advertising,Affiliate Advertising,135
Search Engine,Baidu,1048
Search Engine,Google,251
Search Engine,Bing,147
Search Engine,Others,102
```

### Usage

```
@pie-chart-js(dataUrl="example_data.csv", group="group", subgroup="subgroup",   
              value="value", title="title", radius=30, chartName="Chart Name",
              legendOrient="horizontal", legendPosition="right", selectedMode="single")
```

### Arguments

```text
dataUrl: [string] Your own file with CSV data by specifying the URL/Local Path to your file.
group: column name that is mapped to group column.
subgroup: column name that is mapped to subgroup column.
value: column name that is mapped to value column.
title: chart title.
radius: circle radius.
chartName: chart name.
legendOrient: "horizontal", "vertical"
legendPosition: "right", "left"
selectedMode: "single", "multiple"
```

### Value
An interactive pie chart.

### Author(s)
Jingcheng Yang(yjcyxky@163.com)

### Examples

```
# If you have a custom data, you need to reset these arguments at least.
@pie-chart-js(dataUrl='example_data.csv')

# If you want to enable user to upload file, you need to use enableLocal argument.
@pie-chart-js(dataUrl='example_data.csv', group="group", subgroup="subgroup",   
              value="value", title="title", radius=30, chartName="Chart Name",
              legendOrient="horizontal", legendPosition="right", selectedMode="single")
```