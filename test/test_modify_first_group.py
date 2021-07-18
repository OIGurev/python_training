from model.group import Group

def test_modify_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="modif_group", header="modif_group header 1", footer="modif_group footer 1"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(name="new group name", header="new group header", footer="new group footer"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)