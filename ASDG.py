#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ASDG (A Scientific DDoS Gun Tool) - Network Stress Testing Utility
==================================================================

File: ASDG.py
Author: WYT
Version: 1.0.0
License: MIT
Description: Python-based network testing tool with VS Code-style dark UI
             featuring proxy validation and multi-threaded testing capabilities.

Important Notice:
⚠️ For LEGAL security testing and educational purposes ONLY
⚠️ Unauthorized network testing is illegal
⚠️ Users assume full legal responsibility
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import threading
import time

class ApplicationMainWindow(tk.Tk):
    """主应用程序窗口类"""
    
    def __init__(self):
        super().__init__()
        self.title("ASDG \"A SCIENTIFIC DDOS GUN TOOL\" 某科学的DDOS炮")
        self.state("zoomed")
        self.configure(bg="#1e1e1e")
        
        # 当前活动视图
        self.CurrentView = None
        self.Views = {}  # 存储所有视图
        
        # 设置深色主题
        self.Style = ttk.Style()
        self.Style.theme_use('clam')
        self.ConfigureDarkTheme()
        
        # 创建UI组件
        self.CreateTopMenu()
        self.CreateLeftSidebar()
        self.CreateMainContentFrame()
        
        # 初始化默认视图
        self.SwitchView("AttackPanel")
    
    def ConfigureDarkTheme(self):
        """配置深色主题样式"""
        self.Style.configure('.', background='#252526', foreground='#d4d4d4')
        self.Style.configure('TFrame', background='#1e1e1e')
        self.Style.configure('TButton', 
                           background='#333333', 
                           foreground='#ffffff',
                           borderwidth=0,
                           relief='flat',
                           width=5,
                           padding=5)
        self.Style.configure('TLabel', background='#1e1e1e', foreground='#d4d4d4')
        self.Style.configure('TEntry', fieldbackground='#333333', foreground='#ffffff')
        self.Style.configure('TCombobox', fieldbackground='#333333', foreground='#ffffff')
        self.Style.map('TButton', background=[('active', '#3e3e42')])
        self.Style.configure('Active.TButton', background='#3e3e42', foreground='#ffffff')
        
        # 配置Treeview样式
        self.Style.configure('Treeview', 
                           background='#252526', 
                           foreground='#ffffff',
                           fieldbackground='#252526',
                           borderwidth=0)
        self.Style.map('Treeview', background=[('selected', '#3e3e42')])
        
        # 配置菜单样式
        self.Style.configure('TMenubutton', background='#252526', foreground='#d4d4d4')
        self.Style.configure('TMenu', background='#252526', foreground='#d4d4d4')
        
        # IP状态样式
        self.Style.configure('Gray.TFrame', background='#555555')
        self.Style.configure('Gray.TLabel', foreground='white')
        self.Style.configure('Green.TFrame', background='#44aa44')
        self.Style.configure('Green.TLabel', foreground='white')
        self.Style.configure('Red.TFrame', background='#aa4444')
        self.Style.configure('Red.TLabel', foreground='white')
        
        # 自定义Spinbox样式
        self.Style.configure('TSpinbox', 
                           fieldbackground='#333333', 
                           foreground='#ffffff',
                           background='#333333',
                           bordercolor='#444444',
                           arrowcolor='#ffffff',
                           arrowsize=12,
                           arrowpadding=5)
        self.Style.map('TSpinbox',
                      background=[('active', '#3e3e42')],
                      fieldbackground=[('active', '#3e3e42')])
    
    def CreateTopMenu(self):
        """创建顶部菜单栏"""
        MenuBar = tk.Menu(self, bg="#252526", fg="#d4d4d4", bd=0)
        
        # 文件菜单
        FileMenu = tk.Menu(MenuBar, tearoff=0, bg="#252526", fg="#d4d4d4", bd=0)
        FileMenu.add_command(label="新建", command=lambda: None)
        FileMenu.add_command(label="打开", command=lambda: None)
        FileMenu.add_separator()
        FileMenu.add_command(label="退出", command=self.quit)
        MenuBar.add_cascade(label="文件", menu=FileMenu)
        
        # 编辑菜单
        EditMenu = tk.Menu(MenuBar, tearoff=0, bg="#252526", fg="#d4d4d4", bd=0)
        EditMenu.add_command(label="剪切", command=lambda: None)
        EditMenu.add_command(label="复制", command=lambda: None)
        EditMenu.add_command(label="粘贴", command=lambda: None)
        MenuBar.add_cascade(label="编辑", menu=EditMenu)
        
        # 视图菜单
        ViewMenu = tk.Menu(MenuBar, tearoff=0, bg="#252526", fg="#d4d4d4", bd=0)
        ViewMenu.add_command(label="攻击面板", command=lambda: self.SwitchView("AttackPanel"))
        ViewMenu.add_command(label="代理训练", command=lambda: self.SwitchView("ProxyTrain"))
        MenuBar.add_cascade(label="视图", menu=ViewMenu)
        
        # 帮助菜单
        HelpMenu = tk.Menu(MenuBar, tearoff=0, bg="#252526", fg="#d4d4d4", bd=0)
        HelpMenu.add_command(label="关于", command=self.ShowAbout)
        MenuBar.add_cascade(label="帮助", menu=HelpMenu)
        
        self.config(menu=MenuBar)
    
    def CreateLeftSidebar(self):
        """创建左侧VS Code风格菜单栏"""
        self.LeftFrame = ttk.Frame(self, width=50, style='TFrame')
        self.LeftFrame.pack(side="left", fill="y")
        self.LeftFrame.configure(style='Dark.TFrame')
        self.Style.configure('Dark.TFrame', background='#181818')  # 更深的背景
        
        # 菜单按钮
        self.MenuButtons = {}
        Buttons = [
            ("AttackPanel", "G"),  # 攻击面板
            ("ProxyTrain",  "P"),  # 代理训练
        ]
        
        for Text, Icon in Buttons:
            Btn = ttk.Button(
                self.LeftFrame, 
                text=Icon, 
                style='TButton',
                command=lambda T=Text: self.SwitchView(T)
            )
            Btn.pack(pady=5, padx=5, ipadx=5, ipady=5)
            self.MenuButtons[Text] = Btn
        
        # 底部设置按钮
        SettingsBtn = ttk.Button(
            self.LeftFrame, 
            text="⚙", 
            style='TButton',
            command=lambda: self.SwitchView("Settings")
        )
        SettingsBtn.pack(side="bottom", pady=5, padx=5, ipadx=5, ipady=5)
        self.MenuButtons["Settings"] = SettingsBtn
    
    def CreateMainContentFrame(self):
        """创建主内容区域容器"""
        self.MainFrame = ttk.Frame(self, style='TFrame')
        self.MainFrame.pack(side="right", fill="both", expand=True)
        
        # 创建所有视图但不立即显示
        self.CreateAttackPanelView()
        self.CreateProxyTrainView()
        self.CreateSettingsView()
    
    def SwitchView(self, ViewName):
        """切换视图"""
        # 更新按钮状态
        for Name, Btn in self.MenuButtons.items():
            if Name == ViewName:
                Btn.configure(style='Active.TButton')
            else:
                Btn.configure(style='TButton')
        
        # 隐藏当前视图
        if self.CurrentView:
            self.CurrentView.pack_forget()
        
        # 显示新视图
        self.CurrentView = self.Views[ViewName]
        self.CurrentView.pack(fill="both", expand=True)
        
        # 更新窗口标题
        self.title(f"ASDG \"A SCIENTIFIC DDOS GUN TOOL\" 某科学的DDOS炮 - {ViewName}")
    
    def CreateAttackPanelView(self):
        """创建攻击面板视图"""
        Frame = ttk.Frame(self.MainFrame, style='TFrame')
        
        # 目标区域
        TargetFrame = ttk.LabelFrame(Frame, text="目标配置", style='TFrame')
        TargetFrame.pack(fill="x", padx=10, pady=10)
        
        ttk.Label(TargetFrame, text="目标URL/IP:").pack(side="left", padx=5)
        self.TargetEntry = ttk.Entry(TargetFrame, width=40)
        self.TargetEntry.pack(side="left", padx=5, fill="x", expand=True)
        
        ttk.Button(TargetFrame, text="锁定目标", style='TButton').pack(side="left", padx=5)
        
        # 代理数据集配置
        ProxyFrame = ttk.LabelFrame(Frame, text="代理数据集", style='TFrame')
        ProxyFrame.pack(fill="x", padx=10, pady=10)
        
        self.ProxyCombopicker = self._create_combopicker(
            parent=ProxyFrame,
            options=['公共代理池', '私有代理池1', '私有代理池2', 'Tor网络', '自定义代理列表'],
            default_text="选择代理数据集"
        )
        self.ProxyCombopicker.pack(fill="x", padx=5, pady=2)
        
        # 攻击站点数据集配置
        SiteFrame = ttk.LabelFrame(Frame, text="攻击站点数据集", style='TFrame')
        SiteFrame.pack(fill="x", padx=10, pady=10)
        
        self.SiteCombopicker = self._create_combopicker(
            parent=SiteFrame,
            options=['常用网站TOP100', '政府机构站点', '教育机构站点', '电商平台站点', '金融支付站点', '自定义站点列表'],
            default_text="选择攻击站点"
        )
        self.SiteCombopicker.pack(fill="x", padx=5, pady=2)
        
        # 攻击参数区域
        AttackFrame = ttk.LabelFrame(Frame, text="攻击参数配置", style='TFrame')
        AttackFrame.pack(fill="x", padx=10, pady=10)
        
        # 线程数
        ttk.Label(AttackFrame, text="线程数:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.ThreadsSpin = ttk.Spinbox(AttackFrame, from_=1, to=1000, width=5)
        self.ThreadsSpin.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        
        # 请求方法
        ttk.Label(AttackFrame, text="方法:").grid(row=0, column=2, padx=5, pady=5, sticky="e")
        self.MethodCombo = ttk.Combobox(AttackFrame, values=["GET", "POST", "UDP", "ICMP"], width=5)
        self.MethodCombo.grid(row=0, column=3, padx=5, pady=5, sticky="w")
        self.MethodCombo.current(0)
        
        # 速度限制
        ttk.Label(AttackFrame, text="速度:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.SpeedCombo = ttk.Combobox(AttackFrame, values=["慢速", "中速", "快速", "极速"], width=8)
        self.SpeedCombo.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        self.SpeedCombo.current(1)
        
        # 攻击按钮
        self.AttackBtn = ttk.Button(AttackFrame, text="充能中...准备发射!", style='TButton')
        self.AttackBtn.grid(row=1, column=2, columnspan=2, padx=5, pady=5, sticky="ew")
        
        # 状态区域
        StatusFrame = ttk.LabelFrame(Frame, text="攻击状态监控", style='TFrame')
        StatusFrame.pack(fill="both", expand=True, padx=10, pady=10)
        
        self.StatusText = tk.Text(StatusFrame, bg="#252526", fg="#d4d4d4", insertbackground="#d4d4d4")
        self.StatusText.pack(fill="both", expand=True, padx=5, pady=5)
        self.StatusText.insert("end", "攻击面板已就绪...\n")
        
        # 底部控制按钮
        ControlFrame = ttk.Frame(Frame, style='TFrame')
        ControlFrame.pack(fill="x", padx=10, pady=10)
        
        ttk.Button(ControlFrame, text="停止攻击", style='TButton').pack(side="right", padx=5)
        ttk.Button(ControlFrame, text="暂停攻击", style='TButton').pack(side="right", padx=5)
        
        self.Views["AttackPanel"] = Frame

    def _create_combopicker(self, parent, options, default_text="请选择"):
        """创建可靠的多选下拉框组件"""
        container = ttk.Frame(parent)
        
        # 状态变量
        container.selected_var = tk.StringVar(value=default_text)
        container.is_dropped = False
        container.options = options
        
        # 主控件框架（Entry + Button）
        header_frame = ttk.Frame(container)
        header_frame.pack(fill="x")
        
        # 显示框
        entry = ttk.Entry(
            header_frame,
            textvariable=container.selected_var,
            state="readonly",
            style='TEntry'
        )
        entry.pack(side="left", fill="x", expand=True, padx=(0, 5))
        
        # 下拉按钮
        btn = ttk.Button(
            header_frame,
            text="▼",
            width=3,
            command=lambda: self._toggle_combopicker(container)
        )
        btn.pack(side="right")
        
        # Listbox容器（关键修正：必须作为container的子组件）
        container.list_frame = ttk.Frame(container)
        container.listbox = tk.Listbox(
            container.list_frame,
            selectmode="multiple",
            height=5,
            bg="#333333",
            fg="#ffffff",
            exportselection=0,  # 保持选择状态
            selectbackground="#003eff",  # 选中项背景色
            selectforeground="white"     # 选中项文字色
        )
        
        # 添加滚动条
        scrollbar = ttk.Scrollbar(container.list_frame)
        scrollbar.pack(side="right", fill="y")
        container.listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=container.listbox.yview)
        
        container.listbox.pack(fill="both", expand=True)
        
        # 填充选项
        for opt in options:
            container.listbox.insert("end", opt)
        
        # 事件绑定
        container.listbox.bind("<<ListboxSelect>>", 
            lambda e, c=container: self._update_combopicker_selection(c))
        
        return container
    
    def _toggle_combopicker(self, container):
        """控制下拉框显示/隐藏"""
        if container.is_dropped:
            container.list_frame.pack_forget()
        else:
            # 确保listbox显示在container下方
            container.list_frame.pack(fill="x", pady=(2, 0))
            container.listbox.focus_set()
        container.is_dropped = not container.is_dropped
    
    def _update_combopicker_selection(self, container):
        """更新选中值到Entry"""
        selected = [container.options[i] 
                   for i in container.listbox.curselection()]
        container.selected_var.set(", ".join(selected) if selected else "请选择")

    def CreateProxyTrainView(self):
        """创建代理IP训练视图"""
        Frame = ttk.Frame(self.MainFrame, style='TFrame')
        
        # 训练集配置区域
        ConfigFrame = ttk.LabelFrame(Frame, text="训练配置", style='TFrame')
        ConfigFrame.pack(fill="x", padx=10, pady=5)
        
        # 训练集名称
        ttk.Label(ConfigFrame, text="训练集名称:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.TrainingSetName = ttk.Entry(ConfigFrame)
        self.TrainingSetName.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        
        # 测试域名
        ttk.Label(ConfigFrame, text="测试域名:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.TestDomain = ttk.Entry(ConfigFrame)
        self.TestDomain.insert(0, "http://example.com")  # 默认测试域名
        self.TestDomain.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        
        # 超时时间(秒)
        ttk.Label(ConfigFrame, text="超时时间(s):").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.Timeout = ttk.Spinbox(ConfigFrame, from_=1, to=60, width=5)
        self.Timeout.set(5)  # 默认5秒
        self.Timeout.grid(row=2, column=1, padx=5, pady=5, sticky="w")
        
        # 批量导入区域
        ImportFrame = ttk.LabelFrame(Frame, text="批量导入IP", style='TFrame')
        ImportFrame.pack(fill="x", padx=10, pady=5)
        
        self.ProxyFileEntry = ttk.Entry(ImportFrame)
        self.ProxyFileEntry.pack(side="left", padx=5, fill="x", expand=True)
        
        ttk.Button(
            ImportFrame, 
            text="选择文件", 
            command=self._select_proxy_file
        ).pack(side="left", padx=5)
        
        # 状态统计区域
        StatsFrame = ttk.Frame(Frame, style='TFrame')
        StatsFrame.pack(fill="x", padx=10, pady=5)
        
        self.StatsLabel = ttk.Label(
            StatsFrame, 
            text="就绪 | 总数: 0 | 未完成: 0 | 成功: 0 | 失败: 0",
            style='TLabel'
        )
        self.StatsLabel.pack(side="left")
        
        # 进度可视化区域
        self.ProgressCanvas = tk.Canvas(Frame, bg="#252526", height=30, highlightthickness=0)
        self.ProgressCanvas.pack(fill="x", padx=10, pady=5)
        
        # IP可视化展示区
        IPContainer = ttk.Frame(Frame)
        IPContainer.pack(fill="both", expand=True, padx=10, pady=5)
        
        self.IPDisplayCanvas = tk.Canvas(IPContainer, bg="#252526", highlightthickness=0)
        self.IPDisplayScrollbar = ttk.Scrollbar(IPContainer, orient="vertical", command=self.IPDisplayCanvas.yview)
        self.IPDisplayFrame = ttk.Frame(self.IPDisplayCanvas, style='TFrame')
        
        self.IPDisplayCanvas.configure(yscrollcommand=self.IPDisplayScrollbar.set)
        self.IPDisplayCanvas.create_window((0, 0), window=self.IPDisplayFrame, anchor="nw")
        
        self.IPDisplayFrame.bind(
            "<Configure>",
            lambda e: self.IPDisplayCanvas.configure(
                scrollregion=self.IPDisplayCanvas.bbox("all")
            )
        )
        
        self.IPDisplayCanvas.pack(side="left", fill="both", expand=True)
        self.IPDisplayScrollbar.pack(side="right", fill="y")
        
        # 控制按钮区
        ControlFrame = ttk.Frame(Frame)
        ControlFrame.pack(fill="x", padx=10, pady=10)
        
        self.StartBtn = ttk.Button(
            ControlFrame,
            text="开始训练",
            command=self._start_proxy_validation
        )
        self.StartBtn.pack(side="left", padx=5)
        
        self.StopBtn = ttk.Button(
            ControlFrame,
            text="停止训练",
            state="disabled",
            command=self._stop_proxy_validation
        )
        self.StopBtn.pack(side="left", padx=5)
        
        self.ExportBtn = ttk.Button(
            ControlFrame,
            text="导出结果",
            state="disabled",
            command=self._export_proxy_results
        )
        self.ExportBtn.pack(side="right", padx=5)
        
        # 状态变量
        self.ProxyIPs = []
        self.ValidIPs = []
        self.InvalidIPs = []
        self.IPBlocks = {}  # 存储IP方块引用
        self.IsValidating = False
        self.ShouldStop = False
        self.TotalIPs = 0
        self.ProcessedIPs = 0
        
        self.Views["ProxyTrain"] = Frame

    def _select_proxy_file(self):
        """选择IP文本文件"""
        filepath = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if filepath:
            self.ProxyFileEntry.delete(0, tk.END)
            self.ProxyFileEntry.insert(0, filepath)
            self._load_proxy_ips(filepath)

    def _load_proxy_ips(self, filepath):
        """异步加载IP列表并创建可视化方块"""
        # 清空现有显示
        for widget in self.IPDisplayFrame.winfo_children():
            widget.destroy()
        
        self.ProxyIPs = []
        self.ValidIPs = []
        self.InvalidIPs = []
        self.IPBlocks = {}
        self.ExportBtn.config(state="disabled")
        self.StartBtn.config(state="disabled")
        self.StopBtn.config(state="disabled")
        self.StatsLabel.config(text="正在加载IP列表...")
        
        # 启动异步加载线程
        load_thread = threading.Thread(
            target=self._async_load_proxy_ips,
            args=(filepath,),
            daemon=True
        )
        load_thread.start()

    def _export_proxy_results(self):
        """导出验证结果"""
        if not self.ValidIPs:
            messagebox.showwarning("警告", "没有有效的IP可以导出")
            return
        
        filepath = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt")]
        )
        
        if filepath:
            with open(filepath, 'w') as f:
                f.write("\n".join(self.ValidIPs))
            
            messagebox.showinfo("导出成功", f"有效IP已导出到:\n{filepath}")

    def _async_load_proxy_ips(self, filepath):
        """异步加载IP列表的实现"""
        try:
            # 读取IP文件
            with open(filepath, 'r', encoding="UTF-8") as f:
                ips = [line.strip() for line in f if line.strip()]
            
            self.TotalIPs = len(ips)
            self.ProcessedIPs = 0
            self.ProxyIPs = ips
            
            # 分批创建UI元素，避免界面卡顿
            batch_size = 100  # 每批处理100个IP
            for i in range(0, len(ips), batch_size):
                if self.ShouldStop:  # 检查是否中止
                    break
                    
                batch = ips[i:i+batch_size]
                self.after(0, self._create_ip_blocks_batch, batch, i, len(ips))
                
                # 更新进度
                self.ProcessedIPs = min(i + batch_size, len(ips))
                self.after(0, self._update_loading_progress)
                
                time.sleep(0.1)  # 稍微延迟，让UI有机会更新
            
            # 加载完成
            self.after(0, self._finish_loading_ips)
        except Exception as e:
            self.after(0, messagebox.showerror, "加载错误", f"加载IP列表时出错: {str(e)}")
            self.after(0, self._reset_loading_state)

    def _create_ip_blocks_batch(self, ip_batch, start_index, total_count):
        """创建一批IP方块"""
        # 计算每行可显示的IP数量（根据窗口宽度）
        canvas_width = self.IPDisplayCanvas.winfo_width() - 20
        if canvas_width < 100:  # 默认值
            canvas_width = 800
        
        ip_width = 150  # 每个IP方块的宽度
        ips_per_row = max(1, canvas_width // ip_width)
        
        # 创建IP方块网格布局
        for i, ip in enumerate(ip_batch):
            row, col = divmod(start_index + i, ips_per_row)
            
            # 创建IP方块框架
            frame = ttk.Frame(
                self.IPDisplayFrame, 
                width=ip_width, 
                height=100,
                style='Gray.TFrame'
            )
            frame.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
            frame.pack_propagate(False)  # 固定大小
            
            # IP地址标签
            label = ttk.Label(
                frame, 
                text=ip, 
                wraplength=ip_width-10,
                style='Gray.TLabel'
            )
            label.pack(pady=5)
            
            # 状态标签
            status = ttk.Label(
                frame,
                text="待验证",
                style='Gray.TLabel'
            )
            status.pack()
            
            self.IPBlocks[ip] = (frame, label, status)
        
        # 配置网格列权重
        for col in range(ips_per_row):
            self.IPDisplayFrame.columnconfigure(col, weight=1)

    def _update_loading_progress(self):
        """更新加载进度显示"""
        self.StatsLabel.config(
            text=f"正在加载... ({self.ProcessedIPs}/{self.TotalIPs}) | 总数: {self.TotalIPs} | 未完成: {self.TotalIPs} | 成功: 0 | 失败: 0"
        )

    def _finish_loading_ips(self):
        """完成IP加载"""
        self.StatsLabel.config(
            text=f"加载完成 | 总数: {self.TotalIPs} | 未完成: {self.TotalIPs} | 成功: 0 | 失败: 0"
        )
        self.StartBtn.config(state="normal")
        self._update_progress_bar()

    def _reset_loading_state(self):
        """重置加载状态"""
        self.StatsLabel.config(text="加载已取消")
        self.StartBtn.config(state="normal")

    def _update_progress_bar(self):
        """更新进度条显示"""
        self.ProgressCanvas.delete("all")
        canvas_width = self.ProgressCanvas.winfo_width()
        if canvas_width < 10 or self.TotalIPs == 0:
            return
        
        # 计算各状态比例
        valid_ratio = len(self.ValidIPs) / self.TotalIPs
        invalid_ratio = len(self.InvalidIPs) / self.TotalIPs
        pending_ratio = 1 - valid_ratio - invalid_ratio
        
        # 绘制进度条
        x = 0
        if valid_ratio > 0:
            width = int(canvas_width * valid_ratio)
            self.ProgressCanvas.create_rectangle(x, 0, x+width, 30, fill="#44aa44", outline="")
            x += width
        
        if invalid_ratio > 0:
            width = int(canvas_width * invalid_ratio)
            self.ProgressCanvas.create_rectangle(x, 0, x+width, 30, fill="#aa4444", outline="")
            x += width
        
        if pending_ratio > 0:
            width = int(canvas_width * pending_ratio)
            self.ProgressCanvas.create_rectangle(x, 0, x+width, 30, fill="#555555", outline="")

    def _stop_proxy_validation(self):
        """停止验证IP有效性"""
        if self.IsValidating:
            self.ShouldStop = True
            self.StatsLabel.config(text=f"正在停止... | 总数: {self.TotalIPs} | 未完成: {self.TotalIPs - len(self.ValidIPs) - len(self.InvalidIPs)} | 成功: {len(self.ValidIPs)} | 失败: {len(self.InvalidIPs)}")

    def _validate_proxy_ips(self, test_domain, timeout):
        """验证IP有效性的线程函数"""
        try:
            for i, ip in enumerate(self.ProxyIPs):
                if self.ShouldStop:  # 检查是否中止
                    break
                
                self.current_ip = ip
                is_valid = self._check_ip_validity(ip, test_domain, timeout)
                
                # 更新UI
                self.after(0, self._update_ip_status, ip, is_valid)
                
                # 记录结果
                if is_valid:
                    self.ValidIPs.append(ip)
                else:
                    self.InvalidIPs.append(ip)
                
                # 更新进度
                self.ProcessedIPs = i + 1
                self.after(0, self._update_validation_progress)
                
            # 验证完成
            self.after(0, self._finish_proxy_validation)
        except Exception as e:
            self.after(0, messagebox.showerror, "验证错误", f"验证过程中出错: {str(e)}")
            self.after(0, self._finish_proxy_validation)

    def _check_ip_validity(self, ip, test_domain, timeout):
        """使用requests检查IP有效性，并记录耗时"""
        try:
            import requests
            from urllib.parse import urlparse
            start_time = time.time()  # 记录开始时间
            
            # 解析测试域名，确保有协议头
            if not test_domain.startswith(('http://', 'https://')):
                test_domain = 'http://' + test_domain
            
            # 设置代理，支持HTTP和HTTPS
            proxies = {
                'http': f'http://{ip}',
                'https': f'http://{ip}'
            }
            
            # 发送测试请求
            response = requests.get(
                test_domain,
                proxies=proxies,
                timeout=timeout,
                headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
                }
            )
            
            # 计算耗时（毫秒）
            elapsed_time = int((time.time() - start_time) * 1000)
            
            # 检查响应状态码
            return (response.status_code == 200, elapsed_time)
            
        except (requests.exceptions.RequestException, ValueError) as e:
            elapsed_time = int((time.time() - start_time) * 1000)
            return (False, elapsed_time)

    def _start_proxy_validation(self):
        """开始验证IP有效性"""
        if self.IsValidating or not self.ProxyIPs:
            return
        
        # 重置状态
        self.IsValidating = True
        self.ShouldStop = False
        self.ValidIPs = []
        self.InvalidIPs = []
        self.ProcessedIPs = 0
        
        # 更新UI状态
        self.StartBtn.config(state="disabled")
        self.StopBtn.config(state="normal")
        self.ExportBtn.config(state="disabled")
        self.StatsLabel.config(
            text=f"训练中... (0/{self.TotalIPs}) | 总数: {self.TotalIPs} | 未完成: {self.TotalIPs} | 成功: 0 | 失败: 0"
        )
        self._update_progress_bar()
        
        # 获取测试参数
        test_domain = self.TestDomain.get()
        timeout = int(self.Timeout.get())
        
        # 创建线程池
        max_threads = min(100, max(5, int(self.Timeout.get())))  # 线程数基于超时时间，最小5，最大100
        self.ValidationThreads = []
        self.IPQueue = list(self.ProxyIPs)  # 待验证IP队列
        self.Lock = threading.Lock()
        
        # 创建验证线程
        for _ in range(max_threads):
            thread = threading.Thread(
                target=self._validate_proxy_ips_thread,
                args=(test_domain, timeout),
                daemon=True
            )
            thread.start()
            self.ValidationThreads.append(thread)

    def _validate_proxy_ips_thread(self, test_domain, timeout):
        """验证IP有效性的线程函数"""
        while True:
            with self.Lock:
                if self.ShouldStop or not self.IPQueue:
                    break
                ip = self.IPQueue.pop(0)
            
            # 验证IP
            is_valid, elapsed_time = self._check_ip_validity(ip, test_domain, timeout)
            
            # 更新结果
            with self.Lock:
                if is_valid:
                    self.ValidIPs.append((ip, elapsed_time))
                else:
                    self.InvalidIPs.append((ip, elapsed_time))
                
                self.ProcessedIPs = len(self.ValidIPs) + len(self.InvalidIPs)
                
                # 更新UI
                self.after(0, self._update_ip_status, ip, is_valid, elapsed_time)
                self.after(0, self._update_validation_progress)
        
        # 检查是否所有线程都完成了
        with self.Lock:
            if all(not t.is_alive() for t in self.ValidationThreads):
                self.after(0, self._finish_proxy_validation)

    def _update_ip_status(self, ip, is_valid, elapsed_time):
        """更新IP状态显示，包括耗时"""
        if ip not in self.IPBlocks:
            return
        
        frame, label, status = self.IPBlocks[ip]
        
        if is_valid:
            frame.config(style='Green.TFrame')
            label.config(style='Green.TLabel')
            status.config(text=f"有效 ({elapsed_time}ms)", style='Green.TLabel')
        else:
            frame.config(style='Red.TFrame')
            label.config(style='Red.TLabel')
            status.config(text=f"无效 ({elapsed_time}ms)", style='Red.TLabel')

    def _update_validation_progress(self):
        """更新验证进度显示"""
        pending = self.TotalIPs - len(self.ValidIPs) - len(self.InvalidIPs)
        self.StatsLabel.config(
            text=f"训练中... ({self.ProcessedIPs}/{self.TotalIPs}) | 总数: {self.TotalIPs} | 未完成: {pending} | 成功: {len(self.ValidIPs)} | 失败: {len(self.InvalidIPs)}"
        )
        self._update_progress_bar()

    def _finish_proxy_validation(self):
        """完成IP验证"""
        self.IsValidating = False
        self.ShouldStop = False
        self.StartBtn.config(state="normal")
        self.StopBtn.config(state="disabled")
        self.ExportBtn.config(state="normal")
        
        # 计算平均响应时间
        avg_time = 0
        if self.ValidIPs:
            avg_time = sum(time for _, time in self.ValidIPs) / len(self.ValidIPs)
        
        # 更新最终状态
        pending = self.TotalIPs - len(self.ValidIPs) - len(self.InvalidIPs)
        self.StatsLabel.config(
            text=f"训练完成 | 总数: {self.TotalIPs} | 未完成: {pending} | 成功: {len(self.ValidIPs)} | 失败: {len(self.InvalidIPs)} | 平均耗时: {int(avg_time)}ms"
        )
        self._update_progress_bar()
        
        # 显示统计信息
        if not self.ShouldStop:
            messagebox.showinfo(
                "训练完成",
                f"训练完成！\n"
                f"有效IP: {len(self.ValidIPs)}个\n"
                f"无效IP: {len(self.InvalidIPs)}个\n"
                f"平均响应时间: {int(avg_time)}ms\n"
            )

    def _export_proxy_results(self):
        """导出验证结果（包含耗时）"""
        if not self.ValidIPs:
            messagebox.showwarning("警告", "没有有效的IP可以导出")
            return
        
        filepath = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt")]
        )
        
        if filepath:
            with open(filepath, 'w') as f:
                # 按响应时间排序（从快到慢）
                sorted_ips = sorted(self.ValidIPs, key=lambda x: x[1])
                f.write("IP地址:端口\t响应时间(ms)\n")
                f.write("\n".join([f"{ip}\t{time}" for ip, time in sorted_ips]))
            
            messagebox.showinfo("导出成功", f"有效IP已导出到:\n{filepath}")

    def CreateSettingsView(self):
        """创建设置视图"""
        self.Style.configure('Settings.TNotebook.Tab', 
                           background='#252526',
                           foreground='white')
        self.Style.map('Settings.TNotebook.Tab',
                     background=[('selected', '#3e3e42')],
                     foreground=[('selected', 'white')])
        
        Frame = ttk.Frame(self.MainFrame, style='TFrame')
        SettingsFrame = ttk.LabelFrame(Frame, text="设置", style='TFrame')
        SettingsFrame.pack(fill='both', expand=True, padx=10, pady=10)
        
        # 使用自定义样式
        Notebook = ttk.Notebook(SettingsFrame, style='Settings.TNotebook')
        
        # 常规设置
        GeneralFrame = ttk.Frame(Notebook, style='TFrame')
        
        ttk.Label(GeneralFrame, text="主题:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        ThemeCombo = ttk.Combobox(GeneralFrame, values=["深色", "浅色", "系统"])
        ThemeCombo.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        ThemeCombo.current(0)
        
        ttk.Label(GeneralFrame, text="字体大小:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        FontSpin = ttk.Spinbox(GeneralFrame, from_=8, to=24)
        FontSpin.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        FontSpin.set(12)
        
        Notebook.add(GeneralFrame, text="常规")
        
        # 编辑器设置
        EditorFrame = ttk.Frame(Notebook, style='TFrame')
        
        ttk.Label(EditorFrame, text="制表符大小:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        TabSpin = ttk.Spinbox(EditorFrame, from_=1, to=8)
        TabSpin.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        TabSpin.set(4)
        
        ttk.Label(EditorFrame, text="自动换行:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        WrapCombo = ttk.Combobox(EditorFrame, values=["关闭", "开启", "按单词"])
        WrapCombo.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        WrapCombo.current(0)
        
        Notebook.add(EditorFrame, text="编辑器")
        
        # 保存按钮
        SaveFrame = ttk.Frame(SettingsFrame, style='TFrame')
        SaveFrame.pack(fill="x", padx=10, pady=10)
        
        ttk.Button(SaveFrame, text="保存设置", style='TButton').pack(side="right", padx=5)
        
        Notebook.pack(fill="both", expand=True, padx=5, pady=5)
        
        self.Views["Settings"] = Frame
    
    def ShowAbout(self):
        """显示关于对话框"""
        messagebox.showinfo("关于", "网络工具 - LOIC风格\n版本 1.0\n\n使用Python Tkinter创建")

class NetworkToolApplication:
    """应用程序入口类"""
    
    @staticmethod
    def Run():
        """运行应用程序"""
        App = ApplicationMainWindow()
        App.mainloop()

if __name__ == "__main__":
    NetworkToolApplication.Run()