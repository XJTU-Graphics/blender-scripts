# Blender Scripts for Rendering Point Clouds and Meshes

这里是一些用于自动渲染点云和 Mesh 的 Python 脚本，用来在实验过程中观察输出结果，或者在写论文时渲染结果图。

## 工作环境

从 Blender 3.4 开始，Blender 开发者在 PyPI 上创建了一个叫做 `bpy` 的包，只要安装这个包就可以直接在外部 Python 开发环境中编写 Blender 脚本，并且直接用执行一般 Python 脚本的命令执行它们而无需显式调用 Blender 。由这个包提供的 Blender 环境是独立于图形界面版 Blender 的，二者可以共存而互不影响。这个包在 PyPI 上的页面如下：

[bpy · PyPI](https://pypi.org/project/bpy/)

目前本项目中的脚本在 `bpy 3.6` 环境下验证可用。

注意：`bpy` 这个包如同完整的 Blender 一样依赖于特定的 Python 版本，例如 `bpy 3.6` 必须是 Python 3.10 才能安装。因此，建议用 pyenv / virtualenv / conda 等工具安装并管理多版本 Python 。

## 使用方法

凡是可以直接执行的脚本中都有 `if __name__ == '__main__'` 的部分，而其他的文件里是一些通用的功能。例如要执行 `render_mesh.py` 渲染 Mesh ，只需要直接调用

```shell
$ python3 render_mesh.py
```

即可。

## 编写方式

Blender 中所有的图形化操作都有相应的 Python API ，但编写脚本和编写插件的思路并不完全一样。总体上来说，Python 程序访问 Blender 数据或进行操作有两种模式：

- 类似 GUI 的选择-操作逻辑：先用一些 API 选中要操作的对象（如 Object / Material / Collection 等），然后通过 `bpy.context` 系列 API 访问当前被选中的对象、通过 `bpy.ops` 系列 API 操纵当前被选中的对象。
- 更加程序化的“属性集合”：Blender 中有一种抽象的类型 `bpy_prop_collection` ，同时支持下标索引和键值对两种访问方式。所有的集合、物体、形状、材质等信息全部存储在 `bpy.data` 中，通过访问其中的若干个 `bpy_prop_collection` 对象来查改数据，类似于访问一个大型的 Python Dict 。这种方法不需要来回切换选择的对象，更像是批处理而不是交互。

我更偏好使用第二种方式操作数据，因为我要用脚本实现的正是一些批处理操作。少数情况下，直接用 `bpy.ops` 修改一些全局设定确实更方便，我也就不再专门操作 bpy.data 了。

## 代码风格

对于处理实验结果的脚本而言，文件 I/O 不构成性能瓶颈，所以这里的脚本都提倡使用 `pathlib` 代替 `os.path` 模块。否则漫天乱飞的字符串连接和切片操作非常不利于阅读，也非常不利于调试和修改。

在传递参数、进行循环等重复操作时，多使用 Dict 和 `itertools` 配合生成器、迭代器，可以用简洁易懂的代码生成各种 case ，避免反复粘贴相似的代码。
