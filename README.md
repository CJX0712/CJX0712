<div align="center">

# 晨星 · Chen Xing

**前端工程师 × AI 系统构建者**

用 React 把界面做对，用 Python 把算法算对。

`深圳，中国` · `TypeScript` · `React` · `Python 3.13`

</div>

---

白天在企业协同平台重构前端组件；晚上从零手写反向传播、注意力机制和扩散模型。

判断"是否真的懂了"的标准很简单 —— **能不能自己实现一遍，并且留下一条可被独立验证的不变量**。

## forge — 从零手写的算法实验室

**40 个算法实验室**（38 个 forge + 2 个 lab），**零依赖 · 零构建 · 单文件 HTML**。浏览器打开即运行，Node 无头自检全绿。

不是调库 Demo。每个 forge 都留了一条能被交叉验证的硬标准：解析解对数值解、暴力枚举对贪心、KKT 互补松弛、Bellman 残差收敛……

| 领域 | 代表项目 | 验证的不变量 |
| --- | --- | --- |
| 深度学习 | [nn-forge](https://github.com/CJX0712/nn-forge) · [attn-forge](https://github.com/CJX0712/attn-forge) · [transformer-forge](https://github.com/CJX0712/transformer-forge) · [diffusion-forge](https://github.com/CJX0712/diffusion-forge) | 梯度检验 maxRelErr ≈ 1e-7 |
| 强化学习 | [az-forge](https://github.com/CJX0712/az-forge)（AlphaZero 自对弈）· [cartpole-forge](https://github.com/CJX0712/cartpole-forge)（PPO）· [rl-forge](https://github.com/CJX0712/rl-forge) | Bellman 残差 → 0 |
| 概率与推断 | [gmm-forge](https://github.com/CJX0712/gmm-forge) · [hmm-forge](https://github.com/CJX0712/hmm-forge) · [vi-forge](https://github.com/CJX0712/vi-forge) · [mcmc-forge](https://github.com/CJX0712/mcmc-forge) | 对数似然 / ELBO 单调不降 |
| 数值线代 | [pca-forge](https://github.com/CJX0712/pca-forge) · [nmf-forge](https://github.com/CJX0712/nmf-forge) · [ica-forge](https://github.com/CJX0712/ica-forge) · [gp-forge](https://github.com/CJX0712/gp-forge) | ‖Av − λv‖ ≈ 1e-15 |
| 经典算法 | [astar-forge](https://github.com/CJX0712/astar-forge) · [avl-forge](https://github.com/CJX0712/avl-forge) · [rs-forge](https://github.com/CJX0712/rs-forge) · [svm-forge](https://github.com/CJX0712/svm-forge) | 堆序不变量 · KKT 互补松弛 |

## 端到端 AI 系统

| 项目 | 是什么 |
| --- | --- |
| [glassbox](https://github.com/CJX0712/glassbox) | 可解释的离线 RAG 引擎 —— BM25 + dense + RRF + rerank，每个环节都可查证 |
| [loom](https://github.com/CJX0712/loom) | MCP 原生的本地智能体运行时 —— Ollama / MCP / crawl4ai 组装成真正会干活的 Agent |
| [aetheros](https://github.com/CJX0712/aetheros) | 默认拒答无出处断言的 Agent Runtime |
| [tekmor](https://github.com/CJX0712/tekmor) | 证据锚定的 RAG 知识库，配套单文件控制台 |
| [dialectica-ai](https://github.com/CJX0712/dialectica-ai) | 辩衡 —— 证据锚定、可证收敛的多智能体审议推理 |
| [evolver](https://github.com/CJX0712/evolver) | 智能体自进化层 —— 技能 / 踩坑蒸馏 + 对照组基准 |
| [aurora](https://github.com/CJX0712/aurora) | 纯本机 CPU 推理的自主智能体（llama.cpp + Qwen2.5 + RAG + ReAct） |
| [hyperion-ai](https://github.com/CJX0712/hyperion-ai) | 双引擎 AI 系统：Python 训练 / TS 零依赖推理 |
| [morningstar-ai-collab](https://github.com/CJX0712/morningstar-ai-collab) | 可自托管的 AI 原生团队协作平台，全栈 TypeScript |

## 单文件工具

[schema-dowser](https://github.com/CJX0712/schema-dowser) 从 CSV 里探出隐藏的函数依赖 ·
[diff-scope](https://github.com/CJX0712/diff-scope) Myers 差分的每一轮波前 ·
[wave-loom](https://github.com/CJX0712/wave-loom) 约束传播织机 ·
[mojibake-er](https://github.com/CJX0712/mojibake-er) 乱码反推 ·
[prompt-terrain](https://github.com/CJX0712/prompt-terrain) prompt 冗余断层扫描

## 技术栈

| | |
| --- | --- |
| 前端 | React · TypeScript · Vite · 手写单文件 HTML/CSS/JS |
| 后端 | Python 3.13 · FastAPI |
| AI | 从零手写的神经网络实现 · 混合检索（BM25 / dense / RRF / rerank）· llama.cpp · Ollama · MCP · ONNX / GGUF |

---

<div align="center">

**✦** 天黑前把活干完，天亮时把结果交出去。

</div>
