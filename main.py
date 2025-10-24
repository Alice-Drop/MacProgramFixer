import os
import time
from tkinter import messagebox as msgbox
from tkinter import filedialog

PROJECT_NAME = "Mac软件无法运行修复工具 - by AliceDrop"
VERSION = "0.1"

class Commands:
    enable_third_party_source = "sudo spctl --master-disable"
    remove_ext_attr = "sudo xattr -rd com.apple.quarantine "

def main():
    print(f"{PROJECT_NAME} v{VERSION}")
    print()
    print("1.开启任何来源，可解决大多数软件无法运行的问题。\n  用于修复 “Apple无法验证“XXX.app”是否包含可能危害Mac安全或泄漏隐私的恶意软件。” 的问题。")
    print("\n如果使用了以上方法仍然无法运行，则根据提示使用下面的修复工具：")
    print("2.修复“xxx已损坏，无法打开。您应将它移到废纸篓。”问题，也就是隔离附加属性问题。")
    print("3.修复“无法打开“ XXX”，因为无法确定开发者的身份。”")
    print()
    print("其他工具：\na:查看文件是否有异常附加属性")

    choice = input("\n输入需要的操作：")
    print()
    if choice == "1":
        os.system(Commands.enable_third_party_source)
    elif choice == "2":
        print("请选择需要修复的软件...")
        time.sleep(1)
        app_path = filedialog.askopenfilename(filetypes=[("应用程序", "app"), ("任意文件", "*")], initialdir="/Applications/")
        if len(app_path) == 0:
            input("未选择文件，按回车退出程序...")
            exit()
        os.system(Commands.remove_ext_attr + app_path)
        print("修复完成！")
    elif choice == "3":
        pass

if __name__ == "__main__":
    main()
