from random import randrange
from model.group import Group

def test_modify_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="modif_group", header="modif_group header 1", footer="modif_group footer 1"))

    old_groups = db.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="new group name", header="new group header", footer="new group footer")
    group.id = old_groups[index].id
    app.group.modify_group_by_id(group.id, group)
    assert len(old_groups) == app.group.count()
    new_groups = db.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        def clean(group):
            return Group(id=group.id, name=group.name.strip())
        new_groups = map(clean, db.get_group_list())
        #assert new_groups == sorted(app.group.get_group_list(), key=Group.id_or_max)
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)