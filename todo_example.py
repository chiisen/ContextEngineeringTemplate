# DEMO/todo_example.py
"""
本檔案示範如何撰寫一個簡單的 CLI Todo List 程式。
設計方式參考原始 README.md 的「Using Examples Effectively」與「Best Practices」章節。
"""

import argparse

class TodoItem:
    def __init__(self, title):
        self.title = title
        self.done = False

    def mark_done(self):
        self.done = True

class TodoList:
    def __init__(self):
        self.items = []

    def add(self, title):
        self.items.append(TodoItem(title))

    def complete(self, index):
        if 0 <= index < len(self.items):
            self.items[index].mark_done()
        else:
            print("⚠️ 無效的項目編號")

    def list(self):
        for idx, item in enumerate(self.items):
            status = "✔️" if item.done else "❌"
            print(f"{idx}. {item.title} [{status}]")

def main():
    parser = argparse.ArgumentParser(description="簡易 Todo List")
    subparsers = parser.add_subparsers(dest="command")

    parser_add = subparsers.add_parser("add")
    parser_add.add_argument("title", help="待辦事項標題")

    parser_done = subparsers.add_parser("done")
    parser_done.add_argument("index", type=int, help="完成的項目編號")

    parser_list = subparsers.add_parser("list")

    args = parser.parse_args()
    todo = TodoList()

    # 情境範例：假設啟動時預設有兩個待辦事項
    todo.add("買牛奶")
    todo.add("寫作業")

    if args.command == "add":
        todo.add(args.title)
        print(f"已新增：{args.title}")
    elif args.command == "done":
        todo.complete(args.index)
        print(f"已標記完成：{args.index}")
    elif args.command == "list":
        todo.list()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
