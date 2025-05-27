import sys
import re


def parse_block(lines):
    """時間情報を含むブロックを解析する"""
    if len(lines) < 2:
        return None
    match = re.match(r"(\d+:\d+:\d+,\d+)", lines[1])
    if match:
        return {"index": lines[0], "time": match.group(1), "lines": lines}
    return None


def read_blocks(filename):
    """ファイルを読み込み、ブロックを抽出する"""
    with open(filename, "r", encoding="GB2312") as file:
        content = file.read().strip()
    raw_blocks = content.split("\n\n")
    blocks = [
        parse_block(block.strip().split("\n"))
        for block in raw_blocks
        if parse_block(block.strip().split("\n"))
    ]
    print(raw_blocks[0].split("\n"))
    print(raw_blocks[1].strip().split("\n"))
    print(blocks)
    return blocks


def sort_blocks(blocks):
    """ブロックを時間の昇順にソートする"""
    return sorted(blocks, key=lambda x: x["time"])


def write_blocks(blocks, output_filename):
    """ソート済みのブロックをファイルに出力する"""
    with open(output_filename, "w", encoding="UTF-8") as file:
        file.write("\n\n".join("\n".join(block["lines"]) for block in blocks))


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("使用方法: python script.py <入力ファイル> <出力ファイル>")
        sys.exit(1)

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]
    blocks = read_blocks(input_filename)
    sorted_blocks = sort_blocks(blocks)
    write_blocks(sorted_blocks, output_filename)
    print(f"ソートされた結果を {output_filename} に保存しました。")
