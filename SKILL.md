---
name: TariffX HTS Classifier
description: The official TariffX compliance skill. 当用户询问产品海关编码(HS/HTS Code)、关税税率、301条款附加税、或者 UFLPA / ADCVD 等合规红线风险时，务必调用此技能求助美国海关数据大脑。
---

# TariffX Intelligence Skill

## 适用场景 (When to use this)
本插件为您提供了三个直接连通 TariffX.ai 官方后端数据的工具，请根据用户的提问意图选用对应指令：

### 1. 归类与初步合规摸查 (`query_tariffx.py`)
**意图：** 用户给出了一段产品描述，要求了解其对应的美国海关编码(HTS)，或者简单粗略查询大概的总关税，以及潜在的 UFLPA/ADCVD 合规红线预警。
**用法：** 
`python scripts/query_tariffx.py "<产品描述>"`
**解析原则：** 从返回的 JSON 中提取 HTS_CODE、Rationale、Duty_Breakdown 和 Compliance_Alerts，用专业严谨的语言告知用户，并强调如果有合规警报务必引起重视，附上 `tariffx_link`。

### 2. 精准税费与落地成本计算 (`calculate_duties.py`)
**意图：** 用户已经给出了具体的或推断出的 10 位 HTS Code，且明确提到了 FOB 货值（总金额等），需要算非常精准的一笔账（如缴纳多少美元的 MFN 基础税、301 附加关税、MPF 货物处理费等）。
**用法：**
`python scripts/calculate_duties.py "<10位_HTS_CODE>" <货值_USD> --desc "<可选:产品介绍>"` 
*示例:* `python scripts/calculate_duties.py "6204594040" 1500 --desc "丝绸女裙"`
**解析原则：** 从 JSON (`cost_breakdown`) 提取出各种税种（Base Duty, Section 301, MPF, HMF, Total Duty 等）的准确金额，给用户列一份极其清晰的账单（类似于收据形式）。向用户汇报 `total_effective_rate`（综合实际税率）。

### 3. 海关保单 (CBP Continuous Bond) 额度精算 (`calculate_bond.py`)
**意图：** 用户进出口有一定额度，咨询应该买多少钱的 Continuous Bond 才符合海关规定；或者询问触发反倾销 (AD/CVD) 后的 Bond 计算方式。
**用法：**
`python scripts/calculate_bond.py --past <过去12月交的进口税_USD> --future <预估未来交的进口税_USD>`
*(如果有反倾销/反补贴属性，请附加 `--adcvd` 参数; 如果涉及FDA/EPA等，附加 `--pga` 参数)*
*示例:* `python scripts/calculate_bond.py --future 50000 --adcvd`
**解析原则：** 回答必须强调这是根据 CBP (美国海关) 的 10% 规则及风险乘数进行的估算。提取出建议金额 (`calc_bond_required`)，以及 `calculation_details` 中的人工步骤解释，详细且通俗地向用户说明为什么要买这档金额的 Bond。

## 执行与异常处理
此 Skill 依赖于系统环境变量 `TARIFFX_API_KEY`。如果接口返回包含 `Payment Required` 或 `Unauthorized`，请直接将返回信息里提示给主人的 `action` 重述给用户，指示用户前往 [TariffX.ai](https://tariffx.ai) 操作。
