# Handwrite

一个基于 LaTeX、TikZ 和 XeLaTeX 的练字纸素材与生成工具集合。项目包含英文单词、句子和字母练习页生成脚本，以及英文空白练字纸、中文田字格、字体和示例 PDF。

## 项目内容

- `GenHandwritting_word.py`：读取 `words.txt`，生成英文单词练习 PDF。
- `GenHandwritting_sentence.py`：读取 `chapter-101.txt`，生成英文句子练习 PDF。
- `LETTERhand.tex`：英文字母描红练习模板。
- `EnglishPaper/`：横向、纵向及带插图框的英文练字纸模板。
- `ChinesePaper/`：中文田字格模板。
- `font/`、`cursive/`：模板和脚本使用或参考的字体资源。
- `*.txt`：单词、句子和章节练习文本。
- `*.pdf`：已生成的练习纸示例。

## 环境要求

- XeLaTeX，以及模板所需的 LaTeX 宏包：
  - `fontspec`
  - `tikz`
  - `geometry`
  - `lineno`
  - `setspace`
  - `ragged2e`
  - `xeCJK`（中文模板）
  - `dashrule`、`forloop`（部分英文模板）
- 模板指定的字体，例如 `DN Manuscript`、`kiddySans`、`Print Dashed` 和 `KaiTi`。其中 `DN Manuscript` 是 Educational Fontware, Inc. 的商业字体，`Lakesight` 仅限个人使用，二者均未随仓库提供，需要自行获取授权并安装。
- 运行现有 Python 脚本时需要 Python 2。脚本只使用 Python 标准库，但包含 Python 2 的 `print` 语法。
- 脚本调用 `mv` 和 `rm`，因此原始版本更适合 Linux、macOS、WSL 或 Git Bash 环境。

## 使用方法

### 直接编译 LaTeX 模板

安装所需字体和宏包后，在项目根目录运行：

```bash
xelatex LETTERhand.tex
xelatex ChinesePaper/tianzhige.tex
xelatex EnglishPaper/HandwritingPortrait.tex
```

含 `fontspec` 或 `xeCJK` 的模板应使用 XeLaTeX，不要使用传统的 `latex` 或 `pdflatex`。

### 生成单词练习纸

编辑 `words.txt` 后运行：

```bash
python2 GenHandwritting_word.py
```

脚本读取 `words.txt` 的最后一行，将单词排版到 `tmphand.tex`，并输出名称类似 `hwwordsYYYYMMDDHHMM.pdf` 的文件。

### 生成句子练习纸

编辑 `chapter-101.txt`，并将环境变量 `jTMP` 设置为临时输出目录：

```bash
export jTMP=/tmp
python2 GenHandwritting_sentence.py
```

脚本会在该目录生成临时 LaTeX 文件，并输出名称类似 `YYYYMMDDHHMMSSSentence.pdf` 的文件。

## 已知限制

- 两个 Python 文件是历史脚本，尚未适配 Python 3 和原生 Windows 命令。
- 部分字体名称必须与操作系统中安装后的名称完全一致。
- 个别 LaTeX 模板可能需要根据本机纸张大小、字体或 TeX 发行版调整。
- `font/` 和 `cursive/` 中的字体来自不同作者，使用和再分发前请分别检查随附许可或原始授权条款。

## 许可证

仓库中的原创脚本和模板采用 MIT 许可证，见 `LICENSE`。`font/` 和 `cursive/` 中的第三方字体不在 MIT 许可范围内，按各自随附的许可或作者条款使用；其中部分字体仅允许个人或教育用途，不得用于商业用途。

## Git 忽略策略

仓库保留源文件、字体和已有 PDF 示例；LaTeX 编译产生的辅助文件、Python 缓存、虚拟环境、编辑器配置及操作系统元数据不会纳入版本控制。

