@[toc](Pwn学习笔记-持续更新)
# 第一节：基本命令
| 命令|介绍 |
| ---- | ---- | 
| readelf | 查看elf |
|nm| |
hexdump|查看十六进制
strings|
ldd|查看库函数的位置
objdump|反编译成汇编   **objdump [-d] [file] [-M] [intel]**  查看intel下的汇编
gcc |[-S] 直接编译成汇编代码

# 第二节：gdb
gdb命令 | 介绍
--|--
i|i r :查看寄存器
b | 下断点
d | 删除断点
disable | 断点失效 disable b [id]
enable | 断点生效 enable b [id]  
**rip**|存放当前的执行的指令的地址
rsp | 存放当前栈帧的栈顶地址
rbp | 存放当前栈帧的栈底地址
rax|通用寄存器-保存函数返回值
disass | 显示汇编代码
lea | load effective adderss  现在已经不用lea去取有效地址了
lea rax,[rbp-0x18] | rax=rbp-0x18  ==优点:opcode比较短==
xor ebx.ebx | 使ebx=0
movzx | movzx eax,BYTE PTR [rbp-0x10]:把rbp-0x10地址中存放的数据放入eax中
**cmp** | JCC指令 满足一定条件跳转
cmp al,0x61 | 相当于执行了 sub al,0x61 但是不保存减法之后的数据
ni | 步入
si | 强制步入
finish | 步出
