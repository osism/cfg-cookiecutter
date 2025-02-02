# This file is required as of OpenStack Kolla 2024.1.

# customer specific configuration

from django.utils.translation import ugettext_lazy as _

# SESSION_TIMEOUT = 7200
# OPENSTACK_ENABLE_PASSWORD_RETRIEVE = True

SHOW_KEYSTONE_V2_RC = False
USER_MENU_LINKS = [
    {
        "name": _("OpenStack clouds.yml File"),
        "icon_classes": [
            "fa-download",
        ],
        "url": "horizon:project:api_access:clouds.yaml",
        "external": False,
    },
    {
        "name": _("OpenStack RC File v3"),
        "icon_classes": [
            "fa-download",
        ],
        "url": "horizon:project:api_access:openrc",
        "external": False,
    },
]
