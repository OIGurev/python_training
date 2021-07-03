from model.group import Group


def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test group", header="test_group header 1", footer="test_group footer 1"))
    app.group.delete_first_group()