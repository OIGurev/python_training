from model.group import Group

def test_modify_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="modif_group", header="modif_group header 1", footer="modif_group footer 1"))
    app.group.modify_first_group(Group(name="new group name", header="new group header", footer="new group footer"))