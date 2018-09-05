"""
动态规划
定义合法的标识符：数字0-9组成的字符串（可以包含多个前导0）
合法的表达式：
1.若X为合法的标识符，则X为合法的表达式
2.若X为合法的表达式，则（X）为合法的表达式
3.若X和Y均为合法的表达式，则X+Y，X-Y均为合法的表达式

如，1，100，1+2， (10), 1-(3-2)为合法的表达式
(, -1, 1+-2为不合法的表达式

给定长度n，求长为n的合法表达式的数目。输出结果对1000000007取模的余数即可

输入：整数n
输出：长为n的合法表达式的数目对1000000007取模的余数

示例
input：
1
output：
10
"""


