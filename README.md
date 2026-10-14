# 晨星 · Chen Xing

**前端工程师 × AI 系统构建者** · `深圳，中国` · `287 个开源仓库`

用 React 把界面做对，用 Python 把算法算对。

`零依赖 · 零构建 · 可复现 · 可验证` —— 每个项目都留下一条能被独立验证的硬不变量。

---

## ✦ 旗舰：天玑 TIANJI —— 世界顶级混合架构语言模型全栈

**[tianji-ai](https://github.com/CJX0712/tianji-ai)** · Gated DeltaNet × MLA × MoE × Muon2 × 投机解码 · 仅依赖 NumPy · CPU 可训

> 十层架构 · 1024 条可执行微指令 · 10 道可证门禁全绿 · 16 项验收指标达标

不是从零发明，而是把 2026 年已被工业界验证的最优解（Qwen3-Next 3:1 混合、DeepSeek-V3 MoE/MLA、Muon2）**正确地组合起来**，并用可复现基准证明它真的能用：训练 300 步 loss −16.6%、KV cache 节省 83.3%、解析反向 vs 中心差分误差 6.21e-09、同 seed 逐位一致。门禁哲学：**失败就如实报失败，不允许放宽阈值凑绿**。

| 十层分解 | L0 数值内核 → L1 反向契约 → L2 BPE 分词 → L3 架构原语 → L4 Gated DeltaNet → L5 DeepSeek-V3 MoE → L6 Muon2 → L7 训练 → L8 推理量化 → L9 DPO/IPO/SimPO/KTO → L10 微指令+门禁 |
|---|---|

**姊妹系统**：[aurora-worldclass-ai](https://github.com/CJX0712/aurora-worldclass-ai)（MLA+GDN+SWA 混合注意力 / MTP 自投机 / MuonClip）· [tianshu-ai](https://github.com/CJX0712/tianshu-ai)（天枢 · 32 算法家族 + Caruana 集成选择）· [world-class-ai](https://github.com/CJX0712/world-class-ai)（十层分解架构总纲）

---

## 世界顶级 AI 内核矩阵

零依赖、数学可验证的计算内核家族 —— 每个模块以硬不变量自检，浏览器 / Node / Python 三端可跑。

| 内核 | 一句话 | 不变量 |
|---|---|---|
| [aurora-ai-core](https://github.com/CJX0712/aurora-ai-core) | SOTA Transformer 原语：RMSNorm / RoPE / SwiGLU / 因果注意力 | 35/35 全绿 |
| [apex-forge](https://github.com/CJX0712/apex-forge) | 零依赖 AI/ML 基础库，每算法带可验证硬不变量 | 25/25 无头自检 |
| [stellar-ai](https://github.com/CJX0712/stellar-ai) | tape 自动微分 + RoPE/GQA/SwiGLU/MoE + KAN | 有限差分梯度检验全绿 |
| [zenith-ai](https://github.com/CJX0712/zenith-ai) | 15 模块零依赖 AI 核心库，浏览器 & Node 同码 | 24 项梯度校验不变量 |
| [xinghe-ai-forge](https://github.com/CJX0712/xinghe-ai-forge) | 数值线代 + ML + 深度学习单文件内核 | 17 项不变量 |
| [world-class-ai-foundation](https://github.com/CJX0712/world-class-ai-foundation) | 世界级引擎基础内核 | 16/16 全绿 |
| [morningstar-ai-engine](https://github.com/CJX0712/morningstar-ai-engine) | Jacobi SVD / Cholesky / EM-GMM / 反向传播 / 注意力 / Adam | 15/15 全绿 |
| [ai-forge-core](https://github.com/CJX0712/ai-forge-core) | Verification-First 纯 JS AI 核 | 12/12 自检 |
| [chenxing-ai-core](https://github.com/CJX0712/chenxing-ai-core) | 反向模式 AD + Transformer + Jacobi-SVD + Cholesky + logsumexp + Adam | 11/11 全绿 |
| [phosphor-ai](https://github.com/CJX0712/phosphor-ai) / [phosphor-py](https://github.com/CJX0712/phosphor-py) | SVD / JacobiEig / PCA / GMM / kNN / MLP / Attention（JS + Python 双端） | 三重交叉验证 |
| [forge-core](https://github.com/CJX0712/forge-core) | autograd / SVD / Jacobi / k-means / GMM-EM / PCA / 注意力 | 8/8 绿 |
| [gradforge](https://github.com/CJX0712/gradforge) | 反向模式自动微分 + Newton-CG + 优化器族 | 7/7 不变量 |
| [StarAI-Kernel](https://github.com/CJX0712/StarAI-Kernel) | 纯 JS 十层架构 AI 内核 | 23 项逐条可验证 |
| [microforge](https://github.com/CJX0712/microforge) | RMSNorm+RoPE+GQA+SwiGLU+FlashAttention-2+Muon 微型 LLM 栈 | 11 条硬不变量 |
| [mambaforge](https://github.com/CJX0712/mambaforge) | 选择性状态空间模型（纯 JS） | 不变量自检 |
| [morningforge](https://github.com/CJX0712/morningforge) | micrograd / LAPACK 语义 SVD / Jolliffe PCA / k-means++ / Vaswani 注意力 / Adam | 8/8 交叉验证 |
| [jsforge](https://github.com/CJX0712/jsforge) | 纯 JS 单文件 ML/数值库，无头 Node 8/8 | 全绿 |
| [ai-microforge](https://github.com/CJX0712/ai-microforge) / [forge-1024](https://github.com/CJX0712/forge-1024) | 第十层微指令基石：1024 条可验证微指令 | 零构建可复现 |
| [morningstar-ai-forge](https://github.com/CJX0712/morningstar-ai-forge) | 十层架构 + 跨库交叉验证（forge 纯实现 vs numpy/scipy/sklearn/torch 黄金参照） | 参照对拍 |

---

## forge —— 从零手写的算法实验室

**48 个算法实验室**，**零依赖 · 零构建 · 单文件 HTML**。浏览器打开即运行，Node 无头自检全绿。

不是调库 Demo。每个 forge 都留了一条能被交叉验证的硬标准：解析解对数值解、暴力枚举对贪心、KKT 互补松弛、Bellman 残差收敛……

| 领域 | 代表项目 | 验证的不变量 |
| --- | --- | --- |
| 深度学习 | [nn-forge](https://github.com/CJX0712/nn-forge) · [attn-forge](https://github.com/CJX0712/attn-forge) · [transformer-forge](https://github.com/CJX0712/transformer-forge) · [diffusion-forge](https://github.com/CJX0712/diffusion-forge) | 梯度检验 maxRelErr ≈ 1e-7 |
| 强化学习 | [az-forge](https://github.com/CJX0712/az-forge)（AlphaZero 自对弈）· [cartpole-forge](https://github.com/CJX0712/cartpole-forge)（PPO）· [rl-forge](https://github.com/CJX0712/rl-forge) · [mcts-forge](https://github.com/CJX0712/mcts-forge) | Bellman 残差 → 0 |
| 概率与推断 | [gmm-forge](https://github.com/CJX0712/gmm-forge) · [hmm-forge](https://github.com/CJX0712/hmm-forge) · [vi-forge](https://github.com/CJX0712/vi-forge) · [mcmc-forge](https://github.com/CJX0712/mcmc-forge) | 对数似然 / ELBO 单调不降 |
| 数值线代 | [pca-forge](https://github.com/CJX0712/pca-forge) · [nmf-forge](https://github.com/CJX0712/nmf-forge) · [ica-forge](https://github.com/CJX0712/ica-forge) · [gp-forge](https://github.com/CJX0712/gp-forge) | ‖Av − λv‖ ≈ 1e-15 |
| 经典算法 | [astar-forge](https://github.com/CJX0712/astar-forge) · [avl-forge](https://github.com/CJX0712/avl-forge) · [rs-forge](https://github.com/CJX0712/rs-forge) · [svm-forge](https://github.com/CJX0712/svm-forge) | 堆序不变量 · KKT 互补松弛 |

<details>
<summary><b>展开全部 48 个实验室 →</b></summary>

**深度学习与生成**（9）：[nn-forge](https://github.com/CJX0712/nn-forge) MLP 反向传播 · [attn-forge](https://github.com/CJX0712/attn-forge) 缩放点积自注意力+因果掩码+多头 · [transformer-forge](https://github.com/CJX0712/transformer-forge) mini-GPT · [transformer-forge-v2](https://github.com/CJX0712/transformer-forge-v2) decoder-only 因果 Transformer · [diffusion-forge](https://github.com/CJX0712/diffusion-forge) DDPM 闭式解/DDIM · [ddpm-forge](https://github.com/CJX0712/ddpm-forge) 31+16 项不变量 · [denoise-forge](https://github.com/CJX0712/denoise-forge) U-Net+FiLM 图像 DDPM · [word2vec-forge](https://github.com/CJX0712/word2vec-forge) skip-gram+负采样 · [bpe-forge](https://github.com/CJX0712/bpe-forge) 字符级 BPE

**强化学习与决策**（5）：[az-forge](https://github.com/CJX0712/az-forge) AlphaZero · [cartpole-forge](https://github.com/CJX0712/cartpole-forge) PPO+GAE · [rl-forge](https://github.com/CJX0712/rl-forge) Q-learning vs 价值迭代 · [gridworld-rl-lab](https://github.com/CJX0712/gridworld-rl-lab) · [mcts-forge](https://github.com/CJX0712/mcts-forge) UCT vs Minimax

**概率模型与推断**（7）：[gmm-forge](https://github.com/CJX0712/gmm-forge) · [hmm-forge](https://github.com/CJX0712/hmm-forge) 前向-后向/Viterbi/Baum-Welch · [vi-forge](https://github.com/CJX0712/vi-forge) 平均场 CAVI · [mcmc-forge](https://github.com/CJX0712/mcmc-forge) MH/HMC/Gibbs · [kalman-forge](https://github.com/CJX0712/kalman-forge) KF/RTS/粒子滤波 · [gp-forge](https://github.com/CJX0712/gp-forge) Cholesky 推断+边际似然解析梯度 · [ot-forge](https://github.com/CJX0712/ot-forge) Sinkhorn

**数值线代与无监督**（5）：[pca-forge](https://github.com/CJX0712/pca-forge) 雅可比特征分解 · [nmf-forge](https://github.com/CJX0712/nmf-forge) Lee-Seung+ALS · [ica-forge](https://github.com/CJX0712/ica-forge) FastICA · [kmeans-forge](https://github.com/CJX0712/kmeans-forge) k-means++/1D DP 对照 · [spectral-forge](https://github.com/CJX0712/spectral-forge) NJW+Lanczos

**经典算法与数据结构**（8）：[astar-forge](https://github.com/CJX0712/astar-forge) · [avl-forge](https://github.com/CJX0712/avl-forge) · [tree-forge](https://github.com/CJX0712/tree-forge) 决策树+随机森林 · [sort-forge](https://github.com/CJX0712/sort-forge) · [sudo-forge](https://github.com/CJX0712/sudo-forge) · [rx-forge](https://github.com/CJX0712/rx-forge) Thompson NFA · [maze-forge](https://github.com/CJX0712/maze-forge) · [rs-forge](https://github.com/CJX0712/rs-forge) GF(256) Reed-Solomon

**几何 · 物理 · 信号**（11）：[fourier-forge](https://github.com/CJX0712/fourier-forge) · [orbit-forge](https://github.com/CJX0712/orbit-forge) Verlet 动量守恒 · [ray-forge](https://github.com/CJX0712/ray-forge) · [ray-forge-v2](https://github.com/CJX0712/ray-forge-v2) Whitted+Fresnel+AA · [koch-forge](https://github.com/CJX0712/koch-forge) · [ant-forge](https://github.com/CJX0712/ant-forge) Langton ant · [cellular-lab](https://github.com/CJX0712/cellular-lab) · [life-forge](https://github.com/CJX0712/life-forge) · [synth-forge](https://github.com/CJX0712/synth-forge) WebAudio · [gravity-forge](https://github.com/CJX0712/gravity-forge) Barnes-Hut N 体 · [wave-forge](https://github.com/CJX0712/wave-forge) Crank-Nicolson 薛定谔

**机器学习基础**（3）：[svm-forge](https://github.com/CJX0712/svm-forge) SMO/KKT · [tinyml-lab](https://github.com/CJX0712/tinyml-lab) · [forest-forge-v2](https://github.com/CJX0712/forest-forge-v2) CART+Bagging+OOB

</details>

---

## Forge 系统 —— 可复现的机器学习算法库

**75+ 个模块化算法系统**（Python），复用顶级开源（scikit-learn / LightGBM / Optuna / FAISS / ruptures / river……），每套带纯 numpy 离线兜底与基线对照，CPU 可跑、确定性可复现。

**表格 · 监督 · 半监督**：[tabulaforge](https://github.com/CJX0712/tabulaforge) XGBoost+LightGBM+Optuna · [rankforge](https://github.com/CJX0712/rankforge) Learning to Rank · [cvforge](https://github.com/CJX0712/cvforge) 图像分类 · [intentforge](https://github.com/CJX0712/intentforge) 置信校准级联路由 · [featforge](https://github.com/CJX0712/featforge) / [featureforge](https://github.com/CJX0712/featureforge) AutoML 特征工程 · [semiforge](https://github.com/CJX0712/semiforge) / [gacsforge](https://github.com/CJX0712/gacsforge) 半监督 GACS（macro-F1 超基线 +0.0536）· [labelforge](https://github.com/CJX0712/labelforge) Dawid-Skene 弱监督 · [activeforge](https://github.com/CJX0712/activeforge) 主动学习 · [balanceforge](https://github.com/CJX0712/balanceforge) 长尾学习 · [imputeforge](https://github.com/CJX0712/imputeforge) 缺失值插补 · [svmforge](https://github.com/CJX0712/svmforge) 核 SVM · [metricforge](https://github.com/CJX0712/metricforge) 度量学习 · [metaforge](https://github.com/CJX0712/metaforge) ProtoNet/MAML/Reptile

**图与网络**：[graphforge](https://github.com/CJX0712/graphforge) GCN/GAT · [nodeforge](https://github.com/CJX0712/nodeforge) · [graphforge-linkpred](https://github.com/CJX0712/graphforge-linkpred) node2vec · [graphrepforge](https://github.com/CJX0712/graphrepforge) · [heteroforge](https://github.com/CJX0712/heteroforge) 异质图 HAAR · [gnnforge](https://github.com/CJX0712/gnnforge) GCN/GAT/GraphSAGE · [kgforge](https://github.com/CJX0712/kgforge) 知识图谱嵌入（Filtered MRR +17.56%）· [matchforge](https://github.com/CJX0712/matchforge) 图匹配 QAP/GRAMPA · [clusterforge](https://github.com/CJX0712/clusterforge) 共识聚类 · [spectralforge](https://github.com/CJX0712/spectralforge) 谱聚类

**因果 · 概率 · 不确定性**：[causalforge](https://github.com/CJX0712/causalforge) 交叉拟合 DML · [dagforge](https://github.com/CJX0712/dagforge) NOTEARS 因果发现 · [notearsforge](https://github.com/CJX0712/notearsforge) · [causaldiscforge](https://github.com/CJX0712/causaldiscforge) 跨家族共识集成 · [chainforge](https://github.com/CJX0712/chainforge) NUTS/ADVI/Laplace · [bayesforge](https://github.com/CJX0712/bayesforge) 贝叶斯优化 · [gaussforge](https://github.com/CJX0712/gaussforge) GP+AutoKernel · [gpforge](https://github.com/CJX0712/gpforge) 高斯过程 · [conformalforge](https://github.com/CJX0712/conformalforge) / [conformforge](https://github.com/CJX0712/conformforge) / [confforge](https://github.com/CJX0712/confforge) 共形预测 · [certiscale](https://github.com/CJX0712/certiscale) 推理时计算规模化（Anytime-valid）· [oodforge](https://github.com/CJX0712/oodforge) OOD 检测 · [seqforge](https://github.com/CJX0712/seqforge) KF/EKF/UKF/粒子滤波 · [pgmforge](https://github.com/CJX0712/pgmforge) 概率图模型

**时序 · 推荐 · 检索**：[chrono-forge](https://github.com/CJX0712/chrono-forge) / [tsforge](https://github.com/CJX0712/tsforge) 预测 · [changeforge](https://github.com/CJX0712/changeforge) 变化点检测 · [tscforge](https://github.com/CJX0712/tscforge) TinyRocket+DTW 分类 · [hawkesforge](https://github.com/CJX0712/hawkesforge) 自激发过程 · [recforge](https://github.com/CJX0712/recforge) / [recoforge](https://github.com/CJX0712/recoforge) 推荐 · [vecforge](https://github.com/CJX0712/vecforge) FAISS 向量检索 · [visionforge](https://github.com/CJX0712/visionforge) 以图搜图 · [voiceforge](https://github.com/CJX0712/voiceforge) librosa/whisper · [searchforge](https://github.com/CJX0712/searchforge) BM25+FAISS+LambdaMART（nDCG@10 +11.73%）· [topicforge](https://github.com/CJX0712/topicforge) LDA/NMF · [riverforge](https://github.com/CJX0712/riverforge) / [onlineforge](https://github.com/CJX0712/onlineforge) 在线学习/概念漂移

**生成模型**：[diffusionforge](https://github.com/CJX0712/diffusionforge) DDPM/DDIM · [diffuforge](https://github.com/CJX0712/diffuforge) NFE 预算采样 · [scoreforge](https://github.com/CJX0712/scoreforge) score-based 基准 · [rectforge](https://github.com/CJX0712/rectforge) Flow Matching/Rectified Flow · [flowforge](https://github.com/CJX0712/flowforge) RealNVP+MAF 精确似然 · [vaeforge](https://github.com/CJX0712/vaeforge) VAE/IWAE · [ssmforge](https://github.com/CJX0712/ssmforge) S4/S4D（adding problem 1e-11）· [FeynmanForge](https://github.com/CJX0712/FeynmanForge) / [symforge](https://github.com/CJX0712/symforge) 符号回归 · [ptqforge](https://github.com/CJX0712/ptqforge) / [quantforge](https://github.com/CJX0712/quantforge) 训练后量化

**优化 · 决策 · 博弈**：[convexforge](https://github.com/CJX0712/convexforge) KKT 认证凸优化（ADMM/Chambolle-Pock/内点）· [otforge](https://github.com/CJX0712/otforge) / [transforge](https://github.com/CJX0712/transforge) 最优传输 · [optiforge](https://github.com/CJX0712/optiforge) 组合优化 TSP/背包 · [SubmodForge](https://github.com/CJX0712/SubmodForge) 子模优化 (1−1/e) 保证 · [mooforge](https://github.com/CJX0712/mooforge) 多目标 EMO · [nasforge](https://github.com/CJX0712/nasforge) 神经架构搜索 · [eternalforge](https://github.com/CJX0712/eternalforge) 优化器不收敛分析 · [nashforge](https://github.com/CJX0712/nashforge) 不完美信息博弈均衡 · [banditforge](https://github.com/CJX0712/banditforge) 上下文老虎机+OPE · [rlforge](https://github.com/CJX0712/rlforge) 强化学习全谱系 · [offlineforge](https://github.com/CJX0712/offlineforge) / [tabularofflineforge](https://github.com/CJX0712/tabularofflineforge) 离线 RL+OPE · [ctrlforge](https://github.com/CJX0712/ctrlforge) iLQR/DDP 最优控制 · [imitationforge](https://github.com/CJX0712/imitationforge) BC/DAGGER · [neuroforge](https://github.com/CJX0712/neuroforge) 深度 RL · [portforge](https://github.com/CJX0712/portforge) 投资组合优化

**科学计算 · 信号 · 鲁棒**：[operatorforge](https://github.com/CJX0712/operatorforge) FNO/DeepONet 神经算子 · [odeforge](https://github.com/CJX0712/odeforge) 辛积分 ODE · [sindyforge](https://github.com/CJX0712/sindyforge) 稀疏系统辨识 · [sparseforge](https://github.com/CJX0712/sparseforge) 压缩感知 · [dictforge](https://github.com/CJX0712/dictforge) 字典学习 · [kernelforge](https://github.com/CJX0712/kernelforge) 随机特征核近似 · [tensorforge](https://github.com/CJX0712/tensorforge) 张量分解 · [topoforge](https://github.com/CJX0712/topoforge) 持久同调 · [SketchForge](https://github.com/CJX0712/SketchForge) 数据流草图 · [seqmineforge](https://github.com/CJX0712/seqmineforge) 序列模式挖掘（1.84× SOTA）· [robustforge](https://github.com/CJX0712/robustforge) 对抗鲁棒 · [fairforge](https://github.com/CJX0712/fairforge) / [equiforge](https://github.com/CJX0712/equiforge) 算法公平 · [privforge](https://github.com/CJX0712/privforge) / [miaforge](https://github.com/CJX0712/miaforge) / [perclass-mia](https://github.com/CJX0712/perclass-mia) / [aiaforge](https://github.com/CJX0712/aiaforge) 隐私与成员推断 · [watermarkforge](https://github.com/CJX0712/watermarkforge) LLM 水印 · [explainforge](https://github.com/CJX0712/explainforge) / [attribforge](https://github.com/CJX0712/attribforge) XAI 归因 · [anomalyforge](https://github.com/CJX0712/anomalyforge) / [anoforge](https://github.com/CJX0712/anoforge) 异常检测 · [mmforge](https://github.com/CJX0712/mmforge) / [modalforge](https://github.com/CJX0712/modalforge) / [mvforge](https://github.com/CJX0712/mvforge) 多模态/多视图 · [domainforge](https://github.com/CJX0712/domainforge) 域适应 · [neurosymforge](https://github.com/CJX0712/neurosymforge) 神经符号 · [distilforge](https://github.com/CJX0712/distilforge) 蒸馏 · [ensembleforge](https://github.com/CJX0712/ensembleforge) 自动化集成 · [fedforge](https://github.com/CJX0712/fedforge) 联邦学习 · [effattnforge](https://github.com/CJX0712/effattnforge) 高效注意力基准 · [alignforge](https://github.com/CJX0712/alignforge) DPO/IPO/KTO 对齐 · [upliftforge](https://github.com/CJX0712/upliftforge) 增益建模 CATE · [survforge](https://github.com/CJX0712/survforge) 生存分析 · [densforge](https://github.com/CJX0712/densforge) 密度估计（含未通过项，诚实记录）

---

## 端到端 AI 系统

| 项目 | 是什么 |
| --- | --- |
| [tianji-ai](https://github.com/CJX0712/tianji-ai) | **旗舰**：混合架构 LLM 全栈（见顶部） |
| [StellarAI](https://github.com/CJX0712/StellarAI) | 本地优先多模态 AI 引擎：transformers.js + hnswlib + 自研 ReAct 编排，零 API key |
| [chenxing](https://github.com/CJX0712/chenxing) | LLM 推理与智能体栈：RadixAttention / PagedAttention / 投机解码 / FlashAttention / GGUF k-quants 集大成 |
| [qiming-ai](https://github.com/CJX0712/qiming-ai) | 可验证 RAG：混合检索 + Cross-Encoder 重排 + 句级支持度校验 + 拒答门槛，76 测试 + 26 不变量 |
| [glassbox](https://github.com/CJX0712/glassbox) | 玻璃盒 RAG：BM25 + dense + RRF + rerank，证据链全可见 |
| [loom](https://github.com/CJX0712/loom) | MCP 原生本地智能体运行时：Ollama + MCP + crawl4ai |
| [aetheros](https://github.com/CJX0712/aetheros) | 默认拒答无出处断言的 Agent Runtime |
| [tekmor](https://github.com/CJX0712/tekmor) | 证据锚定的 RAG 知识库 + 单文件控制台 |
| [dialectica-ai](https://github.com/CJX0712/dialectica-ai) | 辩衡：证据锚定、可证收敛的多智能体审议 |
| [evolver](https://github.com/CJX0712/evolver) | 智能体自进化层：技能/踩坑蒸馏 + 对照组基准 |
| [aurora](https://github.com/CJX0712/aurora) | 纯本机 CPU 推理自主智能体（llama.cpp + Qwen2.5 + RAG + ReAct） |
| [hyperion-ai](https://github.com/CJX0712/hyperion-ai) | 双引擎：Python 训练内核 + TS 零依赖推理内核 |
| [morningstar-ai-collab](https://github.com/CJX0712/morningstar-ai-collab) | 可自托管 AI 原生协作平台，全栈 TS |
| [aetherflow](https://github.com/CJX0712/aetherflow) / [aether-research](https://github.com/CJX0712/aether-research) | 持久可观测 Agent 运行时 + 可审计深度研究（TS） |
| [zhishu](https://github.com/CJX0712/zhishu) · [worldforge-ai](https://github.com/CJX0712/worldforge-ai) · [atlas-ai-stack](https://github.com/CJX0712/atlas-ai-stack) · [helix-ai-engine](https://github.com/CJX0712/helix-ai-engine) · [lumen-ai](https://github.com/CJX0712/lumen-ai) · [starforge-ai](https://github.com/CJX0712/starforge-ai) · [stellar-ai-core](https://github.com/CJX0712/stellar-ai-core) · [stellar-nexus](https://github.com/CJX0712/stellar-nexus) · [veritas-ai](https://github.com/CJX0712/veritas-ai) · [aletheia-cognition](https://github.com/CJX0712/aletheia-cognition) · [reasonforge](https://github.com/CJX0712/reasonforge) · [novamind](https://github.com/CJX0712/novamind) · [quasar-ai-runtime](https://github.com/CJX0712/quasar-ai-runtime) · [nebula-ai-stack](https://github.com/CJX0712/nebula-ai-stack) · [nexus-ai-core](https://github.com/CJX0712/nexus-ai-core) · [phosphor-ai-stack](https://github.com/CJX0712/phosphor-ai-stack) · [ragnext](https://github.com/CJX0712/ragnext) · [zhi-rag](https://github.com/CJX0712/zhi-rag) · [cxrag](https://github.com/CJX0712/cxrag) · [aurora-rag](https://github.com/CJX0712/aurora-rag) · [helios-ai-stack](https://github.com/CJX0712/helios-ai-stack) · [astraea-ai-system-qhui1](https://github.com/CJX0712/astraea-ai-system-qhui1) · [worldai](https://github.com/CJX0712/worldai) 家族 · [MorningStar-RAG](https://github.com/CJX0712/MorningStar-RAG) · [ai-rag-platform](https://github.com/CJX0712/ai-rag-platform) · [ai-platform-agent-rag](https://github.com/CJX0712/ai-platform-agent-rag) · [ai-llm-api](https://github.com/CJX0712/ai-llm-api) | 模块化 RAG / Agent / 运行时家族（Protocol 优先、离线可验、后端可插拔） |
| [forgestack](https://github.com/CJX0712/forgestack) | 本地 AI 全家桶：forest/spectral/bpe 三引擎 + 向量检索 |

---

## 单文件工具

[schema-dowser](https://github.com/CJX0712/schema-dowser) CSV 函数依赖探矿 ·
[diff-scope](https://github.com/CJX0712/diff-scope) Myers 差分波前可视化 ·
[wave-loom](https://github.com/CJX0712/wave-loom) 约束传播织机 ·
[mojibake-er](https://github.com/CJX0712/mojibake-er) 乱码反推 ·
[prompt-terrain](https://github.com/CJX0712/prompt-terrain) prompt 冗余断层扫描 ·
[bitcrc](https://github.com/CJX0712/bitcrc) CRC 校验和对照标准向量 ·
[bitweave](https://github.com/CJX0712/bitweave) Huffman 无损压缩 ·
[ifs-atlas](https://github.com/CJX0712/ifs-atlas) 混沌游戏分形 ·
[sudoku-lab](https://github.com/CJX0712/sudoku-lab) 唯一解保证数独 ·
[starforge](https://github.com/CJX0712/starforge) GitHub 高星榜单浏览器 ·
[ai-dev-env-report](https://github.com/CJX0712/ai-dev-env-report) ·
[ai-library-dashboard](https://github.com/CJX0712/ai-library-dashboard) ·
[repo-hygiene-gate](https://github.com/CJX0712/repo-hygiene-gate) CI 冒烟模板

---

## 技术栈

| | |
| --- | --- |
| 前端 | React · TypeScript · Vite · 手写单文件 HTML/CSS/JS |
| 后端 | Python 3.13 · FastAPI |
| AI | 混合架构 LLM（GDN+MLA+MoE）· 从零手写的神经网络 · 混合检索（BM25/dense/RRF/rerank）· llama.cpp · Ollama · MCP · ONNX/GGUF |

---

<div align="center">

**✦** 天黑前把活干完，天亮时把结果交出去。

</div>
