# SpecAgent AI 网站开发跟踪文档

本文档用于跟踪 `SpecAgent AI` 官方网站的开发进度。基于 `plans/` 目录下生成的设计文档制定。

## 1. 项目初始化与基础设施 (Infrastructure & Setup)
- [x] **环境搭建**
    - [x] 确认 Django 环境与依赖 (`requirements.txt`)。
    - [x] 配置前端构建工具 (如需构建 React/Vue 组件或 Tailwind CSS)。
    - [x] 配置静态文件 (Static Files) 与媒体文件 (Media) 目录结构。
- [x] **基础架构**
    - [x] 创建基础模板 (`base.html`)：包含 Meta 信息、SEO 标签、通用 Header 和 Footer。
    - [x] 实现 **JSON 内容加载器**：编写 Django Context Processor 或 Utility 函数，用于读取并解析 `data/*.json` 文件，将数据注入模板。
    - [x] 定义全局样式变量 (CSS Variables / Tailwind Config)：深空蓝背景、荧光青强调色、字体设置。

## 2. 数据层建设 (Data Layer)
根据设计文档，创建各个页面的 JSON 数据文件（建议存放于 `data/` 或 `static/data/` 目录）。
- [x] `home_data.json` (首页 Hero, 核心理念, 行业全景)
- [x] `technology_data.json` (技术架构, 优势)
- [x] `government_data.json` (政企业务内容)
- [x] `aviation_data.json` (航空行业内容)
- [x] `education_data.json` (教育培训内容)
- [x] `design_data.json` (设计领域内容)
- [x] `research_data.json` (科研领域内容)
- [x] `portal_data.json` (登录页与 Demo 系统静态文案)

## 3. 页面开发任务 (Page Implementation)

### 3.1 公共组件 (Global Components)
- [x] **导航栏 (Navbar)**
    - [x] 实现初始透明、滚动磨砂玻璃效果 (Glassmorphism)。
    - [x] 响应式菜单 (Mobile Menu)。
- [x] **页脚 (Footer)**
    - [x] 包含版权信息、ICP 备案号、社交链接。
- [x] **Bento Grid 组件**
    - [x] 实现通用的网格布局容器，用于首页行业入口展示。

### 3.2 首页 (Home Page)
- [x] **Hero Section**
    - [x] 集成 3D 粒子特效 (Three.js / Spline) (Placeholder used).
    - [x] 实现标题动效 (Fade Up).
- [x] **核心理念板块**
    - [x] 实现三列布局与动态 Icon。
- [x] **行业全景板块**
    - [x] 使用 Bento Grid 展示 5 大行业卡片，实现 Hover 交互。

### 3.3 核心技术页 (Technology Page)
- [x] **Spec 概念可视化**
    - [x] 实现“自然语言 -> 转换层 -> Spec 代码”的视觉流程图。
- [x] **架构展示**
    - [x] 实现感知识别、逻辑决策、执行行动的三层架构图。

### 3.4 行业解决方案页面 (Industry Solutions)
所有行业页面复用类似的排版逻辑（Hero + 左右图文交替 + 优势总结），但需加载不同 JSON 数据。
- [x] **通用行业模板开发** (可减少重复工作)
    - [x] 创建 `solution_detail.html` 模板。
    - [x] 实现动态路由 `/solutions/<industry_id>/`。
- [x] **政企业务页**: 重点展示公文生成动效 Mockup。
- [x] **航空行业页**: 重点展示雷达扫描与 HUD 风格元素。
- [x] **教育培训页**: 重点展示亲和力风格卡片与插画。
- [x] **设计领域页**: 重点展示瀑布流布局与 Design Token 演示。
- [x] **科研领域页**: 重点展示双栏学术排版与网格背景。

### 3.5 自我演进页 (Self-Optimization Page)
展示 SpecAgent 如何通过元 Spec (Meta-Spec) 实现自我检查、自我修复与代码演进。
- [ ] **数据准备**: 创建 `optimization_data.json`。
- [ ] **页面开发**: 
    - [ ] 可视化展示 "Spec 演进循环" (Loop)。
    - [ ] 对比展示 "优化前 vs 优化后" 的代码/Spec 片段。
    - [ ] 实时日志流模拟 (Simulation Log)。

## 4. 登录与 Demo 系统 (Client Portal)
- [x] **登录页**
    - [x] 实现左右分栏布局。
    - [x] 集成 Django Auth 登录表单 (Mocked for Demo).
- [x] **仪表盘 (Dashboard)**
    - [x] 实现用户欢迎栏。
    - [x] 根据用户权限展示对应的 Demo 入口卡片。
- [x] **Demo Sandbox 框架**
    - [x] 开发三栏布局容器：参数配置(左) + 对话框(中) + 实时预览(右)。
    - [x] **Mock 交互逻辑**: 编写前端 JS 脚本，模拟 Agent 接收指令并输出日志/结果的过程 (无需真实后端 AI，仅前端演示)。

## 5. 视觉与素材制作 (Visuals & Assets)
- [x] **3D/动效资源**
    - [x] 首页粒子网格背景 (Implemented via Unsplash/CSS Placeholder).
    - [x] 各行业 Hero 背景抽象图 (Configured in JSON).
- [ ] **Mockup 物料**
    - [ ] 制作“公文生成前后对比”图。
    - [ ] 制作“航空情报分析”界面图。
    - [ ] 制作“设计规范自动生成”演示视频/GIF。

## 6. 测试与交付 (QA & Delivery)
- [ ] **多设备测试**: 桌面端、平板、手机端响应式检查。
- [ ] **数据校验**: 检查所有 JSON 字段是否正确渲染，无缺漏。
- [ ] **ICP 备案信息**: 确保页脚包含 `ICP_BEIAN.txt` 中的信息。
- [ ] **性能优化**: 图片懒加载、静态资源压缩。

---
**当前状态**: 规划完成，准备启动 `1. 项目初始化` 阶段。
