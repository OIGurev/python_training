import random
from model.group import Group

def test_delete_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test group", header="test_group header 1", footer="test_group footer 1"))

    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id)
    assert len(old_groups) - 1 == app.group.count()
    new_groups = db.get_group_list()
    old_groups.remove(group)
    assert old_groups == new_groups
    if check_ui:
        def clean(group):
            return Group(id=group.id, name=group.name.strip())
        new_groups = map(clean, db.get_group_list())
        #assert new_groups == sorted(app.group.get_group_list(), key=Group.id_or_max)
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)