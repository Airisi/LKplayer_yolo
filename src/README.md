

# Conda 环境导出与导入说明

本项目使用 Conda 管理 Python 环境，包含 YOLO / PyQt5 / OpenCV 等依赖。



# 一、环境导出（Export）

## 1. 导出完整环境（推荐）

```bash
conda env export > env/environment.yml
````

说明：

* 包含所有 conda + pip 依赖
* 包含 Python 版本
* 可完整复现环境

---

## 2. 更干净的导出（推荐用于跨机器）

```bash
conda env export --no-builds > env/environment.yml
```

说明：

* 去除平台相关 build 信息
* 更适合不同电脑使用

---

## 3. 仅导出手动安装依赖（轻量）

```bash
conda env export --from-history > env/environment.yml
```

说明：

* 只记录手动安装的包
* 不包含依赖树

---

## 4. pip 依赖导出（可选）

```bash
pip freeze > env/requirements.txt
```

---

# 二、环境导入（Import）

## 1. 创建新环境

```bash
conda env create -f env/environment.yml
```

---

## 2. 激活环境

```bash
conda activate <env_name>
```

例如：

```bash
conda activate pytorch
```

---

## 3. 安装 pip 依赖（如果存在）

```bash
pip install -r env/requirements.txt
```

---

# 三、查看当前环境

## 查看所有环境

```bash
conda env list
```

## 查看当前环境包

```bash
conda list
```

---

# 四、环境删除（可选）

```bash
conda remove -n <env_name> --all
```

---

# 五、推荐使用流程

## 初始化环境

```bash
conda create -n dev python=3.10
conda activate dev
```

## 安装依赖

```bash
pip install -r env/requirements.txt
```

或

```bash
conda install numpy opencv
```

---

# 六、注意事项

1. 不建议手动修改 environment.yml
2. 不同机器建议使用 `--no-builds`
3. conda 和 pip 不要重复安装同一个包
4. CUDA / PyTorch 版本需保持一致

---

# 七、常见问题

## 1. 创建失败

检查 Python 版本是否冲突

## 2. 依赖缺失

补充执行：

```bash
pip install -r env/requirements.txt
```

## 3. 环境过大

使用：

```bash
conda env export --from-history > env/environment.yml
```
