<div align="center">

# 晨星 · Chen Xing

**前端工程师 × AI 系统构建者**

用 React 把界面做对，用 Python 把算法算对。

`深圳，中国` · `TypeScript` · `React` · `Python 3.13`

`50 个单文件实验室` · `44 个端到端 AI 系统` · `零依赖 · 零构建`

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

<details>
<summary><b>展开全部 40 个实验室 →</b></summary>

**深度学习与生成**（8）

- [`nn-forge`](https://github.com/CJX0712/nn-forge) — MLP 反向传播，实时梯度可视化
- [`attn-forge`](https://github.com/CJX0712/attn-forge) — 手写缩放点积自注意力 + 因果掩码 + 多头 + 正弦位置编码
- [`transformer-forge`](https://github.com/CJX0712/transformer-forge) — mini-GPT 实验室，浏览器内训练
- [`transformer-forge-v2`](https://github.com/CJX0712/transformer-forge-v2) — decoder-only 因果 Transformer
- [`diffusion-forge`](https://github.com/CJX0712/diffusion-forge) — DDPM 前向闭式解 / 后验公式 / DDIM 采样
- [`ddpm-forge`](https://github.com/CJX0712/ddpm-forge) — DDPM v2，31+16 项不变量全绿
- [`denoise-forge`](https://github.com/CJX0712/denoise-forge) — U-Net + FiLM 时间条件的图像 DDPM
- [`word2vec-forge`](https://github.com/CJX0712/word2vec-forge) — skip-gram + 负采样，king-man+woman=queen 类比

**强化学习与决策**（4）

- [`az-forge`](https://github.com/CJX0712/az-forge) — AlphaZero 自对弈 + MCTS，浏览器内学会 Connect-4
- [`cartpole-forge`](https://github.com/CJX0712/cartpole-forge) — PPO：手写 CartPole 物理 + GAE + 裁剪代理目标
- [`rl-forge`](https://github.com/CJX0712/rl-forge) — Q-learning，与 Value Iteration 交叉验证
- [`gridworld-rl-lab`](https://github.com/CJX0712/gridworld-rl-lab) — 价值迭代 vs Q-learning 同屏对比

**概率模型与推断**（7）

- [`gmm-forge`](https://github.com/CJX0712/gmm-forge) — GMM + EM，责任度与权重守恒
- [`hmm-forge`](https://github.com/CJX0712/hmm-forge) — 前向-后向 / Viterbi / Baum-Welch
- [`vi-forge`](https://github.com/CJX0712/vi-forge) — 平均场 CAVI，ELBO 闭合形式
- [`mcmc-forge`](https://github.com/CJX0712/mcmc-forge) — Metropolis-Hastings / HMC / Ising Gibbs
- [`kalman-forge`](https://github.com/CJX0712/kalman-forge) — KF / 信息滤波 / RTS / 粒子滤波
- [`gp-forge`](https://github.com/CJX0712/gp-forge) — 高斯过程回归：Cholesky 推断 + 边际似然解析梯度
- [`ot-forge`](https://github.com/CJX0712/ot-forge) — 熵正则最优传输 / Sinkhorn

**数值线代与无监督**（4）

- [`pca-forge`](https://github.com/CJX0712/pca-forge) — 雅可比特征分解，幂迭代交叉验证
- [`nmf-forge`](https://github.com/CJX0712/nmf-forge) — Lee-Seung 乘法更新 + ALS
- [`ica-forge`](https://github.com/CJX0712/ica-forge) — FastICA：白化 + 定点迭代
- [`kmeans-forge`](https://github.com/CJX0712/kmeans-forge) — k-means++ / Lloyd，1D 精确 DP 对照

**经典算法与数据结构**（8）

- [`astar-forge`](https://github.com/CJX0712/astar-forge) — A*，堆序不变量 + BFS 交叉验证
- [`avl-forge`](https://github.com/CJX0712/avl-forge) — AVL，全不变量自校验
- [`tree-forge`](https://github.com/CJX0712/tree-forge) — 决策树 + 随机森林，根分裂增益暴力枚举对照
- [`sort-forge`](https://github.com/CJX0712/sort-forge) — 6 种排序逐帧可视化 + 比较/写入次数实测
- [`sudo-forge`](https://github.com/CJX0712/sudo-forge) — 数独生成/求解，唯一解保证
- [`rx-forge`](https://github.com/CJX0712/rx-forge) — 正则铁路图，Thompson NFA
- [`maze-forge`](https://github.com/CJX0712/maze-forge) — 迷宫生成与寻路可视化
- [`rs-forge`](https://github.com/CJX0712/rs-forge) — GF(256) Reed-Solomon 纠删码

**几何 · 物理 · 信号**（7）

- [`fourier-forge`](https://github.com/CJX0712/fourier-forge) — 傅里叶本轮路径绘制
- [`orbit-forge`](https://github.com/CJX0712/orbit-forge) — 2D n-body，速度 Verlet，动量严格守恒
- [`ray-forge`](https://github.com/CJX0712/ray-forge) — 光线追踪：相交几何与光照自检
- [`koch-forge`](https://github.com/CJX0712/koch-forge) — Koch 雪花分形
- [`ant-forge`](https://github.com/CJX0712/ant-forge) — Langton ant 元胞自动机
- [`life-forge`](https://github.com/CJX0712/life-forge) — 康威生命游戏 B3/S23
- [`synth-forge`](https://github.com/CJX0712/synth-forge) — WebAudio 合成器，采样数学自检

**机器学习基础**（2）

- [`svm-forge`](https://github.com/CJX0712/svm-forge) — SMO / KKT / 核技巧，2D 硬间隔最优性证书
- [`tinyml-lab`](https://github.com/CJX0712/tinyml-lab) — 带动量的 MLP，决策边界实时可视化

</details>

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

<details>
<summary><b>展开其余 35 个端到端系统 →</b></summary>

**本地优先 RAG 系统**（9）

- [`worldai`](https://github.com/CJX0712/worldai) — 本地优先、CPU 可跑、一键复现的 RAG + Agent 平台
- [`worldai-nexus`](https://github.com/CJX0712/worldai-nexus) — 模块化端到端 AI 系统实验（RAG + Agent）
- [`worldai-rag`](https://github.com/CJX0712/worldai-rag) — faiss + BM25 混合检索 / ONNX 重排 / GGUF 本地推理
- [`worldai-stack`](https://github.com/CJX0712/worldai-stack) — 端到端可运行 RAG + ReAct 智能体系统
- [`worldrag`](https://github.com/CJX0712/worldrag) — 本地优先的 RAG 知识库实验
- [`starlight-ai-stack`](https://github.com/CJX0712/starlight-ai-stack) — 摄取 / 混合检索 / 引用生成，模块可独立验证
- [`starlight-rag`](https://github.com/CJX0712/starlight-rag) — 本地优先的检索增强生成系统
- [`novamind`](https://github.com/CJX0712/novamind) — 协议优先、离线可验的端到端 RAG Agent
- [`novamind-rag`](https://github.com/CJX0712/novamind-rag) — 混合检索 + 引用生成的问答系统

**模块化 AI 系统与平台**（17）

- [`aether-ai-core`](https://github.com/CJX0712/aether-ai-core) — 模块化端到端 AI 系统框架（RAG + Agent），锁版一键复现
- [`aether-ai-core-v2`](https://github.com/CJX0712/aether-ai-core-v2) — Aether 智核 · 模块化 RAG + Agent 实验（CPU 可跑）
- [`atlas-ai-stack`](https://github.com/CJX0712/atlas-ai-stack) — 混合检索 + 守卫式跨域问答
- [`chenxing-ai-stack`](https://github.com/CJX0712/chenxing-ai-stack) — 企业级 RAG/Agent 平台 · 单一职责模块化架构
- [`helix-ai-engine`](https://github.com/CJX0712/helix-ai-engine) — provider-agnostic 的 AI 编排引擎（RAG + 工具型 Agent）
- [`lumen-ai`](https://github.com/CJX0712/lumen-ai) — 模块化 RAG + Agent + Tools，可插拔后端
- [`morningstar-ai`](https://github.com/CJX0712/morningstar-ai) — 晨星 AI · 模块化 RAG + Agent 系统原型
- [`nebula-ai-core`](https://github.com/CJX0712/nebula-ai-core) — 端到端可运行 AI 引擎
- [`nebula-ai-stack`](https://github.com/CJX0712/nebula-ai-stack) — 整合 Ollama / bge-m3 / bge-reranker / Qdrant 的开发环境
- [`nexus-ai-core`](https://github.com/CJX0712/nexus-ai-core) — 模块化 AI 能力中台：模型网关 / 检索 / 智能体 / 工作流 / 记忆
- [`nexus-ai-platform`](https://github.com/CJX0712/nexus-ai-platform) — NexusAI 平台：模型网关 / 知识检索 / 智能体
- [`novaai-stack`](https://github.com/CJX0712/novaai-stack) — 模块化端到端 AI 系统实验（RAG + Agent）
- [`quasar-ai-runtime`](https://github.com/CJX0712/quasar-ai-runtime) — 模块化端到端可运行的 AI 运行时
- [`starforge-ai`](https://github.com/CJX0712/starforge-ai) — FastAPI / FAISS / sentence-transformers / Ollama 组装的应用平台
- [`stellar-ai-core`](https://github.com/CJX0712/stellar-ai-core) — 可编排、接口驱动的端到端 AI 系统
- [`stellar-ai-stack`](https://github.com/CJX0712/stellar-ai-stack) — 协议化接口 + 混合检索 + 确定性 ReAct agent
- [`stellar-ai-workbench`](https://github.com/CJX0712/stellar-ai-workbench) — 模块化桌面 AI 工作台，干净环境可复现

**可自证 · 证据锚定**（4）

- [`aether-research`](https://github.com/CJX0712/aether-research) — 可审计的深度研究 Agent —— 逐字引用校验
- [`veritas-ai`](https://github.com/CJX0712/veritas-ai) — 不变量优先、可自进化的 Agent 运行时
- [`aletheia-cognition`](https://github.com/CJX0712/aletheia-cognition) — 推理时计算 Scaling 引擎（本地 RAG + inference-time compute）
- [`stellar-nexus`](https://github.com/CJX0712/stellar-nexus) — 断言级归因校验 + 自适应链路路由 + 评测门禁

**Agent 运行时**（1）

- [`aetherflow`](https://github.com/CJX0712/aetherflow) — 持久、可观测的通用 AI Agent 运行时（TypeScript）

**应用平台与服务**（3）

- [`ai-platform-agent-rag`](https://github.com/CJX0712/ai-platform-agent-rag) — Agent 编排 + RAG 知识库 + FastAPI 网关 + 单文件 WebUI
- [`ai-rag-platform`](https://github.com/CJX0712/ai-rag-platform) — FastAPI + Qdrant + Ollama + React 的 RAG 问答平台
- [`ai-llm-api`](https://github.com/CJX0712/ai-llm-api) — 本地 LLM 推理服务：FastAPI + llama.cpp 封装

**工程基建**（1）

- [`0.0`](https://github.com/CJX0712/0.0) — 最小仓库卫生门禁 · CI 冒烟验证模板

</details>

## 单文件工具

[schema-dowser](https://github.com/CJX0712/schema-dowser) 从 CSV 里探出隐藏的函数依赖 ·
[diff-scope](https://github.com/CJX0712/diff-scope) Myers 差分的每一轮波前 ·
[wave-loom](https://github.com/CJX0712/wave-loom) 约束传播织机 ·
[mojibake-er](https://github.com/CJX0712/mojibake-er) 乱码反推 ·
[prompt-terrain](https://github.com/CJX0712/prompt-terrain) prompt 冗余断层扫描 ·
[bitcrc](https://github.com/CJX0712/bitcrc) CRC-32/16 · Adler-32 · FNV-1a，对照公开标准向量 ·
[bitweave](https://github.com/CJX0712/bitweave) Huffman 最优前缀码 + 无损往返 ·
[ifs-atlas](https://github.com/CJX0712/ifs-atlas) 迭代函数系统混沌游戏分形浏览器 ·
[ai-dev-env-report](https://github.com/CJX0712/ai-dev-env-report) AI 开发环境体检报告单页 ·
[ai-library-dashboard](https://github.com/CJX0712/ai-library-dashboard) AI 资料库仪表盘单页

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
