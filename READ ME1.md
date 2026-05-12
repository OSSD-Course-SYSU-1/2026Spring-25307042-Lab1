# PDFKit 示例工程文件描述

## 一、工程概述

本项目是一个基于 HarmonyOS NEXT 的 PDF 文件查看与编辑示例应用，展示了如何使用 PDFKit 提供的能力进行 PDF 文件内容查看、编辑、转换等相关操作。

### 项目基本信息
- **项目名称**: PDFKit Sample Code (ArkTS)
- **开发语言**: ArkTS
- **目标平台**: HarmonyOS NEXT Developer Beta3 及以上
- **支持设备**: 华为 Phone、Tablet 和 2in1 设备
- **核心依赖**: @kit.PDFKit 模块

---

## 二、工程目录结构

```
pdfkit_-sample-code_-arkts-master/
├── AppScope/                          # 应用全局资源目录
│   └── resources/
│       └── base/
│           └── element/
│               └── string.json        # 全局字符串资源
├── entry/                             # 主模块目录
│   ├── src/
│   │   └── main/
│   │       ├── ets/                   # ArkTS 源码目录
│   │       │   ├── entryability/
│   │       │   │   └── EntryAbility.ets    # 应用入口 Ability
│   │       │   └── pages/             # 页面目录
│   │       │       ├── Index.ets           # 主页面(文件选择界面)
│   │       │       ├── PDFPreview.ets      # PDF 预览与编辑界面
│   │       │       └── PDFView.ets         # PdfView 组件预览界面
│   │       └── resources/             # 资源文件目录
│   │           ├── base/
│   │           │   ├── element/
│   │           │   │   ├── color.json      # 颜色资源
│   │           │   │   └── string.json     # 字符串资源
│   │           │   ├── media/
│   │           │   │   └── layered_image.json  # 图层图片配置
│   │           │   └── profile/
│   │           │       └── main_pages.json     # 页面路由配置
│   │           ├── en_US/             # 英文资源
│   │           │   └── element/
│   │           │       └── string.json
│   │           └── zh_CN/             # 中文资源
│   │               └── element/
│   │                   └── string.json
│   ├── build-profile.json5            # 模块构建配置
│   ├── oh-package.json5               # 模块依赖配置
│   └── hvigorfile.ts                  # 构建脚本
├── build-profile.json5                # 应用构建配置
├── oh-package.json5                   # 应用依赖配置
├── hvigorfile.ts                      # 应用构建脚本
├── readme_cn.md                       # 中文说明文档
└── readme_en.md                       # 英文说明文档
```

---

## 三、核心文件详解

### 3.1 入口文件 - EntryAbility.ets

**文件路径**: `entry/src/main/ets/entryability/EntryAbility.ets`

**功能描述**: 
应用的主入口 Ability，继承自 UIAbility，负责应用生命周期管理。

**核心功能**:
- `onCreate()`: Ability 创建时的初始化
- `onWindowStageCreate()`: 加载主页面 'pages/Index'
- `onDestroy()`: Ability 销毁时的资源释放
- `onForeground()`/`onBackground()`: 前后台切换处理

**关键代码**:
```typescript
windowStage.loadContent('pages/Index', (err) => {
  // 加载 Index 页面作为应用入口
});
```

---

### 3.2 主页面 - Index.ets

**文件路径**: `entry/src/main/ets/pages/Index.ets`

**功能描述**: 
文件选择主界面，提供三种 PDF 打开方式。

**核心功能**:
1. **打开本地 PDF 文件**: 通过 DocumentViewPicker 选择设备中的 PDF 文件
2. **打开资源 PDF 文件**: 从应用资源目录读取预置的 PDF 文件
3. **打开 PdfView 预览**: 使用 PdfView 组件预览 PDF

**关键方法**:
- `copyResourceFileAndJump()`: 复制资源文件到沙盒并跳转
- `copyURIAndJump(uri: string)`: 复制 URI 文件到沙盒并跳转

