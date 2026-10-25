<div align="center">

# ✦ 晨星 · Chen Xing

**从零造 AI，并造尺子证明它没骗你** · AI 系统构建者 · 验证优先 · 零重写集大成

[![Repos](https://img.shields.io/badge/Repos-309-blue)](https://github.com/CJX0712?tab=repositories)
[![License](https://img.shields.io/badge/License-MIT-green)](https://github.com/CJX0712/tianji-ai/blob/main/LICENSE)
[![Verification](https://img.shields.io/badge/Verification-invariants--first-brightgreen)](https://github.com/CJX0712/tianji-ai)
[![Python](https://img.shields.io/badge/Python-190-3776AB?logo=python)](https://github.com/CJX0712?tab=repositories&language=python)
[![HTML](https://img.shields.io/badge/HTML-73-E34F26?logo=html5)](https://github.com/CJX0712?tab=repositories&language=html)
[![JavaScript](https://img.shields.io/badge/JavaScript-39-F7DF1E?logo=javascript)](https://github.com/CJX0712?tab=repositories&language=javascript)
[![TypeScript](https://img.shields.io/badge/TypeScript-5-3178C6?logo=typescript)](https://github.com/CJX0712?tab=repositories&language=typescript)
[![Location](https://img.shields.io/badge/Shenzhen-China-red)](https://github.com/CJX0712)
[![Stars](https://img.shields.io/github/stars/CJX0712?label=Stars)](https://github.com/CJX0712?tab=repositories)
[![Followers](https://img.shields.io/github/followers/CJX0712?label=Followers)](https://github.com/CJX0712)
[![Stats](https://img.shields.io/badge/stats-auto--refreshed-blueviolet)](https://github.com/CJX0712/CJX0712/actions/workflows/profile-stats.yml)

*天黑前把活干完，天亮时把结果交出去。*

[![▶ 现场跑尺子](https://img.shields.io/badge/▶_现场跑一遍尺子-验伪演示台-27e0a4?style=for-the-badge)](https://cjx0712.github.io/apex-flagship/demo.html)
[![舰队门户](https://img.shields.io/badge/舰队门户-apex--flagship-5b9dff?style=for-the-badge)](https://cjx0712.github.io/apex-flagship/)

</div>

---

## 我在做什么

**从零造 AI，并造一把尺子证明它没骗你 —— 用世界顶级已有成果组装系统，并让「它真的对」这件事可以被独立验证。**

不重新发明轮子。检索已被工业界验证的最优解（RadixAttention、PagedAttention、FlashAttention、Gated DeltaNet、MLA、MoE、Muon2、GGUF k-quants……），正确地组合起来，再用**可复现基准 + 数学不变量**证明它真的能用。

### 三条硬原则

| 原则 | 含义 | 怎么才算做到 |
| --- | --- | --- |
| **零重写 · 集大成** | 任何需求先检索世界最优解，能复用就复用、能组合就组合、能超越就超越 | 每个项目注明复用了哪些顶级开源方案 |
| **验证优先** | 正确性不是「测试通过」，而是**架构层保证的硬不变量** | 解析解 vs 数值解、暴力枚举 vs 贪心、黄金参照库对拍、逐位确定性 |
| **闭环交付** | 可运行、可复现、可验证；失败如实报失败 | 门禁失败不允许放宽阈值凑绿 |

> **失败也公开**：[densforge](https://github.com/CJX0712/densforge) 是一份公开的失败记录 —— 密度估计中位 −1.05% FAIL、流形 5/5 FAIL vs Isomap。它没通过，我把它挂在 README 上而不是藏起来。

---

## ✦ APEX 舰队 · 从零造 AI，并造尺子证明它没骗你

一套开源的**「AI 验伪」方法与实物**：零依赖 JavaScript，从反向自动微分一路造到能对话的迷你 LLM，每一环都配**可独立复现的基准**——包括公开我自己的失败。

> 🖱️ **别信我，自己验**：[验伪演示台](https://cjx0712.github.io/apex-flagship/demo.html) —— 点一下，8 条数学不变量在你浏览器里实时跑（梯度检验 maxRelErr≈1e-10、LayerNorm 输出方差精确等于理论值…）。[舰队门户](https://cjx0712.github.io/apex-flagship/) 可导航全部仓库。

| 仓库 | 自检 | 它证明了什么 |
| --- | --- | --- |
| [apex-flagship](https://github.com/CJX0712/apex-flagship) | 门户 | 舰队总览与导航中枢 |
| [flagship-ai-engine](https://github.com/CJX0712/flagship-ai-engine) | 62/62 | 348 个 API 单文件内联 · 浏览器 / Node 双跑 |
| [flagship-transformer](https://github.com/CJX0712/flagship-transformer) | 9/9 | 反向自动微分 + RoPE + YaRN；外推崩塌被尺子照出，再靠长上下文预训练把原生外推推到 **0.75** |
| [flagship-rag-engine](https://github.com/CJX0712/flagship-rag-engine) | 9/9 | KV-Cache 增量解码与全量重算**逐位等价** + BM25 + 端到端 RAG |
| [flagship-llm-chat](https://github.com/CJX0712/flagship-llm-chat) | 15/15 | 能对话的迷你 LLM；BPE 子词分词把答案命中率 **76% → 100%**、token 省 41% |
| [flagship-monorepo](https://github.com/CJX0712/flagship-monorepo) | 32/32 | 四件实物一键聚合自检总装 |

> 诚实边界：玩具级规模（最大 d=64），量的是**工程正确性与方法可复现**，不是 SOTA 能力。
> 值钱的不是参数，是**每一步都能被独立验证**——以及失败没被藏起来。

---

## 📊 数据看板

<!-- STATS:START -->
> 由 GitHub Actions 自动刷新 · 最后更新 2026-10-25 20:59 UTC · 数字由 API 实拉，不靠手改

| 指标 | 数值 |
| --- | --- |
| 公开仓库 | **309**（活跃 261 · 归档 48） |
| Stars / Followers | **1** / **1** |
| 代码体量 | ≈ 34.4 MB（GitHub 计 35,176 KB） |
| 语言分布 | Python 190 · HTML 73 · JavaScript 39 · TypeScript 5 · 其他 2 |
| 活跃仓库 CI 覆盖 | **249/261**（95%） |
| Fork | 0 |

**最近推送**

- [starforge-ai-verifiable](https://github.com/CJX0712/starforge-ai-verifiable) — StarForge 星炉 · 零依赖纯 ESM JavaScript 世界顶级 AI 引擎 — 线性代数/自动微分/… （今天）
- [forge-llm](https://github.com/CJX0712/forge-llm) — FORGE · Verifiable AI Kernel — 零依赖纯 JS 的 LLM 训练·量化·推理内核，十层… （今天）
- [polaris-flagship-ai](https://github.com/CJX0712/polaris-flagship-ai) — 北极星 POLARIS - 晨星旗舰 AI 操作系统：llama.cpp 世界顶级引擎 x ifai 1024 微指… （今天）
- [ziwei-ai](https://github.com/CJX0712/ziwei-ai) — 紫微 ZIWEI · 可验证推理闭环：在天玑混合架构基座之上，实现 RLVR + GRPO(DAPO/Dr.GRPO… （今天）
- [ai-forge](https://github.com/CJX0712/ai-forge) — AI Forge / 星锻 — 零依赖、全自验证、可复现的 AI 系统（数值内核/自动微分/Muon·L-BFGS/… （今天）
- [nexus-flagship](https://github.com/CJX0712/nexus-flagship) — NEXUS · 晨星旗舰 AI 操作系统：十层架构 + 1024 微指令 ISA，零依赖纯 JS，202 门禁全绿。… （1 天前）
<!-- STATS:END -->

---

## 怎么验证我说的

别信 README，跑一遍。旗舰仓库三条命令出结果，无需 GPU、无需 API key：

```bash
git clone https://github.com/CJX0712/tianji-ai && cd tianji-ai
pip install -r requirements.lock.txt
make verify-all      # = make test + make gates + make quickstart
```

| 你会看到 | 判据 |
| --- | --- |
| 单元测试 | 39 个，全绿 |
| 交付门禁 | 10 道，全绿；任一项失败即 exit non-zero |
| 最小示例 | quickstart 端到端跑通 |
| 梯度校验 | 解析反向 vs 中心差分，相对误差 **6.21e-09** |
| 训练收敛 | 300 步 loss **−16.6%** |
| 复现性 | 同 seed 逐位一致 |

[![CI](https://github.com/CJX0712/tianji-ai/actions/workflows/ci.yml/badge.svg)](https://github.com/CJX0712/tianji-ai/actions/workflows/ci.yml) —— 每次 push 都在公开环境重跑一遍，绿色不是自述，是机器跑出来的。

其他仓库同理：`make verify-all` `make test` 或 `pytest`，多数项目零依赖、CPU 可跑。

---

## ✦ 旗舰：天玑 TIANJI —— 世界顶级混合架构语言模型全栈

**[tianji-ai](https://github.com/CJX0712/tianji-ai)** · Gated DeltaNet × MLA × MoE × Muon2 × 投机解码 · **仅依赖 NumPy** · CPU 可训

> 十层架构 · 1024 条可执行微指令 · 10 道可证门禁全绿 · 16 项验收指标达标

| 实测 | 结果 |
| --- | --- |
| 训练 300 步 | loss **−16.6%** |
| KV cache | 节省 **83.3%** |
| 解析反向 vs 中心差分 | 误差 **6.21e-09** |
| 同 seed 复现 | **逐位一致** |

**十层分解**：L0 数值内核 → L1 反向契约 → L2 BPE 分词 → L3 架构原语 → L4 Gated DeltaNet → L5 DeepSeek-V3 MoE → L6 Muon2 → L7 训练 → L8 推理量化 → L9 DPO/IPO/SimPO/KTO → L10 微指令 + 门禁

**姊妹系统**

- [aurora-worldclass-ai](https://github.com/CJX0712/aurora-worldclass-ai) —— MLA+GDN+SWA 混合注意力 / MTP 自投机 / MuonClip
- [tianshu-ai](https://github.com/CJX0712/tianshu-ai) —— 天枢 · 32 算法家族 + Caruana 集成选择 + 融合旗舰
- [chenxing](https://github.com/CJX0712/chenxing) —— LLM 推理栈：RadixAttention / PagedAttention / 投机解码 / FlashAttention / GGUF k-quants

---

## 端到端 AI 系统

| 项目 | 是什么 | 硬指标 |
| --- | --- | --- |
| [axiom-ai](https://github.com/CJX0712/axiom-ai) | 自验证 AI 微指令操作系统：十层 × 1024 微指令，单文件双端同源 | 64 项数学不变量 |
| [qiming-ai](https://github.com/CJX0712/qiming-ai) | 启明 · 可验证 RAG：混合检索 + Cross-Encoder 重排 + 句级支持度校验 + 覆盖率门槛拒答 | 76 测试 + 26 不变量 |
| [atlas-ai-stack](https://github.com/CJX0712/atlas-ai-stack) | ATLAS · 混合检索 + 重排 + 确定性工具路由 + ReAct + 逐句溯源 | 157 测试 |
| [glassbox](https://github.com/CJX0712/glassbox) | 玻璃盒 RAG：BM25 + dense + RRF + rerank，证据链全可见 | 纯 CPU 零 API key |
| [zhishu](https://github.com/CJX0712/zhishu) | 智枢 · 企业级知识中枢，Web / API / CLI 三形态 | Docker 一键复现 |
| [loom](https://github.com/CJX0712/loom) | MCP 原生本地智能体运行时：Ollama + MCP + crawl4ai | 本地优先 |
| [veritas-ai](https://github.com/CJX0712/veritas-ai) | 不变量优先、可自进化的 Agent 运行时 | 正确性提升到架构层 |
| [dialectica-ai](https://github.com/CJX0712/dialectica-ai) | 辩衡 · 证据锚定、可证收敛的多智能体审议 | 收敛可证 |
| [hyperion-ai](https://github.com/CJX0712/hyperion-ai) | 双引擎：Python 训练内核 + TypeScript 零依赖推理内核 | 13 模块 + 重排护栏 |
| [StellarAI](https://github.com/CJX0712/StellarAI) | 本地优先多模态引擎：transformers.js + hnswlib + ReAct | 零 API key |

---

## 零依赖 AI 内核矩阵

纯 JS / 纯 Python 内核家族 —— 每个模块以硬不变量自检，浏览器 / Node / Python 三端可跑。

| 内核 | 一句话 | 不变量 |
| --- | --- | --- |
| [zenith-ai](https://github.com/CJX0712/zenith-ai) | 15 模块零依赖纯 JS AI 核心库，浏览器 & Node 同码 | 24 项梯度校验 |
| [apex-forge](https://github.com/CJX0712/apex-forge) | 零依赖 AI/ML 基础库，每算法带可验证硬不变量 | 25/25 无头自检 |
| [microforge](https://github.com/CJX0712/microforge) | RMSNorm + RoPE + GQA + SwiGLU + FlashAttention-2 + Muon 微型 LLM 栈 | 11 条硬不变量 |
| [StarAI-Kernel](https://github.com/CJX0712/StarAI-Kernel) | 纯 JS 十层架构 AI 内核 | 23 项逐条可验证 |
| [ai-forge](https://github.com/CJX0712/ai-forge) | 星锻 · 数值内核 / 自动微分 / Muon·L-BFGS / FlashAttention·GQA·MLA | 逐条机器精度 |
| [phosphor-ai](https://github.com/CJX0712/phosphor-ai) | SVD / JacobiEig / PCA / GMM / kNN / MLP / Attention | 三重交叉验证 |
| [forge-core](https://github.com/CJX0712/forge-core) | autograd / SVD / Jacobi / k-means / GMM-EM / PCA / 注意力 | 8/8 绿 |
| [morningstar-ai-forge](https://github.com/CJX0712/morningstar-ai-forge) | 十层架构 + 跨库交叉验证（forge 纯实现 vs numpy/scipy/sklearn/torch） | 黄金参照对拍 |

---

## forge —— 从零手写的算法实验室

**69 个单文件实验室**，**零依赖 · 零构建 · 单文件 HTML/JS**。浏览器打开即运行，Node 无头自检全绿。

不是调库 Demo。每个 forge 都留了一条能被交叉验证的硬标准：解析解对数值解、暴力枚举对贪心、KKT 互补松弛、Bellman 残差收敛……

| 领域 | 代表项目 | 验证的不变量 |
| --- | --- | --- |
| 深度学习 | [nn-forge](https://github.com/CJX0712/nn-forge) · [attn-forge](https://github.com/CJX0712/attn-forge) · [transformer-forge](https://github.com/CJX0712/transformer-forge) · [gpt-forge](https://github.com/CJX0712/gpt-forge) | 梯度检验 maxRelErr ≈ 1e-7 |
| 生成模型 | [diffusion-forge](https://github.com/CJX0712/diffusion-forge) · [ddpm-forge](https://github.com/CJX0712/ddpm-forge) · [denoise-forge](https://github.com/CJX0712/denoise-forge) | DDPM 闭式解 / DDIM 一致性 |
| 强化学习 | [az-forge](https://github.com/CJX0712/az-forge)（AlphaZero 自对弈）· [cartpole-forge](https://github.com/CJX0712/cartpole-forge)（PPO+GAE）· [mcts-forge](https://github.com/CJX0712/mcts-forge) | Bellman 残差 → 0 / UCT vs Minimax |
| 概率与推断 | [gmm-forge](https://github.com/CJX0712/gmm-forge) · [hmm-forge](https://github.com/CJX0712/hmm-forge) · [vi-forge](https://github.com/CJX0712/vi-forge) · [mcmc-forge](https://github.com/CJX0712/mcmc-forge) · [kalman-forge](https://github.com/CJX0712/kalman-forge) | 对数似然 / ELBO 单调不降 |
| 数值线代 | [pca-forge](https://github.com/CJX0712/pca-forge) · [nmf-forge](https://github.com/CJX0712/nmf-forge) · [ica-forge](https://github.com/CJX0712/ica-forge) | ‖Av − λv‖ ≈ 1e-15 |
| 经典算法 | [astar-forge](https://github.com/CJX0712/astar-forge) · [avl-forge](https://github.com/CJX0712/avl-forge) · [rs-forge](https://github.com/CJX0712/rs-forge)（GF(256) Reed-Solomon）· [svm-forge](https://github.com/CJX0712/svm-forge) | 堆序不变量 · KKT 互补松弛 |
| 几何 · 物理 · 信号 | [fourier-forge](https://github.com/CJX0712/fourier-forge) · [orbit-forge](https://github.com/CJX0712/orbit-forge)（Verlet 动量守恒）· [wave-forge](https://github.com/CJX0712/wave-forge)（Crank-Nicolson 薛定谔）· [gravity-forge](https://github.com/CJX0712/gravity-forge)（Barnes-Hut N 体） | 守恒量 / 解析解对照 |
| 词向量 · 分词 | [word2vec-forge](https://github.com/CJX0712/word2vec-forge)（king−man+woman=queen）· [bpe-forge](https://github.com/CJX0712/bpe-forge) | 26 项不变量全绿 |

> ▶ **65 个项目已上线在线演示**（GitHub Pages，无需克隆）：`https://cjx0712.github.io/<仓库名>/`
> 随手可点：[nn-forge](https://cjx0712.github.io/nn-forge/) · [attn-forge](https://cjx0712.github.io/attn-forge/) · [diffusion-forge](https://cjx0712.github.io/diffusion-forge/) · [mcts-forge](https://cjx0712.github.io/mcts-forge/) · [gravity-forge](https://cjx0712.github.io/gravity-forge/) · [koch-forge](https://cjx0712.github.io/koch-forge/) · [fourier-forge](https://cjx0712.github.io/fourier-forge/) · [wave-forge](https://cjx0712.github.io/wave-forge/)

---

## Forge 系统 —— 可复现的机器学习算法库

**150+ 个模块化算法系统**（Python），复用顶级开源（scikit-learn / LightGBM / XGBoost / Optuna / FAISS / ruptures / river……），每套带纯 numpy 离线兜底与基线对照，CPU 可跑、确定性可复现。

| 领域 | 代表项目 |
| --- | --- |
| 表格 · AutoML | [tabulaforge](https://github.com/CJX0712/tabulaforge) · [rankforge](https://github.com/CJX0712/rankforge) · [featforge](https://github.com/CJX0712/featforge) · [semiforge](https://github.com/CJX0712/semiforge)（macro-F1 +0.0536）· [StarAI](https://github.com/CJX0712/StarAI) |
| 图与网络 | [graphforge](https://github.com/CJX0712/graphforge) · [gnnforge](https://github.com/CJX0712/gnnforge) · [kgforge](https://github.com/CJX0712/kgforge)（Filtered MRR +17.56%）· [heteroforge](https://github.com/CJX0712/heteroforge) |
| 因果 · 不确定性 | [causalforge](https://github.com/CJX0712/causalforge) · [dagforge](https://github.com/CJX0712/dagforge) · [confforge](https://github.com/CJX0712/confforge) · [certiscale](https://github.com/CJX0712/certiscale)（FDR 降 21–43×）· [pgmforge](https://github.com/CJX0712/pgmforge)（误差 6.9e-15） |
| 时序 · 检索 | [tsforge](https://github.com/CJX0712/tsforge) · [changeforge](https://github.com/CJX0712/changeforge) · [searchforge](https://github.com/CJX0712/searchforge)（nDCG@10 +11.73%）· [vecforge](https://github.com/CJX0712/vecforge) · [riverforge](https://github.com/CJX0712/riverforge) |
| 生成模型 | [diffusionforge](https://github.com/CJX0712/diffusionforge) · [rectforge](https://github.com/CJX0712/rectforge) · [flowforge](https://github.com/CJX0712/flowforge) · [ssmforge](https://github.com/CJX0712/ssmforge)（adding problem 1e-11） |
| 优化 · 决策 | [convexforge](https://github.com/CJX0712/convexforge) · [transforge](https://github.com/CJX0712/transforge)（155 测试）· [nashforge](https://github.com/CJX0712/nashforge) · [ctrlforge](https://github.com/CJX0712/ctrlforge) · [portforge](https://github.com/CJX0712/portforge) |
| 科学计算 | [operatorforge](https://github.com/CJX0712/operatorforge)（FNO/DeepONet）· [odeforge](https://github.com/CJX0712/odeforge) · [sindyforge](https://github.com/CJX0712/sindyforge) · [tensorforge](https://github.com/CJX0712/tensorforge) · [topoforge](https://github.com/CJX0712/topoforge) |
| 可信 · 隐私 | [robustforge](https://github.com/CJX0712/robustforge) · [privforge](https://github.com/CJX0712/privforge)（DP-SGD）· [fairforge](https://github.com/CJX0712/fairforge) · [watermarkforge](https://github.com/CJX0712/watermarkforge) · [explainforge](https://github.com/CJX0712/explainforge) |

---

## 技术栈

| | |
| --- | --- |
| 语言 | Python 3.13 · JavaScript (ESM) · TypeScript · 单文件 HTML/CSS/JS |
| 前端 | React · Vite · 手写零依赖单文件页面 |
| 后端 | FastAPI · Docker · Protocol 可注入模块化架构 |
| 数值 | NumPy / SciPy 纯 CPU 内核 · 可选 torch / JAX 后端 |
| AI | 混合架构 LLM（GDN+MLA+MoE）· 混合检索（BM25/dense/RRF/rerank）· llama.cpp · Ollama · MCP · ONNX / GGUF |
| 质量 | pytest · ruff · 数学不变量自检 · 逐位确定性复现 · 门禁不允许放宽阈值 |

---

## 📇 全部 309 个仓库

按语言分组的完整清单见 **[REPOSITORY_INDEX.md](./REPOSITORY_INDEX.md)**（零遗漏；归档项目保留但不推荐 —— 它们是历史迭代的诚实痕迹）。

语言分布与逐仓状态见上方[数据看板](#-数据看板)，由 Actions 自动刷新，不会过期。

---

## 许可与署名

- 全部开源项目统一 **MIT License**
- 作者：**晨星 · Chen Xing**（GitHub [@CJX0712](https://github.com/CJX0712)）· 深圳，中国
- 主力项目：[tianji-ai](https://github.com/CJX0712/tianji-ai)

<div align="center">

**✦** 不是太阳，不负责把什么都照亮 —— 是天亮前最后还亮着的那颗。

</div>
