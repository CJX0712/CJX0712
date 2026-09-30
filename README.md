<div align="center">

# 晨星 · Chen Xing

**前端工程师 × AI 系统构建者**

用 React 把界面做对，用 Python 把算法算对。

`深圳，中国` · `TypeScript` · `React` · `Python 3.13`

`48 个单文件实验室` · `43 个可复现 ML 系统` · `52 个端到端 AI 系统` · `12 个单文件工具` · `零依赖 · 零构建`

</div>

---

白天在企业协同平台重构前端组件；晚上从零手写反向传播、注意力机制和扩散模型。

判断"是否真的懂了"的标准很简单 —— **能不能自己实现一遍，并且留下一条可被独立验证的不变量**。

## forge — 从零手写的算法实验室

**48 个算法实验室**（45 个 forge + 3 个 lab），**零依赖 · 零构建 · 单文件 HTML**。浏览器打开即运行，Node 无头自检全绿。

不是调库 Demo。每个 forge 都留了一条能被交叉验证的硬标准：解析解对数值解、暴力枚举对贪心、KKT 互补松弛、Bellman 残差收敛……

| 领域 | 代表项目 | 验证的不变量 |
| --- | --- | --- |
| 深度学习 | [nn-forge](https://github.com/CJX0712/nn-forge) · [attn-forge](https://github.com/CJX0712/attn-forge) · [transformer-forge](https://github.com/CJX0712/transformer-forge) · [diffusion-forge](https://github.com/CJX0712/diffusion-forge) | 梯度检验 maxRelErr ≈ 1e-7 |
| 强化学习 | [az-forge](https://github.com/CJX0712/az-forge)（AlphaZero 自对弈）· [cartpole-forge](https://github.com/CJX0712/cartpole-forge)（PPO）· [rl-forge](https://github.com/CJX0712/rl-forge) · [mcts-forge](https://github.com/CJX0712/mcts-forge)（MCTS/UCT） | Bellman 残差 → 0 |
| 概率与推断 | [gmm-forge](https://github.com/CJX0712/gmm-forge) · [hmm-forge](https://github.com/CJX0712/hmm-forge) · [vi-forge](https://github.com/CJX0712/vi-forge) · [mcmc-forge](https://github.com/CJX0712/mcmc-forge) | 对数似然 / ELBO 单调不降 |
| 数值线代 | [pca-forge](https://github.com/CJX0712/pca-forge) · [nmf-forge](https://github.com/CJX0712/nmf-forge) · [ica-forge](https://github.com/CJX0712/ica-forge) · [gp-forge](https://github.com/CJX0712/gp-forge) | ‖Av − λv‖ ≈ 1e-15 |
| 经典算法 | [astar-forge](https://github.com/CJX0712/astar-forge) · [avl-forge](https://github.com/CJX0712/avl-forge) · [rs-forge](https://github.com/CJX0712/rs-forge) · [svm-forge](https://github.com/CJX0712/svm-forge) | 堆序不变量 · KKT 互补松弛 |

<details>
<summary><b>展开全部 48 个实验室 →</b></summary>

**深度学习与生成**（9）
- [`nn-forge`](https://github.com/CJX0712/nn-forge) — MLP 反向传播，实时梯度可视化
- [`attn-forge`](https://github.com/CJX0712/attn-forge) — 手写缩放点积自注意力 + 因果掩码 + 多头 + 正弦位置编码
- [`transformer-forge`](https://github.com/CJX0712/transformer-forge) — mini-GPT 实验室，浏览器内训练
- [`transformer-forge-v2`](https://github.com/CJX0712/transformer-forge-v2) — decoder-only 因果 Transformer
- [`diffusion-forge`](https://github.com/CJX0712/diffusion-forge) — DDPM 前向闭式解 / 后验公式 / DDIM 采样
- [`ddpm-forge`](https://github.com/CJX0712/ddpm-forge) — DDPM v2，31+16 项不变量全绿
- [`denoise-forge`](https://github.com/CJX0712/denoise-forge) — U-Net + FiLM 时间条件的图像 DDPM
- [`word2vec-forge`](https://github.com/CJX0712/word2vec-forge) — skip-gram + 负采样，king-man+woman=queen 类比
- [`bpe-forge`](https://github.com/CJX0712/bpe-forge) — 字符级 BPE 分词器实验室：从零训练 / 可视化 / 数学不变量验证

**强化学习与决策**（5）

- [`az-forge`](https://github.com/CJX0712/az-forge) — AlphaZero 自对弈 + MCTS，浏览器内学会 Connect-4
- [`cartpole-forge`](https://github.com/CJX0712/cartpole-forge) — PPO：手写 CartPole 物理 + GAE + 裁剪代理目标
- [`rl-forge`](https://github.com/CJX0712/rl-forge) — Q-learning，与 Value Iteration 交叉验证
- [`gridworld-rl-lab`](https://github.com/CJX0712/gridworld-rl-lab) — 价值迭代 vs Q-learning 同屏对比
- [`mcts-forge`](https://github.com/CJX0712/mcts-forge) — 蒙特卡洛树搜索 UCT 实验台，与 Minimax 交叉验证，10/10 无头自检全绿

**概率模型与推断**（7）

- [`gmm-forge`](https://github.com/CJX0712/gmm-forge) — GMM + EM，责任度与权重守恒
- [`hmm-forge`](https://github.com/CJX0712/hmm-forge) — 前向-后向 / Viterbi / Baum-Welch
- [`vi-forge`](https://github.com/CJX0712/vi-forge) — 平均场 CAVI，ELBO 闭合形式
- [`mcmc-forge`](https://github.com/CJX0712/mcmc-forge) — Metropolis-Hastings / HMC / Ising Gibbs
- [`kalman-forge`](https://github.com/CJX0712/kalman-forge) — KF / 信息滤波 / RTS / 粒子滤波
- [`gp-forge`](https://github.com/CJX0712/gp-forge) — 高斯过程回归：Cholesky 推断 + 边际似然解析梯度
- [`ot-forge`](https://github.com/CJX0712/ot-forge) — 熵正则最优传输 / Sinkhorn

**数值线代与无监督**（5）
- [`pca-forge`](https://github.com/CJX0712/pca-forge) — 雅可比特征分解，幂迭代交叉验证
- [`nmf-forge`](https://github.com/CJX0712/nmf-forge) — Lee-Seung 乘法更新 + ALS
- [`ica-forge`](https://github.com/CJX0712/ica-forge) — FastICA：白化 + 定点迭代
- [`kmeans-forge`](https://github.com/CJX0712/kmeans-forge) — k-means++ / Lloyd，1D 精确 DP 对照
- [`spectral-forge`](https://github.com/CJX0712/spectral-forge) — 谱聚类 Ng-Jordan-Weiss + Lanczos 三对角化

**经典算法与数据结构**（8）

- [`astar-forge`](https://github.com/CJX0712/astar-forge) — A*，堆序不变量 + BFS 交叉验证
- [`avl-forge`](https://github.com/CJX0712/avl-forge) — AVL，全不变量自校验
- [`tree-forge`](https://github.com/CJX0712/tree-forge) — 决策树 + 随机森林，根分裂增益暴力枚举对照
- [`sort-forge`](https://github.com/CJX0712/sort-forge) — 6 种排序逐帧可视化 + 比较/写入次数实测
- [`sudo-forge`](https://github.com/CJX0712/sudo-forge) — 数独生成/求解，唯一解保证
- [`rx-forge`](https://github.com/CJX0712/rx-forge) — 正则铁路图，Thompson NFA
- [`maze-forge`](https://github.com/CJX0712/maze-forge) — 迷宫生成与寻路可视化
- [`rs-forge`](https://github.com/CJX0712/rs-forge) — GF(256) Reed-Solomon 纠删码

**几何 · 物理 · 信号**（11）

- [`fourier-forge`](https://github.com/CJX0712/fourier-forge) — 傅里叶本轮路径绘制
- [`orbit-forge`](https://github.com/CJX0712/orbit-forge) — 2D n-body，速度 Verlet，动量严格守恒
- [`ray-forge`](https://github.com/CJX0712/ray-forge) — 光线追踪：相交几何与光照自检
- [`ray-forge-v2`](https://github.com/CJX0712/ray-forge-v2) — Whitted 风格光线追踪：反射 / 折射 / Fresnel / 多重采样 AA
- [`koch-forge`](https://github.com/CJX0712/koch-forge) — Koch 雪花分形
- [`ant-forge`](https://github.com/CJX0712/ant-forge) — Langton ant 元胞自动机
- [`cellular-lab`](https://github.com/CJX0712/cellular-lab) — 元胞自动机：2D 生命游戏 + 1D 初等规则（Rule 0–255）
- [`life-forge`](https://github.com/CJX0712/life-forge) — 康威生命游戏 B3/S23
- [`synth-forge`](https://github.com/CJX0712/synth-forge) — WebAudio 合成器，采样数学自检
- [`gravity-forge`](https://github.com/CJX0712/gravity-forge) — Barnes-Hut 四叉树 N 体引力，三体8字轨道/星系对撞，Verlet 辛积分
- [`wave-forge`](https://github.com/CJX0712/wave-forge) — 一维含时薛定谔方程，手写 Crank-Nicolson，对照解析解

**机器学习基础**（3）
- [`svm-forge`](https://github.com/CJX0712/svm-forge) — SMO / KKT / 核技巧，2D 硬间隔最优性证书
- [`tinyml-lab`](https://github.com/CJX0712/tinyml-lab) — 带动量的 MLP，决策边界实时可视化
- [`forest-forge-v2`](https://github.com/CJX0712/forest-forge-v2) — Random Forest 集成树：CART + Bagging + OOB + 特征重要性

</details>

## Forge 系统 — 可复现的机器学习系统

**43 个模块化 ML 系统**（Python），复用顶级开源（scikit-learn / PyTorch Geometric / LightGBM / Optuna / FAISS……），每套都带纯 numpy 离线兜底与基线对照，CPU 可跑、可复现。

**表格 · 监督学习**（6）

- [`tabulaforge`](https://github.com/CJX0712/tabulaforge) — 自动化表格机器学习：XGBoost + LightGBM + Optuna，sklearn 兜底
- [`rankforge`](https://github.com/CJX0712/rankforge) — Learning to Rank：LightGBM lambdamart + XGBoost rank:ndcg + 纯 numpy RankNet
- [`cvforge`](https://github.com/CJX0712/cvforge) — 基于特征的图像分类：scikit-image / OpenCV 特征 + macro-F1 / NMI / ARI
- [`intentforge`](https://github.com/CJX0712/intentforge) — 置信校准级联路由（C3R）文本分类，CPU-only
- [`featforge`](https://github.com/CJX0712/featforge) — AutoML 特征工程：相关性引导合成 + mRMR/前向选择，聚合精度 +22.5%
- [`featureforge`](https://github.com/CJX0712/featureforge) — 特征工程 × 选择器融合（FEFFuse）：多管线合成 + 选择器共识

**图与表征学习**（6）

- [`graphforge`](https://github.com/CJX0712/graphforge) — GNN 节点分类：PyTorch Geometric（GCN/GAT）+ 纯 numpy 离线兜底
- [`nodeforge`](https://github.com/CJX0712/nodeforge) — 可复现 GNN 节点分类基准：验证集调优的多通道架构
- [`graphforge-linkpred`](https://github.com/CJX0712/graphforge-linkpred) — faithful node2vec 链接预测，纯 numpy 实现
- [`graphrepforge`](https://github.com/CJX0712/graphrepforge) — 图表征学习基准：节点分类 / 链接预测
- [`heteroforge`](https://github.com/CJX0712/heteroforge) — 同质感知自适应路由（HAAR）图表征学习
- [`clustforge`](https://github.com/CJX0712/clusterforge) — 聚类系统：共识集成 EAC 旗舰，纯 numpy 离线兜底，确定性可复现

**因果 · 概率 · 不确定性**（6）

- [`causalforge`](https://github.com/CJX0712/causalforge) — 因果推断：交叉拟合 DML（LightGBM/XGBoost）估计 ATE，含 OLS/PSM 基线
- [`dagforge`](https://github.com/CJX0712/dagforge) — 确定性因果发现：NOTEARS 旗舰 + PC + 离线兜底
- [`gaussforge`](https://github.com/CJX0712/gaussforge) — 高斯过程 + AutoKernel 核结构搜索（Optuna）
- [`oodforge`](https://github.com/CJX0712/oodforge) — 分布外检测与置信度校准：CGOR 门控路由 + 选择性预测弃权带
- [`survforge`](https://github.com/CJX0712/survforge) — 生存分析：Cox / spline-Cox / XGBoost AFT，C-index 加权评测
- [`chainforge`](https://github.com/CJX0712/chainforge) — 贝叶斯后验推断工具箱：NUTS / ADVI / Laplace + 旗舰 VarioNUTS（变分预条件 + 诊断门控 + 诚实回退）

**时序 · 推荐 · 检索**（9）

- [`chrono-forge`](https://github.com/CJX0712/chrono-forge) — 时间序列预测：statsmodels/pmdarima + 残差堆叠集成
- [`tsforge`](https://github.com/CJX0712/tsforge) — 时间序列预测：M4 指标 + 滚动原点基准，零下载可跑 demo
- [`changeforge`](https://github.com/CJX0712/changeforge) — 变化点检测（CPD）：ConStab-CPD 共识集成 + 纯 numpy 离线兜底
- [`recforge`](https://github.com/CJX0712/recforge) — 隐式反馈推荐基准框架
- [`recoforge`](https://github.com/CJX0712/recoforge) — 混合协同过滤：手写 WRMF-ALS + implicit SOTA 后端
- [`vecforge`](https://github.com/CJX0712/vecforge) — 文档向量检索与聚类：FAISS + scikit-learn 兜底
- [`visionforge`](https://github.com/CJX0712/visionforge) — CPU-only 以图搜图（CBIR）：AMDF 自适应多描述子
- [`voiceforge`](https://github.com/CJX0712/voiceforge) — 语音/音频 ML：librosa / whisper / speechbrain，纯 numpy 兜底，21 单测全绿
- [`riverforge`](https://github.com/CJX0712/riverforge) — 在线学习/概念漂移：旗舰 DriftForge 漂移感知集成，scikit-learn/river 复用

**决策 · 优化 · 进阶范式**（10）

- [`activeforge`](https://github.com/CJX0712/activeforge) — 主动学习：5 查询策略（不确定性/QBC-BALD/核心集等）× 5 数据集
- [`banditforge`](https://github.com/CJX0712/banditforge) — 上下文老虎机 + 离线策略评估 OPE：LinUCB / LinTS
- [`offlineforge`](https://github.com/CJX0712/offlineforge) — 离线强化学习 + OPE：BC / CQL-lite / FQE，六种估计器对照 DP 真值
- [`tabularofflineforge`](https://github.com/CJX0712/tabularofflineforge) — 表格 MDP 离线 RL：FQI / CFQI + FQE / WIS，精确真值为金标准
- [`fedforge`](https://github.com/CJX0712/fedforge) — 联邦学习：FedAvg / FedMedian / FedTrimmedMean，Dirichlet 非独立同分布
- [`neuroforge`](https://github.com/CJX0712/neuroforge) — 深度强化学习训练：Gymnasium + SB3 + Optuna，纯 numpy DQN 兜底
- [`optiforge`](https://github.com/CJX0712/optiforge) — 组合优化套件：TSP / 背包 / 指派，OR-Tools + 自研基线
- [`onlineforge`](https://github.com/CJX0712/onlineforge) — 流式/增量学习：river + scikit-learn + 纯 numpy 离线兜底
- [`synthmind-forge`](https://github.com/CJX0712/synthmind-forge) — RCG-NAS：递归批判引导的神经网络架构搜索
- [`mooforge`](https://github.com/CJX0712/mooforge) — 多目标 EMO 工具箱：旗舰 AHVA-MOEA 自适应进化多目标优化

**可解释 · 迁移 · 半监督**（5）

- [`explainforge`](https://github.com/CJX0712/explainforge) — 模型无关特征归因（XAI）：纯 numpy KernelSHAP / LIME
- [`domainforge`](https://github.com/CJX0712/domainforge) — 域适应：CORAL / TCA / JDA / KLIEP 纯 numpy + SAFuse 融合
- [`gacsforge`](https://github.com/CJX0712/gacsforge) — 半监督 GACS：图-树混合类平衡自训练，macro-F1 超最强基线 +0.0536（3 seeds）
- [`anomalyforge`](https://github.com/CJX0712/anomalyforge) — 模块化异常检测：PyOD + scikit-learn + numpy 兜底
- [`conformforge`](https://github.com/CJX0712/conformforge) — 全栈共形预测基准：11 方法 × 10 数据集 × 双后端(numpy/MAPIE)，CAFuse 旗舰，覆盖率硬保证

**全家桶**（1）

- [`forgestack`](https://github.com/CJX0712/forgestack) — 本地可运行 AI 系统：复用 forest / spectral / bpe 三引擎 + 向量检索，41 单测

---

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
<summary><b>展开其余 43 个端到端系统 →</b></summary>

**本地优先 RAG 系统**（9）

- [`worldai`](https://github.com/CJX0712/worldai) — 本地优先、CPU 可跑、一键复现的 RAG + Agent 平台
- [`worldai-nexus`](https://github.com/CJX0712/worldai-nexus) — 入库 → 混合检索 → 工具路由 → 生成；默认零依赖 Mock，可切 OpenAI 兼容 / GGUF
- [`worldai-rag`](https://github.com/CJX0712/worldai-rag) — faiss + BM25 混合检索 / ONNX 重排 / GGUF 本地推理
- [`worldai-stack`](https://github.com/CJX0712/worldai-stack) — FastEmbed(ONNX) / FAISS / Rank-BM25 / llama.cpp，模块只依赖 Protocol
- [`worldrag`](https://github.com/CJX0712/worldrag) — CJK 单字+双字 BM25（零依赖 tokenizer）+ 向量双路召回，独立索引评测 recall@k / MRR
- [`starlight-ai-stack`](https://github.com/CJX0712/starlight-ai-stack) — 摄取 → 混合检索 → 引用生成，无 GPU 的 Windows 机器上可全程跑通
- [`starlight-rag`](https://github.com/CJX0712/starlight-rag) — BM25 + 向量双路召回 RRF 融合；重排权重封顶 50%，免 GPU、无 torch
- [`novamind`](https://github.com/CJX0712/novamind) — 协议优先、离线可验的端到端 RAG Agent
- [`novamind-rag`](https://github.com/CJX0712/novamind-rag) — FAISS + BM25 双路召回，ONNX cross-encoder 按 0.3 加权融合，带 AST 安全计算器

**模块化 AI 系统与平台**（17）

- [`aether-ai-core`](https://github.com/CJX0712/aether-ai-core) — 把「文档摄取 → 向量召回 → 生成 → 工具调用」切成 10 个职责单一的模块
- [`aether-ai-core-v2`](https://github.com/CJX0712/aether-ai-core-v2) — 晨星智核 v2：默认栈零重依赖，Chroma / FAISS / vLLM·Ollama 以适配器即插即用
- [`atlas-ai-stack`](https://github.com/CJX0712/atlas-ai-stack) — 混合检索 + 守卫式跨域问答
- [`chenxing-ai-stack`](https://github.com/CJX0712/chenxing-ai-stack) — 覆盖「摄入 → 向量化 → 召回 → 重排 → 编排 → 推理 → 服务 → 观测」全链路
- [`helix-ai-engine`](https://github.com/CJX0712/helix-ai-engine) — Provider-agnostic 编排引擎：RAG + 工具型 Agent，模块间只走接口契约
- [`lumen-ai`](https://github.com/CJX0712/lumen-ai) — 抽象接口编排 Ollama / FAISS / FastAPI / Gradio，每模块带 Mock，后端可插拔
- [`morningstar-ai`](https://github.com/CJX0712/morningstar-ai) — 晨星 AI · 模块化 RAG + Agent 系统原型
- [`nebula-ai-core`](https://github.com/CJX0712/nebula-ai-core) — 11 个 AI 功能模块，每块 = Protocol 接口 + 默认实现；默认后端零依赖离线可跑
- [`nebula-ai-stack`](https://github.com/CJX0712/nebula-ai-stack) — 无 GPU、15GB 内存的 Windows 上跑通「文档 → 检索 → 重排 → 引用生成 → 评测」全链路
- [`nexus-ai-core`](https://github.com/CJX0712/nexus-ai-core) — 能力中台：模型网关 / 检索 / 智能体 / 工作流 / 记忆；无 Key 无网无 GPU 时离线降级
- [`nexus-ai-platform`](https://github.com/CJX0712/nexus-ai-platform) — NexusAI 平台：模型网关 / 知识检索 / 智能体
- [`novaai-stack`](https://github.com/CJX0712/novaai-stack) — 零依赖默认的 RAG + ReAct Agent，ingest / embed / vectorstore / rerank / llm 等十个模块
- [`quasar-ai-runtime`](https://github.com/CJX0712/quasar-ai-runtime) — 混合检索 + 工具调用智能体 + 证据绑定回答；离线档零模型零网络全绿
- [`starforge-ai`](https://github.com/CJX0712/starforge-ai) — 模块只依赖 ABC 抽象接口，内置确定性 Mock 后端，零网络零密钥即可跑通端到端
- [`stellar-ai-core`](https://github.com/CJX0712/stellar-ai-core) — 以「单一职责 + 清晰接口 + 能力注册表」组织能力，模块只经抽象契约通信
- [`stellar-ai-stack`](https://github.com/CJX0712/stellar-ai-stack) — 零依赖离线可跑：mock LLM + BLAKE2b 哈希嵌入 + 内存余弦索引 + IDF 重排
- [`stellar-ai-workbench`](https://github.com/CJX0712/stellar-ai-workbench) — 桌面 AI 工作台：模型网关（故障转移 + Mock）、可插拔 RAG、智能体编排、记忆

**可自证 · 证据锚定**（4）

- [`aether-research`](https://github.com/CJX0712/aether-research) — 可审计的深度研究 Agent —— 逐字引用校验
- [`veritas-ai`](https://github.com/CJX0712/veritas-ai) — 不变量优先、可自进化的 Agent 运行时 —— 把「正确性」从测试环节提升到架构层
- [`aletheia-cognition`](https://github.com/CJX0712/aletheia-cognition) — 推理时计算 Scaling 引擎（本地 RAG + inference-time compute）
- [`stellar-nexus`](https://github.com/CJX0712/stellar-nexus) — 检索增强 + 自适应链路路由 + 断言级归因校验 + 智能体闭环 + 评测门禁

**Agent 运行时**（1）

- [`aetherflow`](https://github.com/CJX0712/aetherflow) — 持久、可观测的通用 AI Agent 运行时（TypeScript）

**应用平台与服务**（3）

- [`ai-platform-agent-rag`](https://github.com/CJX0712/ai-platform-agent-rag) — LangGraph 编排 Agent + Chroma 知识库 + FastAPI 网关 + 单文件 WebUI
- [`ai-rag-platform`](https://github.com/CJX0712/ai-rag-platform) — FastAPI + Qdrant + Ollama + React 的 RAG 问答平台
- [`ai-llm-api`](https://github.com/CJX0712/ai-llm-api) — FastAPI + llama-cpp-python 本地 LLM 推理服务，镜像自动推 ghcr.io

**工程基建**（1）

- [`repo-hygiene-gate`](https://github.com/CJX0712/repo-hygiene-gate) — 最小仓库卫生门禁 · CI 冒烟验证模板


**新锐 RAG 与智能体系统**（8）

- [`zhishu`](https://github.com/CJX0712/zhishu) — 智枢：本地优先、混合推理的企业级 AI 知识中枢与智能体平台，Web/API/CLI 三形态
- [`phosphor-ai-stack`](https://github.com/CJX0712/phosphor-ai-stack) — 端到端检索增强智能体平台：摄入 → 分块 → 向量化 → 混合检索 → 重排 → 多智能体
- [`ragnext`](https://github.com/CJX0712/ragnext) — 模块化 RAG：FAISS / sentence-transformers / ragas 评测，CPU 可跑、一键复现
- [`zhi-rag`](https://github.com/CJX0712/zhi-rag) — ZhiDa 多模态 RAG 引擎：BM25 + dense + RRF 混合检索，LLM 可插拔
- [`cxrag`](https://github.com/CJX0712/cxrag) — CxRAG 混合检索增强问答引擎：离线 / CPU / 模块化 / 一键复现
- [`aurora-rag`](https://github.com/CJX0712/aurora-rag) — 模块化、可插拔、CPU/离线可运行的 RAG 系统
- [`helios-ai-stack`](https://github.com/CJX0712/helios-ai-stack) — 分层架构 RAG：Protocol 可注入、三档 profile、可量化评测基线
- [`astraea-ai-system-qhui1`](https://github.com/CJX0712/astraea-ai-system-qhui1) — Astraea：自演化多智能体 AI 系统内核
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
[ai-dev-env-report](https://github.com/CJX0712/ai-dev-env-report) Windows 本机 AI 开发环境安装清单，表格化呈现每一步状态 ·
[ai-library-dashboard](https://github.com/CJX0712/ai-library-dashboard) AI 资料库总览看板，零依赖零构建，双击即用


[sudoku-lab](https://github.com/CJX0712/sudoku-lab) 唯一解保证的数独生成 / 求解器 · 50 题无头自检全绿
[starforge](https://github.com/CJX0712/starforge) GitHub 高星仓库榜单浏览器 · 247 真实仓库 / 12.25M 星 · 10 赛道筛选 · 收藏导出

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