**依赖模块**:
- `@kit.CoreFileKit`: 文件操作和文件选择器
- `@kit.BasicServicesKit`: 业务错误处理
- `@kit.PerformanceAnalysisKit`: 日志记录

---

### 3.3 PDF 预览编辑页面 - PDFPreview.ets

**文件路径**: `entry/src/main/ets/pages/PDFPreview.ets`

**功能描述**: 
PDF 文件预览与编辑功能页面，提供完整的 PDF 操作能力。

**核心功能**:
1. **PDF 加载与显示**: 使用 pdfService 加载并显示 PDF 页面
2. **页面导航**: 上一页/下一页切换
3. **PDF 转图片**: 将 PDF 转换为图片保存
4. **添加文字**: 在 PDF 页面添加文本内容
5. **保存文件**: 保存编辑后的 PDF 文件

**关键方法**:
- `openFile()`: 加载 PDF 文档
- `aboutToAppear()`: 页面初始化，加载第一页
- `aboutToDisappear()`: 页面销毁时释放文档资源

**PDF 操作示例**:
```typescript
// 加载文档
this.document.loadDocument(this.filePath, '');

// 获取页面
let page: pdfService.PdfPage = this.document.getPage(pageIndex);

// 获取页面图像
this.pixelMap = page.getPagePixelMap();

// 添加文字
page.addTextObject('中文HelloWold123', 0, 0, textStyle);

// 保存文档
this.document.saveDocument(savePath);
```

**依赖模块**:
- `@kit.PDFKit`: PDF 服务核心功能
- `@kit.CoreFileKit`: 文件操作
- `@kit.ImageKit`: 图像处理
- `@kit.ArkUI`: 字体管理

---

### 3.4 PdfView 组件页面 - PDFView.ets

**文件路径**: `entry/src/main/ets/pages/PDFView.ets`

**功能描述**: 
使用 PdfView 组件展示 PDF 文件，提供更流畅的预览体验。

**核心功能**:
- 使用 PdfView 组件加载和显示 PDF
- 支持页面适配和滚动显示
- 提供返回按钮覆盖层

**关键代码**:
```typescript
PdfView({
  controller: this.controller,
  pageFit: pdfService.PageFit.FIT_WIDTH,  // 宽度适配
  showScroll: true                         // 显示滚动条
})
```

**依赖模块**:
- `@kit.PDFKit`: PDF 服务和 PdfView 组件
- `@kit.CoreFileKit`: 文件操作

---

## 四、配置文件说明

### 4.1 应用构建配置 - build-profile.json5

**文件路径**: `build-profile.json5`

**配置内容**:
- 支持的 SDK 版本: 5.0.0(12)
- 运行系统: HarmonyOS
- 构建模式: debug 和 release
- 模块配置: entry 模块

### 4.2 模块配置 - module.json5

**文件路径**: `entry/src/main/module.json5`

**配置内容**:
- 模块类型: entry (入口模块)
- 支持设备: phone, tablet, 2in1
- 主 Ability: EntryAbility
- 页面配置: 通过 $profile:main_pages 引用

---

## 五、PDFKit 核心接口

### 5.1 文档操作接口

| 接口名称 | 功能描述 | 参数说明 |
|---------|---------|---------|
| `loadDocument(path, password?, onProgress?)` | 加载 PDF 文档 | path: 文件路径<br>password: 加密密码(可选)<br>onProgress: 进度回调(可选) |
| `releaseDocument()` | 释放 PDF 文档 | 无参数 |
| `saveDocument(path, onProgress?)` | 保存文档 | path: 保存路径<br>onProgress: 进度回调(可选) |
| `getPage(index)` | 获取指定页面对象 | index: 页面索引 |
| `getPageCount()` | 获取页面总数 | 无参数 |
| `convertToImage(outputPath, startIndex)` | PDF 转图片 | outputPath: 输出路径<br>startIndex: 起始页索引 |

### 5.2 页面操作接口

