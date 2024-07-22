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

{%- if cookiecutter.with_keycloak|int %}
LOGOUT_URL = "https://keycloak.testbed.osism.xyz/auth/realms/osism/protocol/openid-connect/logout/?client_id=keystone&post_logout_redirect_uri=https%3A%2F%2Fapi.testbed.osism.xyz%3A5000%2Fredirect_uri%3Flogout%3Dhttps%3A%2F%2Fapi.testbed.osism.xyz%3A5000%2Flogout"

WEBSSO_ENABLED = False

WEBSSO_KEYSTONE_URL = "https://api.testbed.osism.xyz:5000/v3"
WEBSSO_CHOICES = (
    ("credentials", "Keystone Credentials"),
    ("keycloak", "Authenticate via Keycloak"),
)

WEBSSO_IDP_MAPPING = {
    "keycloak": ("keycloak", "openid"),
}
{%- endif %}
