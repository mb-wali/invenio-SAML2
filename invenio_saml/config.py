# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 TUGRAZ.
#
# more details.

""" Invenio-SAML configuration.

.. Path to sp.crt (X.509 cert) Public cert for SERVICE_PROVIDER
SHIBBOLETH_SERVICE_PROVIDER_CERTIFICATE = './saml/sp.crt'

.. Path to sp.key (Private key) Private key for SERVICE_PROVIDER.
SHIBBOLETH_SERVICE_PROVIDER_PRIVATE_KEY = './saml/sp.key'

.. Path to idp.crt Public cert for IDP IDENTITY_PROVIDER.
SHIBBOLETH_IDP_CERT = './saml/idp.crt'

.. Number of seconds after which the state token expires.
SHIBBOLETH_STATE_EXPIRES = 300



.. SERVICE_PROVIDER Is your application/Service in this case invenio.
    * strict MUST be set as True. Otherwise your environment is not secure and will be exposed to attacks.
    * debug set this True for debugging purposes.
    * entity_id is a unique self signed URI, with this the IDENTITY_PROVIDERS knows which SERVICES_PROVIDER is asking for identity.

.. EXAMPLE:

SHIBBOLETH_SERVICE_PROVIDER = dict(
    strict=True,
    debug=True,
    entity_id='https://mydomain/shibboleth'
)


.. IDENTITY_PROVIDERS Is remote application which we redirect the user to login or to identify.
    * idp = dict() idp is your remote_app name, which has these below fields:
        * entity_id Is a unique URI from your IDENTITY_PROVIDERS.
        * title Title for your idp [OPTIONAL]
        * sso_url Is the URL to redirect the user. URL for IDENTITY_PROVIDERS.
        * sso__Logout_url is the URL to redirect for logout.
        * mappings=dict() Is the fields/values that IDENTITY_PROVIDERS sends back after successful identity of user.
            * email
            * full_name
            * user_unique_id

.. EXAMPLE:

SHIBBOLETH_IDENTITY_PROVIDERS = dict(
    idp=dict(
        entity_id='https://identityprovider/idp/shibboleth',
        title='Mydomain remote app',
        sso_url='https://identityprovider/idp/profile/SAML2/Redirect/SSO',
        sso__Logout_url='https://sso.identityprovider.com/slo/Logout',
        mappings=dict(
            email='urn:oid:0.9.2342.19200300.100.1.3',
            full_name='urn:oid:2.5.4.3',
            user_unique_id='urn:oid:2.16.756.1.2.5.1.1.1',
        )
    )
)

.. PS: SHIBBOLETH_IDENTITY_PROVIDERS can have more than one <remote_app>.

.. EXAMPLE

    SHIBBOLETH_IDENTITY_PROVIDERS = dict(
        idp1=dict(
            # Configuration values for idp1
        ),
        idp2=dict(
            # Configuration values for idp2
        )
    )

"""

SHIBBOLETH_SERVICE_PROVIDER_CERTIFICATE = ''
"""Path to certificate."""

SHIBBOLETH_SERVICE_PROVIDER_PRIVATE_KEY = ''
"""Path to certificate private key."""

SHIBBOLETH_IDP_CERT = ''
"""Path to idp.crt"""

SHIBBOLETH_STATE_EXPIRES = 300
"""Number of seconds after which the state token expires."""

SHIBBOLETH_SERVICE_PROVIDER = {}
"""Configuration of service provider."""

SHIBBOLETH_IDENTITY_PROVIDERS = {}
"""Configuration of identity providers."""
