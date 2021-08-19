from random import randrange
from model.group import Group
import allure

def test_modify_group(app, db, check_ui):
    with allure.step('Given a non-empty group list'):
        if len(db.get_group_list()) == 0:
            app.group.create(Group(name="modif_group", header="modif_group header 1", footer="modif_group footer 1"))
        old_groups = db.get_group_list()
    with allure.step('Given a random group from the list'):
        index = randrange(len(old_groups))
    group = Group(name="new group name", header="new group header", footer="new group footer")
    group.id = old_groups[index].id
    with allure.step('When I edit the group %s from the list' % group):
        app.group.modify_group_by_id(group.id, group)
    with allure.step('Then the new list of groups is equal to the old list with the replacement of the edited group'):
        assert len(old_groups) == app.group.count()
        new_groups = db.get_group_list()
        old_groups[index] = group
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
        if check_ui:
            def clean(group):
                return Group(id=group.id, name=group.name.strip())
            new_groups = map(clean, db.get_group_list())
            assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)