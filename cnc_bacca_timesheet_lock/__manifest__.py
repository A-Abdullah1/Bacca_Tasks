# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Bacca Timesheet',
    'version': '1.0.',
    'category': '',
    'sequence': -100,
    'description': """ Adding cond when the task time exceeds the timesheet locks  """,
    'depends': ['project', 'hr_timesheet', 'timesheet_grid'],
    'data': [
        'security/ir.model.access.csv',
        'views/task_view.xml',
        'views/exceeded_tasks_view.xml',

    ],
    'auto_install': False,
    'application': True,
    'license': 'LGPL-3',
}
