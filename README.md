<p align="center">
  <img src="assets/banner.jpg" width="500" style="border-radius: 8px;">
</p>

<h1 align="center">TariffX AI Agent Skill for OpenClaw</h1>

<p align="center">
  <strong>Equip your OpenClaw agent with institutional-grade US Customs Intelligence.</strong>
</p>

---

[English Version] | [中文版](#-什么是-tariffx-skill)

## 🦞 What is TariffX Skill?
This open-source plugin empowers **[OpenClaw](https://github.com/datawhalechina/hello-claw)** and similar AI agents with profound, highly precise US Customs database computing capabilities.
By installing this skill, your agent will no longer blindly guess HS Codes due to a lack of domain expertise or outdated LLM training data.
Every duty calculation, Section 301 penalty check, UFLPA (Uyghur Forced Labor Prevention Act) screening, and AD/CVD case query is vetted by TariffX's cloud intelligence.

## 🌟 Features
1. 💡 **High Precision HTS Classification**: Accurate down to the full 10-digit US Customs tariff number.
2. 💰 **Comprehensive Duty Estimation**: Calculates Column 1 Base rates, Section 301 additional tariffs, and effective total rates.
3. 🚨 **Commercial Compliance Defense**: Automatically screens for high-risk red flags like UFLPA restrictions and AD/CVD (Anti-Dumping / Countervailing Duties) orders.

## 🔧 Installation & Configuration

### Step 1: Obtain Your TariffX API Credentials
This plugin is connected to the TariffX enterprise gateway. To enable commercial API access, register on the official website:
👉 [Get your API Key on TariffX.ai](https://tariffx.ai/dashboard/api-keys)  
*(Each successful cloud inference consumes 1 API Credit)*

### Step 2: The Magic Auto-Install Prompt (Recommended)
You don't need to manually configure the terminal! Just wake up your OpenClaw agent and send it this magic prompt (replace `YOUR_KEY` with your actual API key):

> "Hi OpenClaw, please install the official TariffX Intelligence Skill for yourself:
> 1. In your system terminal, go to your skills directory and run: `git clone https://github.com/tariffxai/openclaw-skill-tariffx.git tariffx_hts`
> 2. Configure this environment variable in your system: `export TARIFFX_API_KEY="tx-live-YOUR_KEY"`
> After you finish the installation, reply to me: 'Installation complete! I am ready to classify products.'"

### Step 3: Manual Installation (For Developers)
If you prefer to install it manually and manage your own environment variables:

```bash
cd path/to/your/openclaw/skills
git clone https://github.com/tariffxai/openclaw-skill-tariffx.git tariffx_hts
export TARIFFX_API_KEY="tx-live-xxxxxxxx"
```

---

## 🚀 See the Magic in Action

Wake up your OpenClaw agent and try commanding it in natural language:

> "I just imported a batch of 100% mulberry silk women's sweaters. Help me use TariffX to check the US import duty rate, and see if there are any UFLPA compliance risks I need to avoid."

OpenClaw will smoothly call the cloud database autonomously and report the perfectly summarized, highly accurate data back to you.

---
---

## 🦞 什么是 TariffX Skill？
该开源插件为 **[OpenClaw](https://github.com/datawhalechina/hello-claw)** 以及类似 AI Agents 赋能了极其深厚、精准的美国海关数据库计算能力。
通过安装该技能，你的龙虾无需再因为缺乏专业知识、或是被大模型老旧的训练集带偏而瞎猜海关编码 (HS Code)。
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

### 步骤 2：自动安装魔法咒语 (强烈推荐)
作为非技术用户，你完全不需要去折腾复杂的命令行。直接启动你的 OpenClaw 聊天框，复制以下魔法咒语发给它即可（别忘了把 `YOUR_KEY` 替换成你真实的 API 秘钥）：

> "你好，请为你自己安装官方的 TariffX 美国海关情报插件。
> 请在你的环境终端进入 skills 目录并运行 `git clone https://github.com/tariffxai/openclaw-skill-tariffx.git tariffx_hts`。
> 然后，将我的专属秘钥作为环境变量配置到系统中：`export TARIFFX_API_KEY="tx-live-YOUR_KEY"`。
> 完成全部下载和安装后，请回复我：系统已就绪，随时可以进行海关编码测算。"

### 步骤 3：极客手动安装 (开发者适用)
如果你偏好自己动手配置终端与系统环境变量：

```bash
cd path/to/your/openclaw/skills
git clone https://github.com/tariffxai/openclaw-skill-tariffx.git tariffx_hts
export TARIFFX_API_KEY="tx-live-xxxxxxxx"
```

---

## 🚀 见证奇迹时刻

重新唤醒并运行你的 OpenClaw Agent。试着用自然语言命令它：

> "我刚进口了一批 100% 桑蚕丝女装毛衣，帮我用 TariffX 查查关税是多少点？顺便看看有没有涉疆等合规性问题可以帮我避雷。"

OpenClaw 会顺滑地自主调用、访问云端数据库，并将完美总结且精准的数据，用自然语言汇报给你。

## 🛡️ License
MIT License.
