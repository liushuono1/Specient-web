# 技术优势页面 (Technology)

## 1. 页面定位
解释“什么是 Spec 驱动”以及各类技术优势，建立技术壁垒认知。

## 2. 内容规划

### A. 核心概念：什么是 Spec 驱动？ (The Spec-Driven Philosophy)
*   **图解**: 
    *   **左侧 (Natural Language)**: "帮我定个票" (模糊，易错)。
    *   **中间 (Transformation)**: SpecAgent 转换层 (NLP + Formal Verification)。
    *   **右侧 (Spec)**: `{ "action": "book_flight", "params": { "airline": "CA", "class": "economy", "policy_check": "strict" } }` (精确，机器可读，合规)。
*   **文案**: 大语言模型擅长发散，工业应用需要收敛。Spec 是我们给模型戴上的“理性枷锁”，确保每一次输出都符合严格的业务规范。

### B. 技术架构 (Architecture)
*   **三层架构图**:
    1.  **感知层 (Perception)**: 多模态输入（文本、图像、仪器数据）。
    2.  **决策层 (Reasoning)**: Spec 引擎 + LLM 大脑。实时校验，拒绝幻觉。
    3.  **执行层 (Actuation)**: API 连接器，RPA 机器人，物理设备接口。

### C. 关键优势 (Key Differentiators)
*   **Safety (安全)**: 任何偏离 Spec 的操作都会被拦截。
*   **Interoperability (互操作)**: 轻松集成到现有的 ERP/CRM/OA 系统。
*   **Customizability (可定制)**: 客户无需懂代码，只需用自然语言定义业务 Spec。

## 3. 样式要求
*   **风格**: 硬核科技风。线条硬朗，使用“代码视窗”作为主要视觉容器。
*   **配色**: 黑客绿 (Matrix Green) 或 终端白字黑底。

## 4. 数据来源
*   本页面内容由 `technology_data.json` 驱动渲染。
