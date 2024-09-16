from django.core.management.base import BaseCommand
from django.db import connection

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        sql = '''
            TRUNCATE TABLE user_module_usermodule CASCADE;
            TRUNCATE TABLE module_group_module CASCADE;
            TRUNCATE TABLE module_group_modulegroup CASCADE;

            INSERT INTO module_group_modulegroup (id, group_name) VALUES
            (1, 'Training Management'),
            (2, 'User Management'),
            (3, 'Assessment Management');

            INSERT INTO module_group_module (id, module_name, module_url, icon, module_group_id) VALUES
            (1, 'Subject', 'subject:subject_list', 'fas fa-book', 1),
            (2, 'Category', 'category:category_list', 'fas fa-tags', 1),
            (3, 'Training Program', 'training_program:training_program_list', 'fas fa-calendar-alt', 1),
            (4, 'User', 'user:user_list', 'fas fa-user', 2),
            (5, 'Role', 'role:role_list', 'fas fa-briefcase', 2),
            (6, 'Module', 'module_group:module_list', 'fas fa-cogs', 2),
            (7, 'Module Group', 'module_group:module_group_list', 'fas fa-folder', 2),
            (8, 'User Module', 'user_module:user_module_list', 'fas fa-user-tag', 2),
            (9, 'Quiz', 'question:question_list', 'fas fa-user-tag', 3);
        '''
        with connection.cursor() as cursor:
            cursor.execute(sql)