| 接口名称 | 功能描述 | 参数说明 |
|---------|---------|---------|
| `getPagePixelMap()` | 获取页面图像 | 返回 PixelMap 对象 |
| `addTextObject(text, x, y, style)` | 添加文本内容 | text: 文本内容<br>x, y: 坐标位置<br>style: 文本样式 |

### 5.3 PdfView 组件接口

| 属性名称 | 类型 | 功能描述 |
|---------|------|---------|
| `controller` | PdfController | PdfView 控制器 |
| `pageFit` | PageFit | 页面适配模式 (FIT_WIDTH 等) |
| `showScroll` | boolean | 是否显示滚动条 |

---

## 六、关键技术点

### 6.1 文件沙盒机制
应用通过 `context.filesDir` 获取沙盒目录，将 PDF 文件复制到沙盒中进行操作，确保文件访问权限。

### 6.2 资源文件处理
使用 `context.resourceManager.getRawFileContentSync()` 读取应用资源文件，然后写入沙盒目录。

### 6.3 文件选择器
通过 `picker.DocumentViewPicker` 实现设备本地文件选择功能，支持过滤 PDF 文件类型。

### 6.4 图像显示
使用 `image.PixelMap` 对象配合 `Image` 组件显示 PDF 页面内容。

### 6.5 字体管理
通过 `getUIContext().getFont()` 获取系统字体列表，用于 PDF 文字添加功能。

---

## 七、使用流程

### 7.1 打开本地 PDF 文件
1. 点击"打开电脑里的PDF文件"按钮
2. 使用文件选择器选择 PDF 文件
3. 文件复制到沙盒目录
4. 跳转到 PDFPreview 页面进行预览和编辑

### 7.2 打开资源 PDF 文件
1. 点击"打开资源PDF文件"按钮
2. 从应用资源目录读取预置 PDF
3. 复制到沙盒目录
4. 跳转到 PDFPreview 页面

### 7.3 PDF 编辑操作
1. 在 PDFPreview 页面加载 PDF
2. 使用上一页/下一页导航
3. 点击"添加示例文字"在当前页添加文本
4. 点击"保存文件"保存编辑结果
5. 点击"PDF转图片"将 PDF 转换为图片

---

## 八、依赖与约束

### 8.1 核心依赖
- **@kit.PDFKit**: PDF 服务核心模块
- **@kit.CoreFileKit**: 文件操作模块
- **@kit.ImageKit**: 图像处理模块
- **@kit.ArkUI**: UI 框架模块
- **@kit.AbilityKit**: Ability 框架模块
- **@kit.PerformanceAnalysisKit**: 性能分析模块
- **@kit.BasicServicesKit**: 基础服务模块

### 8.2 约束与限制
1. **设备类型**: 华为 Phone、Tablet 和 2in1
2. **系统版本**: HarmonyOS NEXT Developer Beta3 及以上
3. **开发工具**: DevEco Studio NEXT Developer Beta3 及以上
4. **SDK 版本**: HarmonyOS NEXT Developer Beta3 SDK 及以上
5. **PDF 转图片限制**: 页面数超过 20 页的 PDF 不建议转换

### 8.3 权限要求
- 无特殊权限要求

---

## 九、项目特色

1. **完整的 PDF 操作能力**: 支持查看、编辑、转换等多种操作
2. **多种打开方式**: 支持本地文件、资源文件、组件预览三种方式
3. **用户友好的界面**: 提供清晰的导航和操作按钮
4. **错误处理完善**: 完整的异常捕获和用户提示
5. **性能优化**: 文件沙盒机制确保访问效率
6. **国际化支持**: 提供中英文资源文件

---

## 十、总结

本工程是一个完整的 HarmonyOS PDF 应用示例，展示了 PDFKit 的核心能力。通过三个主要页面实现了从文件选择、预览编辑到组件展示的完整流程。代码结构清晰，注释完善，是学习 HarmonyOS PDF 开发的优秀参考项目。
