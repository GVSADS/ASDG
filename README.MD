# ASDG - A Scientific DDoS Gun Tool

### This project is currently under development

![Python](https://img.shields.io/badge/Python-3.7+-blue?logo=python)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green)
![License](https://img.shields.io/badge/License-MIT-orange)

ASDG ("A Scientific DDoS Gun Tool") is a network stress testing tool developed with Python Tkinter, featuring a VS Code-inspired dark UI design that provides intuitive proxy training and attack simulation capabilities.

## Key Features

- 🎨 **Modern UI Interface** - Dark theme with sidebar navigation
- 🔍 **Proxy IP Training System** - Batch validation of proxy IP availability with visual results
- ⚡ **Multi-threaded Attack Simulation** - Supports GET/POST/UDP/ICMP and other attack methods
- 📊 **Real-time Monitoring** - Graphical display of attack progress and proxy validation status
- 📁 **Data Import/Export** - Supports saving and loading proxy lists and attack results

## Installation

1. Ensure Python 3.7+ is installed (3.12.0 recommended)
```bash
python --version
```

2. Clone repository and install dependencies
```bash
git clone https://github.com/yourusername/ASDG.git
cd ASDG
pip install -r requirements.txt
```

3. Run the application
```bash
python ASDG.py
```

## User Guide

### Proxy Training Mode

1. Click the `P` button on the left sidebar to switch to Proxy Training view
2. Click "Select File" to import IP list (one IP:Port per line)
3. Set test domain and timeout (default: example.com)
4. Click "Start Training" to validate proxy availability
5. Export valid proxy list after validation completes

### Attack Simulation Mode

1. Click the `G` button on the left sidebar to switch to Attack Panel
2. Enter target URL/IP address
3. Select proxy dataset and target site dataset
4. Configure attack parameters:
   - Thread count (1-1000)
   - Request method (GET/POST/UDP/ICMP)
   - Attack speed (Slow/Medium/Fast/Extreme)
5. Click "Charging... Ready to Fire!" to begin simulated attack

### Settings

Click the gear icon in the bottom left to adjust:
- UI theme (Dark/Light/System)
- Font size
- Editor preferences

## Important Notes

⚠️ **This tool is for legal security testing and educational purposes only**  
⚠️ Unauthorized DDoS testing against websites is illegal  
⚠️ Users assume all legal responsibility  

## Contribution Guidelines

We welcome issues and pull requests! Suggested improvements:
- Add more proxy validation methods
- Implement attack logging functionality
- Optimize multi-threading performance

## License

MIT License - See LICENSE file in the project

---

# ASDG - 某科学的DDOS炮工具

### 本项目暂未完成

![Python](https://img.shields.io/badge/Python-3.7+-blue?logo=python)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green)
![License](https://img.shields.io/badge/License-MIT-orange)

ASDG（某科学的DDOS炮）是一款基于Python Tkinter开发的网络压力测试工具，采用VS Code风格的深色UI设计，提供直观的代理训练和攻击模拟功能。

## 功能特性

- 🎨 **现代化UI界面** - VS Code风格的深色主题，带侧边栏导航
- 🔍 **代理IP训练系统** - 批量验证代理IP可用性并可视化结果
- ⚡ **多线程攻击模拟** - 支持GET/POST/UDP/ICMP等多种攻击方式
- 📊 **实时状态监控** - 图形化显示攻击进度和代理验证状态
- 📁 **数据导入导出** - 支持代理列表和攻击结果的保存与加载

## 安装方法

1. 确保已安装Python 3.7+ (推荐使用3.12.0)
```bash
python --version
```

2. 克隆仓库并安装依赖
```bash
git clone https://github.com/yourusername/ASDG.git
cd ASDG
pip install -r requirements.txt
```

3. 运行应用程序
```bash
python ASDG.py
```

## 使用指南

### 代理训练模式

1. 点击左侧`P`按钮切换到代理训练视图
2. 点击"选择文件"导入IP列表（每行一个IP:Port）
3. 设置测试域名和超时时间（默认example.com）
4. 点击"开始训练"验证代理可用性
5. 验证完成后可导出有效代理列表

### 攻击模拟模式

1. 点击左侧`G`按钮切换到攻击面板
2. 输入目标URL/IP地址
3. 选择代理数据集和攻击站点数据集
4. 配置攻击参数：
   - 线程数（1-1000）
   - 请求方法（GET/POST/UDP/ICMP）
   - 攻击速度（慢速/中速/快速/极速）
5. 点击"充能中...准备发射!"开始模拟攻击

### 设置选项

点击左下角齿轮图标可调整：
- 界面主题（深色/浅色/系统）
- 字体大小
- 编辑器偏好设置

## 注意事项

⚠️ **本工具仅用于合法安全测试和教育目的**  
⚠️ 未经授权对网站进行DDoS测试是违法行为  
⚠️ 使用者需自行承担所有法律责任  

## 贡献指南

欢迎提交Issue和Pull Request！建议改进方向：
- 添加更多代理验证方式
- 实现攻击日志记录功能
- 优化多线程处理性能

## 许可证

MIT License - 详见项目内LICENSE文件