<p align="center">
  <img src="https://tariffx.ai/logo.png" width="128">
</p>

<h1 align="center">TariffX AI Agent Skill for OpenClaw</h1>

<p align="center">
  <strong>Equip your OpenClaw agent with institutional-grade US Customs Intelligence.</strong>
</p>

## 🦞 什么是 TariffX Skill？
该开源插件为 **[OpenClaw](https://github.com/datawhalechina/hello-claw)** 以及类似 AI Agents 赋能了极其深厚、精准的美国海关数据库计算能力。
通过安装该技能，你的龙虾无需再因为缺乏专业知识、或是被 OpenAI 老旧的训练集带偏而瞎猜海关编码 (HS Code)。
每一条关税、301 惩罚、新疆棉 (UFLPA) 和反倾销反补贴查询，都经过 TariffX 云端超算级别的 AI 核准。

## 🌟 特色
1. 💡 **极精准 (High Precision)**的商品归类 (HTS Classification)，最高至美国 10 位海关编码。
2. 💰 **完整的税率估算体系**（包含 Column 1 Base, Section 301 Rates, 综合税率）。
3. 🚨 **商业合规底线防御**：强制自动检测有无涉疆 (UFLPA) 与倾销 (AD/CVD) 爆雷清单。

## 🔧 安装与配置指南

### 步骤 1：获取你的 TariffX API 凭证
此插件为 TariffX 企业级服务的一部分。为了启动商业调用网关，您需前往官网进行注册：
👉 [Get your free API Key on TariffX.ai](https://tariffx.ai/dashboard/api-keys)  
*(每次云端调用均消耗 1 枚 API Credit)*

### 步骤 2：下载并放入龙虾肚子
打开你装有 OpenClaw 引擎终端的工作目录，将本技能 Clone 下来：

```bash
cd path/to/your/openclaw/skills
git clone https://github.com/tariffxai/openclaw-skill-tariffx.git tariffx_hts
```

### 步骤 3：注入环境变量
确保你的龙虾在运行前，能从宿主机或 `.env` 配置文件中读取你刚申请到的那把锁钥：

```bash
# Linux / macOS (或直接写进系统 .bashrc / .zshrc)
export TARIFFX_API_KEY="tx-live-xxxxxxxx"
```

---

## 🚀 见证奇迹时刻

重新唤醒并运行你的 OpenClaw Agent。试着用自然语言命令它：

> "我刚进口了一批 100% 桑蚕丝女装毛衣，帮我用 TariffX 查查关税是多少点？顺便看看有没有涉疆等合规性问题可以帮我避雷。"

OpenClaw 会顺滑地自主调用、访问云端数据库，并将完美总结且精准的数据，用自然语言汇报给你。

## 🛡️ License
MIT License.
