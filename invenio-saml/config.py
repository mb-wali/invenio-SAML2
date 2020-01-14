# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 TUGRAZ.
#
#
#
# more details.

"""configuration.

.. Path to certificate
SHIBBOLETH_SERVICE_PROVIDER_CERTIFICATE = './docker/nginx/sp.pem'

.. Path to certificate private key.
SHIBBOLETH_SERVICE_PROVIDER_PRIVATE_KEY = './docker/nginx/sp.key'

.. idp.crt "" 'this file will have the certificate you get from your IDENTITY_PROVIDERS'
SHIBBOLETH_IDP_CERT = './docker/shibbolethAuthenticator/idp.crt'


.. SERVICE_PROVIDER is your application in this case invenioRDM.
... strict
... debug
... entity_id  "this can be a unique URI that the IDENTITY_PROVIDERS knows which Service provider is asking for
    identity".

SHIBBOLETH_SERVICE_PROVIDER = dict(
    strict=True,
    debug=True,
    entity_id='https://mydomain/shibboleth'
)

.. IDENTITY_PROVIDERS is remote application which we redirect the user to login.
... idp = dict()  is name of your remote_app. this dictionary can have these values:
                ... entity_id ????
                ... title  you can give a title
                ... sso_url  is URL you get from your remote application to redirect the user.
                ... mapping = dict() is the values or fields you get back from your remote application:
                    see below for examples:

SHIBBOLETH_IDENTITY_PROVIDERS = dict(
    idp=dict(
        entity_id='https://identityprovider/idp/shibboleth',  # name of invenio something to get to know
        title='RDM remote application',
        sso_url='https://identityprovider/idp/profile/SAML2/Redirect/SSO',  # redirects to for authentication
        sso__Logout_url='https://sso.idp.com/slo/Logout', # Logout url
        mappings=dict(
            email='urn:oid:0.9.2342.19200300.100.1.3',
            full_name='urn:oid:2.5.4.3',
            user_unique_id='urn:oid:2.16.756.1.2.5.1.1.1',
            .
            .
            .

        )
    )
)

.. Number of seconds after which the state token expires.
SHIBBOLETH_STATE_EXPIRES = 300


"""
