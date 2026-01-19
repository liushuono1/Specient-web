# 首页 (Home Page) 设计方案

## 1. 页面目标
在5秒内传达“Spec驱动Agent”的核心概念，明确展示五大业务领域，并引导用户点击深入了解或登录体验。

## 2. 文案与内容规划

### A. Hero Section (首屏)
*   **主标题 (H1)**: Spec驱动智能，重构行业规则 (Redefining Industries with Spec-Driven Agents)
*   **副标题 (Subhead)**: 从模糊的指令到精准的执行。SpecAgent AI 将严格的规范(Spec)与生成式AI的灵活性结合，为政企、航空、科研等领域提供零差错的智能代理服务。
*   **CTA按钮**: 
    *   [主要] 探索解决方案 (Explore Solutions)
    *   [次要] 观看演示 (Watch Demo) - 弹窗播放视频。
*   **视觉素材描述**: 
    *   **背景**: 动态的3D粒子流，粒子汇聚成一张发光的网格（代表Spec），网格节点上通过光线连接着不同的行业图标（飞机、文件、烧杯、笔刷等）。
    *   **交互**: 鼠标移动会轻微改变粒子流的流动方向，体现“响应式的智能”。

### B. 核心理念 (Why Spec-Driven?)
*   **文案**: 
    *   标题: 为什么选择 Spec 驱动？
    *   描述: 传统的LLM容易产生幻觉。我们将行业标准(Standard)、操作规范(Spec)转化为Agent不仅能读懂，更能严格遵守的代码约束。
    *   关键词: 确定性 (Deterministic)、可解释 (Explainable)、行业合规 (Compliant)。
*   **视觉/布局**: 三列布局，每列一个动态Icon（如：锁=安全，尺子=精准，大脑=智能）。

### C. 行业全景 (Industry Panorama)
*   **布局**: 采用 **Bento Grid (便当盒)** 风格的卡片式布局。
*   **内容板块**:
    1.  **政企业务**: "数据治理与公文写作的自动化专家" -> 链接至政企页。
    2.  **航空行业**: "保障每一次飞行的精准调度与维护" -> 链接至航空页。
    3.  **教育培训**: "AI教员，重塑职业技能传承" -> 链接至培训页。
    4.  **设计领域**: "从规范文档直接生成合规设计" -> 链接至设计页。
    5.  **科研领域**: "加速实验流程，从文献到发现" -> 链接至科研页。
*   **视觉素材**: 每个卡片背景为该行业的抽象线条图或高质量暗色调实景图，悬停时图片轻微放大，覆盖层文字变亮。

### D. 信任背书 (Trust & Partners)
*   **文案**: 赋能未来的合作伙伴
*   **内容**: 一行灰度的企业Logo墙（如航空公司Logo、科研机构Logo等，可使用占位符）。

### E. 底部引导 (Footer CTA)
*   **文案**: 准备好体验真正的行业智能了吗？
*   **按钮**: 登录 Demo 系统 (Access Client Portal)

## 3. 动态效果要求
*   **滚动视差 (Parallax)**: 背景元素随滚动缓慢移动。
*   **文字显现**: 标题和段落采用向上浮动淡入 (Fade Up) 效果。
*   **导航栏**: 初始透明，滚动后变为半透明磨砂玻璃效果 (Glassmorphism)。

## 4. JSON 数据结构示例 (Sample Data Scheme)
本页面内容将由 `home_data.json` 驱动，以下为 Hero Section 的数据结构示例：

```json
{
  "heroSection": {
    "title": "Spec驱动智能，重构行业规则",
    "subTitle": "从模糊的指令到精准的执行。SpecAgent AI 将严格的规范(Spec)与生成式AI的灵活性结合...",
    "ctaButtons": [
      {
        "text": "探索解决方案",
        "link": "#solutions",
        "type": "primary"
      },
      {
        "text": "观看演示",
        "action": "openVideoModal",
        "type": "secondary"
      }
    ],
    "backgroundEffect": "3d-particle-network"
  }
}
```
