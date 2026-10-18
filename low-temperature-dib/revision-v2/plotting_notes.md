# 图注与 Origin 作图说明

## 英文图注建议

Strict panel: Low-temperature cycling and discharge-to-charge-rate ratio for records with separately specified charge and discharge rates. The x axis is the demonstrated low-temperature cycle count and the y axis is the discharge rate divided by the charge rate for the same cycling test. Both axes are logarithmic. Red stars denote the user-supplied This work data, which have not been independently experimentally verified. Records with missing directional rates are omitted.

Conditional panel: Low-temperature cycling and discharge-to-charge-rate ratio. Red stars denote user-supplied This work data. Hollow blue circles show literature points under an equal-charge/discharge-current assumption; their directional rates were not independently reported. These assumed ratios must not be cited as directly measured or separately reported values. Labels identify the reference and temperature. No data point is displaced to avoid overlap; only its annotation is moved.

此图是循环圈数—充放电倍率比图，不是传统能量密度—功率密度 Ragone 图。倍率比必须来自同温度同一次循环试验，不能用某篇文献最高倍率除以循环倍率，也不能从容量保持率列产生倍率比。

## Origin 建议

1. 导入 Origin_all_records.csv（UTF-8），Cycles 设为 X，Ratio_strict 设为 Y，Point_ID/Ref_ID/Temperature_C 作为标签和分组。
2. 严格图只保留 Ratio_strict 非空且温度低于0°C的记录。两方向倍率未分别给出时保持空值。
3. 条件图可另外绘制 Ratio_assumed，并只接受 Symmetry_assumption=true 的记录；把这组符号设为白色填充、蓝色边框。This work 用红色星形，并注明 user supplied。
4. 横纵轴均选择 Log10，横轴 Low-temperature cycle count，纵轴 Low-temperature discharge / charge rate ratio。Y=1可加灰色虚线。
5. 标签建议 Ref_ID: Temperature_C °C。相同坐标的点不要随机抖动；应合并标签或用引线移动文字。循环数不同的记录不能横向移点。
6. 条件图必须保留脚注：Hollow literature points assume equal charge/discharge currents; not independently reported.
7. 按600dpi导出PNG，另外保存矢量PDF或SVG；本脚本SVG保留可编辑文字，PDF嵌入TrueType字体。

运行：python plot_figures.py（默认读同级交付文件_V2/Origin_all_records.csv并输出到该目录）。可用 --input 和 --output-dir 指定别处。脚本只读数据，不改写CSV。
