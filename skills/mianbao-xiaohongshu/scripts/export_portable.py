#!/usr/bin/env python3
"""Export the local skill as a portable Markdown snapshot and ZIP, without network access."""
from __future__ import annotations
import argparse
from datetime import date
from pathlib import Path
import re
import tempfile
import zipfile

ROOT = Path(__file__).resolve().parents[1]
TEXT_ORDER = (
    'SKILL.md',
    'memory/profile.md',
    'memory/current.md',
    'memory/decisions.md',
    'references/voice.md',
    'references/return-post.md',
    'references/creators.md',
    'references/continuity.md',
)
PACKAGE_FILES = TEXT_ORDER + ('agents/openai.yaml', 'scripts/export_portable.py')

def write_atomic(path: Path, content: str) -> None:
    with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', dir=path.parent,
                                     prefix=path.name + '.', suffix='.tmp', delete=False) as f:
        f.write(content)
        tmp = Path(f.name)
    tmp.replace(path)

def flatten_links(text: str, relative_file: str) -> str:
    def replace(match: re.Match[str]) -> str:
        label, target = match.groups()
        if target.startswith(('https://', 'http://', '#')):
            return match.group(0)
        linked = (ROOT / relative_file).parent / target.split('#', 1)[0]
        relative = linked.resolve().relative_to(ROOT).as_posix()
        return f'{label}（见本文件中的「{relative}」部分）'
    return re.sub(r'\[([^\]]+)\]\(([^)]+)\)', replace, text)

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir', type=Path, required=True)
    parser.add_argument('--as-of', type=date.fromisoformat, required=True,
                        help='Client/user date, YYYY-MM-DD; this does not refresh stored facts.')
    args = parser.parse_args()
    out = args.output_dir.expanduser().resolve()
    if out == ROOT or ROOT in out.parents:
        parser.error('Export outside the skill directory so exports do not become live memory.')
    for relative in PACKAGE_FILES:
        if not (ROOT / relative).is_file():
            parser.error(f'Missing required file: {relative}')
    out.mkdir(parents=True, exist_ok=True)
    opening = f'''# 面包账号记忆：跨平台读取快照

导出日期：{args.as_of.isoformat()}（按用户日期传入）。事实各自的记录时点见对应章节，导出日期不代表重新核验。

这是一份包含协作方法、账号记忆、文风与成稿案例的自包含文件。用于上传到其他可读取Markdown的聊天平台。它不是自动同步服务，不包含照片、登录凭据或已核验的发布后数据。

## 开始使用

请先读取本文件中SKILL.md、memory/profile.md和memory/current.md部分，按需读其他部分。遵循我的最新消息，区分事实、计划和建议，保留原文的细节、口气和幽默。用你知道的最新进度接着聊；不要把计划发布写成已发布，也不要自行继续部署GitHub或MCP。

如果所在平台没有文件系统，下面的相对路径代表本文件的章节，不需要额外联网取文件。不能回写时，在新事实或偏好出现后给出「记忆增量：日期、内容、状态、取代的旧条目」，明确尚未保存，让用户保留。

这是导出快照。原技能包中的memory/是主记录；迁移后产生的新记忆需要保存或合并，换平台前应重新导出或带上增量。
'''
    parts = [opening]
    for relative in TEXT_ORDER:
        content = (ROOT / relative).read_text(encoding='utf-8')
        if relative == 'SKILL.md' and content.startswith('---\n'):
            content = content.split('---\n', 2)[-1]
        parts.append(f'\n\n---\n\n# 文件：{relative}\n\n' + flatten_links(content, relative))
    md = out / '面包账号记忆-跨平台.md'
    write_atomic(md, ''.join(parts))
    archive = out / 'mianbao-xiaohongshu.zip'
    with tempfile.NamedTemporaryFile(dir=out, prefix=archive.name + '.', suffix='.tmp', delete=False) as f:
        tmp = Path(f.name)
    with zipfile.ZipFile(tmp, 'w', compression=zipfile.ZIP_DEFLATED) as z:
        for relative in PACKAGE_FILES:
            z.write(ROOT / relative, f'{ROOT.name}/{relative}')
    tmp.replace(archive)
    print(md)
    print(archive)
    print(f'Packaged {len(PACKAGE_FILES)} files; snapshot is not automatic synchronization.')

if __name__ == '__main__':
    main()
