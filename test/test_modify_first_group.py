from model.group import Group

def test_modify_first_group(app):
    app.group.go_to_modify_page()
    app.group.modify_first_group(Group(name="new group name", header="new group header", footer="new group footer"))