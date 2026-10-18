# V2 性能对比表（逐项复核稿）

12篇独立文献、17条温度/循环条件记录。169个原有字段逐项检查，10处字段更新。仍有NR/NV；当前未完成原始至少20篇要求。

[返回目录](README.md) · [Origin与图](revision-v2/README.md) · [下载最新Excel](battery-performance.xlsx?raw=true)

## 构型与条件

| Ref | 正极 \|\| 负极 | 电解液 | 电压 / V | 载量 / mg cm⁻² | 资料完整度 |
| --- | --- | --- | --- | --- | --- |
| [R01](https://doi.org/10.1016/j.cej.2024.152602) | Graphite \|\| Li<br>(dual-ion half-cell; coin) | 4.8 M LiFSI + 1 wt% LiPF6<br>FEA/DMC = 8:2 (v/v) | RT: 3.0–5.1<br>LT: 3.0–5.0 | ≈2.0 (reported electrode loading) | A：正文＋SI |
| [R02](https://doi.org/10.1021/jacs.4c12126) | PTPAn \|\| carbon-coated Al<br>(anode-free K-DIB; N/P=0) | 1 M KPF6 in DME/diglyme = 8:2 (v/v)<br>+ saturated KClO4 | 2.0–4.3 | 5–7 (PTPAn active mass) | B：摘要＋SI；正文未取得 |
| [R03](https://doi.org/10.1002/adma.202513832) | Graphite \|\| Li<br>(coin; separate RT pouch tests) | RT: LiTFSI/DMC/HFE = 1:1.64:1.23 (mol)<br>LT: DMC replaced by EMC (LHCE-EMC) | 3.0–5.1 | Coin: 2.0–3.0<br>RT pouch: 10 and 25 | A：正文＋SI |
| [R04](https://doi.org/10.1093/nsr/nwaf526) | PTT-4 \|\| Al<br>(Swagelok; RT pouch also reported) | AlCl3/[EMIm]Cl = 1.3:1 (mol) | RT: 0.1–2.2<br>LT cutoffs: NV | ≈1.0–1.5 (active material) | A：正文＋SI；DIB按机制判定 |
| [R05](https://doi.org/10.1038/s41467-026-74628-2) | Graphite \|\| PTCDI<br>(single-layer pouch) | EG-PAM-DG-TFSI-Cl hydrogel<br>40 vol% EG + 60 vol% aqueous stock<br>Stock: 1 M LiTFSI + 2 M ZnCl2 | −40°C: 0.6–3.0 V | Graphite: 1.0 (rate); 1.2 (cycling) | A：正文＋SI＋Source Data |
| [R06](https://doi.org/10.1039/d6sc05745d) | TPPAPZ \|\| Na (half-cell)<br>Separate RT pouch: TPPAPZ \|\| HC | 1 M NaPF6 in PC + 5% FEC<br>(% basis not stated) | ≈2.0–4.1 V vs. Na+/Na<br>(GCD curves; method text does not state exact cutoff) | ≈1 (electrode loading; active-mass basis NR) | A：正文＋SI |
| [R07](https://doi.org/10.1002/adfm.202201038) | Coated graphite \|\| 3D-framework Li | NV | NV | NV | C：仅摘要核实 |
| [R08](https://doi.org/10.1002/aenm.202203253) | PyPz cathode \|\| NV<br>(aluminum DIB) | NV | NV | NV | C：仅摘要核实 |
| [R09](https://doi.org/10.1002/adfm.202212287) | Graphite cathode \|\| NV | LiPF6 in methyl acetate/DEC<br>Concentration and ratio: NV | NV | NV | C：仅摘要核实 |
| [R10](https://doi.org/10.1002/adma.202307592) | PTPAn \|\| hydrogen titanate (HTO) | NV | NV | NV | C：仅摘要核实 |
| [R11](https://doi.org/10.1002/anie.202406765) | PTPAn \|\| Ti3C2 MXene | NV | NV | NV | C：仅摘要核实 |
| [R12](https://doi.org/10.1002/adma.73760) | P(PhTz) \|\| hard carbon<br>(K-DIB full-cell) | LT: 1 M KPF6 in DME; RT: NV | NV | NV | B：正文核实；SI未取得 |

## 室温性能

| Ref | 循环 | 倍率 | 软包 | 软包表现 |
| --- | --- | --- | --- | --- |
| R01 | 91.5% / 2000 / 5C | 94.8% / 30C<br>(baseline: 2C) | NR | NR |
| R02 | NR / 40 / 0.5C<br>(25°C; full cell; exact retention NR) | NV | NV | NV |
| R03 | 83% / 2000 / 5C | NR / 50C<br>87.11 mAh g⁻¹ | Yes (RT) | 10 mg cm⁻²: NR / 200 / 2C<br>“negligible capacity fading”<br>25 mg cm⁻²: NR / 150 shown / 1C |
| R04 | NR / 18000 / 10 A g⁻¹<br>99 mAh g⁻¹ at end | 56.4% [calc.] / 10 A g⁻¹<br>(baseline: 1 A g⁻¹) | Yes (RT) | 93% / 1500 / 1 and 2 A g⁻¹<br>Rate: 88.2% [calc.] at 2 vs 1 A g⁻¹ |
| R05 | NR | NR | Yes (cell format) | NR |
| R06 | 88% / 1000 / 0.2 A g⁻¹<br>(Na half-cell) | 80% / 10 A g⁻¹<br>(baseline: 0.3 A g⁻¹) | Yes (HC full-cell demo) | NR |
| R07 | NV | NV | NV | NV |
| R08 | NV | NV | NV | NV |
| R09 | NV | NV | NV | NV |
| R10 | NV | NV | NV | NV |
| R11 | NV | NV | NV | NV |
| R12 | 81% / 1300 / 1 A g−1 (5C)<br>78% / 150 / 0.1 A g−1 (0.5C) | 83% / 4 A g−1 (20C); baseline 0.1 A g−1 (0.5C) | NV | NV |

## 低温性能

| Ref | 温度 / °C | 循环 | 倍率 | 软包 | 软包表现 |
| --- | --- | --- | --- | --- | --- |
| R01 | −20 | NR / 100 / 0.5C<br>“almost no capacity decay” | NR | NR | NR |
| R02 | −40 | 80% / 183 / NV | NV | NV | NV |
| R03 | −20 | NR / 700 / 5C<br>(LHCE-EMC) | NR | NR | NR |
| R04 | −20 | ≈100% / 12000 / 1 A g⁻¹<br>(after activation) | 37.9% [calc.] / 5 A g⁻¹<br>(baseline: 0.05 A g⁻¹) | NR | NR |
| R04 | −20 | ≈87% / 3000 / 0.2 A g⁻¹ | 37.9% [calc.] / 5 A g⁻¹<br>(baseline: 0.05 A g⁻¹) | NR | NR |
| R05 | −40 | 47.8% [calc.] / 124 / 80 mA g⁻¹<br>(reference: cycle 1) | 23.4% [calc.] / 100 mA g⁻¹<br>(baseline: 60 mA g⁻¹) | Yes | 47.8% [calc.] / 124 / 80 mA g⁻¹<br>(same pouch test as J) |
| R06 | −30 | 107.2% (calc., 89/83) / 3000 / 0.5 A g⁻¹<br>Na half-cell; capacity activation; charge/discharge rates not separately listed | NR / 0.5 A g⁻¹<br>100 mAh g⁻¹ | NR | NR |
| R06 | −30 | 98.3% [calc., 113/115] / 1000 / 0.2 A g⁻¹<br>Na half-cell; caption conflict retained | NR / 0.5 A g⁻¹<br>100 mAh g⁻¹ | NR | NR |
| R06 | −12 | 91% / 500 / 0.5 A g⁻¹<br>Na half-cell | NR | NR | NR |
| R07 | −25 (operating range endpoint) | NV | NV | NV | NV |
| R08 | −30 | NV | NV | NV | NV |
| R09 | −20; −70 (operation) | NV | NV | NV | NV |
| R10 | −40 | 94.1% / 6000 / NV | NV | NV | NV |
| R10 | −60 | 91% / 1000 / NV | NV | NV | NV |
| R11 | −60 | 86.7% / 20000 / NV | NV | NV | NV |
| R12 | −40 | 87% / 850 / 0.1 A g−1 (0.5C) | NV | NV | NV |
| R12 | −40 | 67% / 1000 / 1 A g⁻¹ (5C) | NV | NV | NV |

## 限制和原文冲突

- **R01**：正文与SI Table S2的室温循环数值冲突：正文/Fig.4c为91.5%/2000/5C，SI表为94.1%/2000/2C。本表采用正文及主图并保留冲突记录。−30°C容量69.2 mAh g⁻¹@0.5C不等于循环保持率。
- **R02**：−40°C 80%/183 cycles来自原始摘要；对应倍率尚未核实。SI Fig.S20的0.5C是PTPAn半电池，不能移用到无负极全电池。
- **R03**：室温使用DMC型LHCE，−20°C使用EMC替代DMC的LHCE-EMC，不是同一电解液。13000次结果在10000次时更换Li，不作为连续寿命使用。
- **R04**：室温与低温循环有活化过程；−20°C约100%以活化后的稳定阶段为语境，不能等同首圈基准。文中Al||PTT-4已按模板改为正极||负极。
- **R05**：主图明确−40°C窗口0.6–3.0 V。Source Data至124圈，末值76.0/首圈158.9=47.8%；主图显示至120圈，97.2/158.9=61.2%。同次试验不同终点不作独立对比点；均不是统一80%失效寿命。所有相关测试为软包。
- **R06**：−30°C的3000圈保持率107.2%由图内印刷89/83计算；1000圈98.3%由113/115计算。1000圈采用正文与图内共同支持的0.2 A/g，保留图注0.5的冲突。低温数据为Na半电池，不是HC全电池/软包。
- **R07**：摘要将80%/2700与−25至40°C工作范围并述，未给2700次对应温度；电流单位在摘要元数据中异常为mA⁻¹。不能擅自填为−25°C循环数据。
- **R08**：−30°C运作由摘要确认；100000次及231 mAh g⁻¹未明确属于−30°C，未移入低温循环栏。
- **R09**：−20°C容量为室温的93.8%，这是LT/RT比值，不能写入倍率保持率。摘要85.35%/1000/5C温度未明确；−70°C仅确认可工作。首次在线元数据仅精确到2023-01。
- **R10**：−40与−60°C是同一篇论文的两组测试，只计1篇；倍率、电解液与载量待全文。
- **R11**：−60°C循环86.7%/20000由摘要确认，倍率未核实。英文anie与德文ange版本不重复计数。
- **R12**：新取得公开PMC完整正文。低温1 M KPF6/DME；−40°C两组独立循环为87%/850/0.5C和67%/1000/5C。共同GCD电流未分别拆分，不能把倍率比1当独立报告值。SI未取得，载量与精确截止电压仍NV。
