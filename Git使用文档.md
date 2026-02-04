# Git 安装、配置与使用文档

## 📋 目录
- [Git 安装](#git-安装)
- [Git 配置](#git-配置)
- [Git 常用功能](#git-常用功能)
- [分支管理](#分支管理)
- [远程仓库操作](#远程仓库操作)
- [高级技巧](#高级技巧)
- [常见问题](#常见问题)

---

## 🔧 Git 安装

### Windows 系统

1. **下载安装包**
   - 访问 Git 官网：https://git-scm.com/download/win
   - 下载最新版本的 Git for Windows

2. **安装步骤**
   - 双击下载的 `.exe` 文件
   - 推荐选项：
     - ✅ Git Bash Here（右键菜单集成）
     - ✅ Git GUI Here
     - ✅ 选择 "Use Git from Git Bash only" 或 "Git from the command line and also from 3rd-party software"
     - ✅ Use the OpenSSL library
     - ✅ Checkout Windows-style, commit Unix-style line endings
     - ✅ Use MinTTY（默认终端）

3. **验证安装**
   ```bash
   git --version
   ```

### macOS 系统

**方法一：使用 Homebrew（推荐）**
```bash
brew install git
```

**方法二：使用 Xcode Command Line Tools**
```bash
xcode-select --install
```

**方法三：下载安装包**
- 访问：https://git-scm.com/download/mac

### Linux 系统

**Debian/Ubuntu**
```bash
sudo apt-get update
sudo apt-get install git
```

**Fedora/RHEL/CentOS**
```bash
sudo yum install git
# 或
sudo dnf install git
```

**Arch Linux**
```bash
sudo pacman -S git
```

---

## ⚙️ Git 配置

### 基础配置（必须）

```bash
# 设置用户名
git config --global user.name "你的名字"

# 设置邮箱
git config --global user.email "your.email@example.com"

# 查看配置
git config --list
git config user.name
git config user.email
```

### 常用配置

```bash
# 设置默认编辑器
git config --global core.editor "code --wait"  # VS Code
git config --global core.editor "vim"          # Vim
git config --global core.editor "notepad"      # 记事本

# 设置默认分支名称
git config --global init.defaultBranch main

# 启用颜色显示
git config --global color.ui auto

# 设置行尾转换（Windows）
git config --global core.autocrlf true

# 设置行尾转换（macOS/Linux）
git config --global core.autocrlf input

# 忽略文件权限变化
git config --global core.filemode false

# 设置别名
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.lg "log --oneline --graph --decorate --all"
```

### 配置级别

```bash
# --global: 全局配置（用户级别）
git config --global user.name "张三"

# --local: 仓库配置（仓库级别，默认）
git config --local user.name "李四"

# --system: 系统配置（所有用户）
git config --system user.name "王五"

# 查看特定级别的配置
git config --global --list
git config --local --list
```

---

## 📚 Git 常用功能

### 1. 创建仓库

```bash
# 初始化新仓库
git init

# 克隆远程仓库
git clone <url>
git clone https://github.com/user/repo.git
git clone git@github.com:user/repo.git

# 克隆到指定目录
git clone <url> <directory>
```

### 2. 文件状态管理

```bash
# 查看文件状态
git status

# 查看简洁状态
git status -s

# 添加文件到暂存区
git add <file>              # 添加单个文件
git add .                   # 添加所有文件
git add *.js                # 添加所有 .js 文件
git add src/                # 添加目录

# 从暂存区移除文件
git reset HEAD <file>
git restore --staged <file>  # 新命令

# 丢弃工作区的修改
git checkout -- <file>
git restore <file>          # 新命令
```

### 3. 提交更改

```bash
# 提交暂存区的文件
git commit -m "提交说明"

# 添加并提交（跳过 add）
git commit -am "提交说明"

# 修改最后一次提交
git commit --amend
git commit --amend -m "新的提交说明"

# 提交空变更（用于触发 CI）
git commit --allow-empty -m "Empty commit"
```

### 4. 查看历史

```bash
# 查看提交历史
git log

# 查看简洁日志
git log --oneline

# 查看图形化日志
git log --oneline --graph --decorate --all

# 查看最近 n 次提交
git log -n 5

# 查看某个文件的历史
git log <file>
git log -p <file>           # 显示差异

# 查看某人的提交
git log --author="张三"

# 查看某段时间的提交
git log --since="2024-01-01"
git log --after="2 weeks ago"
git log --before="2024-12-31"

# 搜索提交信息
git log --grep="关键词"
```

### 5. 查看差异

```bash
# 查看工作区与暂存区的差异
git diff

# 查看暂存区与最后一次提交的差异
git diff --staged
git diff --cached

# 查看两个提交之间的差异
git diff <commit1> <commit2>

# 查看某个文件的差异
git diff <file>

# 查看统计信息
git diff --stat
```

### 6. 撤销操作

```bash
# 撤销工作区的修改（未 add）
git restore <file>
git checkout -- <file>

# 撤销暂存区的文件（已 add 未 commit）
git restore --staged <file>
git reset HEAD <file>

# 撤销最后一次提交（保留更改）
git reset --soft HEAD^

# 撤销最后一次提交（不保留更改）
git reset --hard HEAD^

# 撤销到指定提交
git reset --hard <commit>

# 创建一个新提交来撤销指定提交
git revert <commit>
```

### 7. 文件操作

```bash
# 删除文件
git rm <file>

# 只从 Git 中删除，保留工作区文件
git rm --cached <file>

# 重命名文件
git mv <old> <new>

# 查看文件的每一行由谁修改
git blame <file>
```

### 8. 标签管理

```bash
# 查看所有标签
git tag

# 创建轻量标签
git tag v1.0.0

# 创建附注标签（推荐）
git tag -a v1.0.0 -m "版本 1.0.0"

# 给指定提交打标签
git tag -a v1.0.0 <commit> -m "版本 1.0.0"

# 查看标签信息
git show v1.0.0

# 删除本地标签
git tag -d v1.0.0

# 推送标签到远程
git push origin v1.0.0
git push origin --tags       # 推送所有标签

# 删除远程标签
git push origin :refs/tags/v1.0.0
git push origin --delete v1.0.0
```

---

## 🌿 分支管理

### 基本操作

```bash
# 查看分支
git branch                  # 查看本地分支
git branch -r              # 查看远程分支
git branch -a              # 查看所有分支
git branch -v              # 查看分支及最后一次提交

# 创建分支
git branch <branch-name>

# 切换分支
git checkout <branch-name>
git switch <branch-name>   # 新命令

# 创建并切换分支
git checkout -b <branch-name>
git switch -c <branch-name>

# 从远程分支创建本地分支
git checkout -b <local-branch> origin/<remote-branch>

# 删除分支
git branch -d <branch-name>        # 已合并的分支
git branch -D <branch-name>        # 强制删除

# 删除远程分支
git push origin --delete <branch-name>
git push origin :<branch-name>

# 重命名分支
git branch -m <old-name> <new-name>
git branch -m <new-name>           # 重命名当前分支
```

### 合并分支

```bash
# 合并指定分支到当前分支
git merge <branch-name>

# 禁用 Fast-forward 合并
git merge --no-ff <branch-name>

# 查看已合并的分支
git branch --merged

# 查看未合并的分支
git branch --no-merged

# 解决冲突
# 1. 编辑冲突文件
# 2. git add <file>
# 3. git commit

# 中止合并
git merge --abort
```

### 变基（Rebase）

```bash
# 将当前分支变基到指定分支
git rebase <branch-name>

# 交互式变基（整理提交历史）
git rebase -i HEAD~3

# 继续变基
git rebase --continue

# 跳过当前提交
git rebase --skip

# 中止变基
git rebase --abort
```

---

## 🌐 远程仓库操作

### 远程仓库管理

```bash
# 查看远程仓库
git remote
git remote -v              # 显示详细信息

# 添加远程仓库
git remote add <name> <url>
git remote add origin https://github.com/user/repo.git

# 修改远程仓库 URL
git remote set-url origin <new-url>

# 删除远程仓库
git remote remove <name>
git remote rm <name>

# 重命名远程仓库
git remote rename <old-name> <new-name>

# 查看远程仓库详细信息
git remote show origin
```

### 拉取和推送

```bash
# 拉取远程更改（不合并）
git fetch origin
git fetch origin <branch-name>
git fetch --all

# 拉取并合并
git pull origin <branch-name>
git pull                   # 拉取当前分支

# 推送到远程
git push origin <branch-name>
git push                   # 推送当前分支

# 强制推送（危险操作）
git push -f origin <branch-name>
git push --force-with-lease origin <branch-name>  # 更安全

# 推送所有分支
git push origin --all

# 设置上游分支
git push -u origin <branch-name>
git branch --set-upstream-to=origin/<branch-name>
```

### 跟踪分支

```bash
# 查看跟踪关系
git branch -vv

# 设置跟踪分支
git branch -u origin/<branch-name>

# 拉取远程分支并创建本地跟踪分支
git checkout --track origin/<branch-name>
```

---

## 🚀 高级技巧

### 1. Stash（暂存工作）

```bash
# 暂存当前工作
git stash
git stash save "描述信息"

# 查看暂存列表
git stash list

# 应用最近的暂存
git stash apply

# 应用并删除最近的暂存
git stash pop

# 应用指定的暂存
git stash apply stash@{2}

# 删除暂存
git stash drop stash@{0}

# 清空所有暂存
git stash clear

# 暂存包括未跟踪的文件
git stash -u
git stash --include-untracked
```

### 2. Cherry-pick（精选提交）

```bash
# 应用指定提交到当前分支
git cherry-pick <commit>

# 应用多个提交
git cherry-pick <commit1> <commit2>

# 应用一系列提交
git cherry-pick <commit1>..<commit2>

# 解决冲突后继续
git cherry-pick --continue

# 中止 cherry-pick
git cherry-pick --abort
```

### 3. 子模块（Submodule）

```bash
# 添加子模块
git submodule add <url> <path>

# 初始化子模块
git submodule init

# 更新子模块
git submodule update

# 克隆包含子模块的仓库
git clone --recursive <url>

# 拉取子模块更新
git submodule update --remote
```

### 4. 搜索和查找

```bash
# 搜索内容
git grep "关键词"
git grep -n "关键词"       # 显示行号

# 搜索提交历史中的内容
git log -S "关键词"
git log -G "正则表达式"

# 查找引入 bug 的提交
git bisect start
git bisect bad              # 当前版本有问题
git bisect good <commit>    # 某个版本是好的
# Git 会自动二分查找
git bisect reset            # 结束查找
```

### 5. 清理仓库

```bash
# 清理未跟踪的文件（预览）
git clean -n

# 清理未跟踪的文件
git clean -f

# 清理未跟踪的文件和目录
git clean -fd

# 清理忽略的文件
git clean -fX

# 清理所有未跟踪和忽略的文件
git clean -fdx
```

### 6. 高级日志

```bash
# 美化日志输出
git log --pretty=format:"%h - %an, %ar : %s"

# 自定义格式
git log --pretty=format:"%C(yellow)%h%Creset %C(blue)%ad%Creset | %s %C(green)(%an)%Creset" --date=short

# 查看文件变更统计
git log --stat

# 查看每次提交的差异
git log -p

# 查看分支合并图
git log --graph --oneline --all
```

---

## ❓ 常见问题

### 1. 忽略文件（.gitignore）

创建 `.gitignore` 文件：
```
# 忽略所有 .log 文件
*.log

# 忽略 node_modules 目录
node_modules/

# 忽略所有 .DS_Store 文件
.DS_Store

# 忽略 build 目录
/build
/dist

# 忽略环境配置文件
.env
.env.local

# 但不忽略特定文件
!important.log
```

### 2. 修改远程仓库地址

```bash
# HTTPS 改为 SSH
git remote set-url origin git@github.com:user/repo.git

# SSH 改为 HTTPS
git remote set-url origin https://github.com/user/repo.git
```

### 3. 解决合并冲突

```bash
# 1. 查看冲突文件
git status

# 2. 编辑冲突文件，删除冲突标记：
#    <<<<<<< HEAD
#    你的更改
#    =======
#    他人的更改
#    >>>>>>> branch-name

# 3. 标记为已解决
git add <file>

# 4. 完成合并
git commit
```

### 4. 回退到之前的版本

```bash
# 查看提交历史
git log --oneline

# 回退到指定版本（保留更改）
git reset --soft <commit>

# 回退到指定版本（不保留更改）
git reset --hard <commit>

# 回退后推送到远程（需要强制）
git push -f origin <branch-name>
```

### 5. 配置 SSH 密钥

```bash
# 1. 生成 SSH 密钥
ssh-keygen -t rsa -b 4096 -C "your.email@example.com"

# 2. 查看公钥
cat ~/.ssh/id_rsa.pub

# 3. 复制公钥到 GitHub/GitLab
# Settings -> SSH Keys -> Add SSH Key

# 4. 测试连接
ssh -T git@github.com
```

### 6. 大文件处理

```bash
# 安装 Git LFS
git lfs install

# 跟踪大文件
git lfs track "*.psd"
git lfs track "*.zip"

# 提交 .gitattributes
git add .gitattributes
git commit -m "Add Git LFS tracking"
```

### 7. 修改历史提交的用户信息

```bash
# 修改最近一次提交
git commit --amend --author="新名字 <new.email@example.com>"

# 修改多个提交（交互式变基）
git rebase -i HEAD~3
# 将要修改的提交前的 pick 改为 edit
# 然后执行：
git commit --amend --author="新名字 <new.email@example.com>"
git rebase --continue
```

---

## 📖 推荐工作流

### Git Flow 工作流

```
master/main     - 主分支（生产环境）
  └─ develop    - 开发分支
      ├─ feature/*  - 功能分支
      ├─ release/*  - 预发布分支
      └─ hotfix/*   - 热修复分支
```

### GitHub Flow 工作流（简化版）

```
1. 从 main 创建功能分支
2. 在功能分支上开发
3. 提交 Pull Request
4. 代码审查
5. 合并到 main
6. 部署
```

---

## 🔗 有用的资源

- **官方文档**: https://git-scm.com/doc
- **Git 教程**: https://www.atlassian.com/git/tutorials
- **GitHub 文档**: https://docs.github.com
- **交互式学习**: https://learngitbranching.js.org/
- **Git Cheat Sheet**: https://education.github.com/git-cheat-sheet-education.pdf

---

## 💡 最佳实践

1. **频繁提交**：保持提交的原子性，每次只做一件事
2. **有意义的提交信息**：清晰描述本次提交的目的
3. **使用分支**：不要直接在 main/master 上开发
4. **定期拉取**：保持本地代码与远程同步
5. **代码审查**：使用 Pull Request 进行代码审查
6. **保护主分支**：设置分支保护规则
7. **使用 .gitignore**：避免提交不必要的文件
8. **备份重要工作**：在进行危险操作前创建备份分支

---

**文档版本**: v1.0  
**最后更新**: 2026-02-04  
**维护者**: GitHub Copilot
