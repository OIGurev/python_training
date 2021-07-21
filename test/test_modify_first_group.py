from random import randrange
from model.group import Group

def test_modify_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="modif_group", header="modif_group header 1", footer="modif_group footer 1"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="new group name", header="new group header", footer="new group footer")
    group.id = old_groups[index].id
    app.group.modify_group_by_index(index, group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == app.group.count()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)