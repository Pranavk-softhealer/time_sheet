
{
    'name': "sh_timesheet_mgmt",

    'summary': "Timesheet",

    'description': """
Long description of module's purpose
    """,
    'sequence': 1,
    'author': "My Company",
    'website': "https://www.yourcompany.com",

    'category': 'Uncategorized',
    'version': '0.1',


    'depends': ['base_setup','web','mail','base','utm','sale'],

    "data": [
        "security/timesheet_security.xml",
        "security/ir.model.access.csv",
        "views/sh_tag_views.xml",
        "views/sh_task_views.xml",
        "views/sh_reason_views.xml",
        "views/sh_timesheet_views.xml",
        "views/sh_timesheet_mgmt_menus.xml",
        "reports/sh_timesheet_report.xml",
        "data/sh-timesheet_ir_cron.xml",
        "data/ir_sequnce_timesheet.xml",
    ],
    'demo': [
        
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}

