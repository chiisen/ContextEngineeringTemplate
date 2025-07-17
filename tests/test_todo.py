# DEMO/tests/test_todo.py
"""
本檔案示範如何為 Todo List 撰寫基本單元測試。
設計方式參考原始 README.md 的「Using Examples Effectively」與「Best Practices」章節。
"""

from todo_example import TodoList

def test_add_and_list():
    todo = TodoList()
    todo.add("學習 Context Engineering")
    assert len(todo.items) == 1
    assert todo.items[0].title == "學習 Context Engineering"
    assert not todo.items[0].done

def test_complete():
    todo = TodoList()
    todo.add("寫測試")
    todo.complete(0)
    assert todo.items[0].done

def test_invalid_complete(capsys):
    todo = TodoList()
    todo.add("測試錯誤處理")
    todo.complete(5)
    captured = capsys.readouterr()
    assert "無效的項目編號" in captured.out
