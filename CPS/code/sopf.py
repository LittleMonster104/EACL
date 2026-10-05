# sopf.py
import numpy as np
from sklearn.neighbors import KernelDensity
from typing import List, Dict, Tuple
from config import embed

def sopf(chains: List[Dict], fragments: List[Tuple[str, str]], top_k: int = 12) -> List[Dict]:
    """对比式核密度重排序 + 超参自由切割（gap statistic）
    
    Note: 简化实现版本
    - Facet分解: 完整版应使用学习的投影矩阵 P_t (需2400标注样本离线训练)
    - 此简化版直接embed fragment文本
    """
    # 简化版: 直接embed (完整版: f_t = P_t @ h, 其中P_t为学习的投影矩阵)
    f_vecs = np.stack([embed(f"{t} {txt}") for t, txt in fragments])
    c_vecs = np.stack([embed(ch["chain"]) for ch in chains])

    # 冗余密度 ρ
    bandwidth = np.median([np.linalg.norm(c_vecs[i] - c_vecs[j]) for i in range(len(chains)) for j in range(i + 1, len(chains))])
    kde = KernelDensity(kernel='gaussian', bandwidth=bandwidth)
    kde.fit(c_vecs)
    log_dens = kde.score_samples(c_vecs)
    rho = np.exp(log_dens)

    # 覆盖梯度 γ (修复空集问题 - 对应论文Section 3.4.1修改)
    gamma = np.zeros(len(chains))
    selected = []  # 已选中的链索引
    
    # 迭代选择（实际使用时需要在循环中更新selected）
    # 这里为简化，计算初始gamma（空集情况）
    for i, cv in enumerate(c_vecs):
        gap_sum = 0
        for f_vec in f_vecs:
            if len(selected) == 0:
                # 空集时: gap_t = 1 (论文修改8)
                gap = 1.0
            else:
                # 非空集: gap_t = 1 - max(cos(c_l, f_t))
                max_sim = max([np.dot(c_vecs[j], f_vec) for j in selected])
                gap = 1.0 - max_sim
            gap_sum += gap * np.dot(cv, f_vec)
        gamma[i] = gap_sum

    # 对比得分 & 自动切割
    scores = gamma / (rho + 1e-8)
    order = np.argsort(-scores)
    for i in range(1, len(order)):
        if (scores[order[i - 1]] - scores[order[i]]) / scores[order[i - 1]] > 0.05:
            cut = i
            break
    else:
        cut = min(top_k, len(order))
    return [chains[order[i]] for i in range(cut)]