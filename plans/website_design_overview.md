# SpecAgent AI 官方网站设计概览

## 1. 项目背景与目标
**SpecAgent AI** 是一家专注于将Spec（规范）驱动的Agent技术应用于垂直行业的初创公司。网站旨在展示公司核心技术优势，体现其在政企、航空、培训、设计、科研等领域的专业解决方案，并提供客户Demo体验入口。

## 2. 网站整体风格与调性
*   **设计关键词**：专业 (Professional)、未来感 (Futuristic)、理性 (Rational)、精准 (Precise)、连接 (Connected)。
*   **视觉风格**：
    *   采用 **Bento Grid (便当盒)** 布局来展示多元化的业务板块。
    *   **深色模式 (Dark Mode)** 为主基调，体现科技深邃感。
    *   **微交互 (Micro-interactions)**：鼠标悬停时的光效、流畅的页面转场。
*   **配色方案**：
    *   主色：深空蓝 (#0A192F) 或 黑曜石色 (#121212)
    *   强调色：荧光青 (#64FFDA) - 代表“Spec/规范”的精准；电光紫 (#7059E8) - 代表“Agent/智能”的灵动。
    *   辅助色：高级灰 - 用于文字和边框。

## 3. 站点地图 (Site Map)
1.  **首页 (Home)**
    *   全站概览、核心价值主张、行业入口导航。
2.  **核心技术 (Technology)**
    *   Spec驱动原理、Agent架构、技术优势。
3.  **行业解决方案 (Solutions)**
    *   政企业务 (Government & Enterprise)
    *   航空行业 (Aviation)
    *   教育培训 (Training & Education)
    *   设计领域 (Design)
    *   科研领域 (Research)
4.  **客户登录/Demo中心 (Client Portal)**
    *   登录页、Demo仪表盘。

## 4. 技术栈建议
*   **前端**：React / Next.js (SEO友好，高性能)，Tailwind CSS (快速样式开发)，Framer Motion (动画效果)。
*   **后端**：Django (配合现有环境，适合快速开发业务逻辑和API)。
*   **3D/图形**：Three.js 或 Spline (用于展示3D Agent模型或Spec流动效果)。

## 5. 数据驱动内容 (Data-Driven Content)
为了保证内容的可维护性和多语言拓展性，所有页面的静态文案、图片路径、元数据等均通过 JSON 文件进行配置和渲染。
*   **结构**：每个页面对应一个独立的 JSON 文件（如 `home_data.json`, `aviation_data.json`）。
*   **优势**：
    *   **解耦**：设计与内容分离，修改文案无需动代码。
    *   **复用**：相同的组件（如 Bento Grid）可以复用同一套渲染逻辑，只需传入不同的 JSON 数据。
    *   **i18n**：方便后续扩展国际化多语言版本。

---

# 详细页面规划索引
请参考 `plans/` 文件夹下的具体页面设计文档：
- `home_page.md`: 首页详细设计
- `government_enterprise_page.md`: 政企业务页面
- `aviation_page.md`: 航空行业页面
- `education_training_page.md`: 培训行业页面
- `design_page.md`: 设计领域页面
- `scientific_research_page.md`: 科研领域页面
- `technology_page.md`: 技术优势页面
- `login_demo_system.md`: 登录与Demo系统
