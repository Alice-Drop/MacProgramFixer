import os
import time
import tkinter as tk
from tkinter import filedialog, messagebox

PROJECT_NAME = "Mac软件无法运行修复工具 - by AliceDrop"
PROJECT_HREF = "https://github.com/Alice-Drop/MacProgramFixer"
VERSION = "v0.2"

class Commands:
    enable_third_party_source = "spctl --master-disable"
    remove_ext_attr = "xattr -rd com.apple.quarantine "

def run_as_admin(command: str):
    """使用管理员权限执行命令（通过 osascript）"""
    safe_command = command.replace('"', '\\"')
    osascript = f"osascript -e 'do shell script \"{safe_command}\" with administrator privileges'"
    os.system(osascript)

def enable_any_source():
    if messagebox.askyesno("确认", "是否要开启“任何来源”？这将允许安装所有来源的应用。"):
        run_as_admin(Commands.enable_third_party_source)
        messagebox.showinfo("完成", "“任何来源”已开启！")
    else:
        messagebox.showinfo("取消", "操作已取消。")

def fix_damaged_app():
    messagebox.showinfo("提示", "请选择需要修复的应用程序 (.app)")
    app_path = filedialog.askopenfilename(
        title="选择要修复的 .app",
        filetypes=[("所有文件", "*"),("应用程序", "*.app")],
        initialdir="/Applications/"
    )
    if not app_path:
        return
    run_as_admin(Commands.remove_ext_attr + f'"{app_path}"')
    messagebox.showinfo("完成", f"已移除隔离属性，修复完成：\n{app_path}")

def check_attr():
    messagebox.showinfo("提示", "请选择要检查的文件或应用程序")
    app_path = filedialog.askopenfilename(
        title="选择文件",
        filetypes=[("所有文件", "*")],
        initialdir="/Applications/"
    )
    if not app_path:
        return
    os.system(f"xattr -l '{app_path}' > /tmp/xattr_check.txt")
    with open("/tmp/xattr_check.txt", "r", encoding="UTF-8") as f:
        content = f.read()
    if content.strip():
        messagebox.showinfo("结果", f"该文件有以下附加属性：\n\n{content}")
    else:
        messagebox.showinfo("结果", "该文件没有异常附加属性。")

def fix_undefined_developer():
    messagebox.showinfo("提示", "此问题是签名问题，通过 “1.开启任何来源” 即可解决。\n如仍无法打开，请尝试右键→打开。")

def open_project_page():
    os.system("open " + PROJECT_HREF)

def main():
    root = tk.Tk()
    root.title(PROJECT_NAME)
    root.geometry("480x420")
    root.resizable(False, False)

    tk.Label(root, text=PROJECT_NAME, font=("Helvetica", 16, "bold")).pack(pady=10)
    tk.Label(root, text=f"版本 {VERSION}", fg="gray").pack(pady=2)

    # 功能按钮
    tk.Button(root, text="1. 开启任何来源（解决 Apple 无法验证问题）", width=40, command=enable_any_source).pack(pady=10)
    tk.Button(root, text="2. 修复“xxx已损坏，无法打开”", width=40, command=fix_damaged_app).pack(pady=10)
    tk.Button(root, text="3. 修复“无法确定开发者身份”", width=40, command=fix_undefined_developer).pack(pady=10)
    tk.Button(root, text="检查文件附加属性", width=40, command=check_attr).pack(pady=10)

    tk.Label(root, text="使用须知：本工具仅用于修复合法软件在 Mac 上的运行限制。\n请勿用于绕过安全机制或运行不可信软件。", wraplength=420, justify="center", fg="gray").pack(pady=20)
    tk.Button(root, text="Github",underline=True, command=open_project_page).pack()
    root.mainloop()

    # todo: 未来加入自动检查，一键修复。

if __name__ == "__main__":
    main()
