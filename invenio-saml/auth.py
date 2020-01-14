# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 TUGRAZ.
#

"""Authentication utils."""

from flask import current_app, url_for
from onelogin.saml2.auth import OneLogin_Saml2_Auth


def init_saml_auth(req, remote_app):
    """
    Init SAML authentication for remote application.

    :param req: (flask.request) Prepared flask request.
    :param remote: (str) Identity provider key.
    :returns: (onelogin.saml2.auth) Auth object.
    """
    # Retreive configuration for identity provider and service provider

    idp_config = get_identity_provider_configuration(remote_app)
    sp_config = current_app.config.get('SHIBBOLETH_SERVICE_PROVIDER')
    idp_crt = current_app.config.get('SHIBBOLETH_IDP_CERT')

    # Check configuration data
    if 'strict' not in sp_config:
        sp_config['strict'] = True

    if 'debug' not in sp_config:
        sp_config['debug'] = False

    if 'entity_id' not in sp_config:
        raise Exception('"entityId" for service provider not configured')

    if 'x509cert' not in sp_config:
        raise Exception('"x509cert" path for service provider not configured')

    if 'private_key' not in sp_config:
        raise Exception('"private_key" path for service provider not configured')

    # Read certificates
    with open(sp_config['x509cert'], 'r') as content_file:
        x509cert = content_file.read()

    with open(sp_config['private_key'], 'r') as content_file:
        private_key = content_file.read()

    with open(
            idp_crt.format(
                remote_app=remote_app), 'r') as content_file:
        idp_cert = content_file.read()

    # Create auth object with settings below
    settings = {
        'strict': sp_config['strict'],
        'debug': sp_config['debug'],
        'sp': {
            'entityId': sp_config['entity_id'],
            'assertionConsumerService': {
                'url':
                    url_for('shibboleth_authenticator.authorized',
                            remote_app=remote_app,
                            _external=True),
                'binding':
                    'urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST'
            },

            "NameIDFormat": "urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified",
            'x509cert': x509cert,
            'privateKey': private_key
        },
        'idp': {
            'entityId': idp_config['entity_id'],
            'singleSignOnService': {
                'url': idp_config['sso_url'],
                'binding': 'urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect'
            },
            "singleLogoutService": {

                "url": idp_config['sso__Logout_url'],
                "binding": "urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect"
            },
            'x509cert': idp_cert
        },

        "security": {
            "nameIdEncrypted": False,
            "authnRequestsSigned": False,
            "logoutRequestSigned": False,
            "logoutResponseSigned": False,
            "signMetadata": False,
            "wantMessagesSigned": True,
            "wantAssertionsSigned": False,
            "wantNameIdEncrypted": False,
            "requestedAuthnContext": False
        }
    }

    print('SETTINGS: ', settings)
    auth = OneLogin_Saml2_Auth(req, settings)
    return auth


def get_identity_provider_configuration(remote_app):
    """Get the configuration for identity provider key.

    :param remote_app: (str) Identity provider key.
    :returns: (dict) A dictionary with the identity provider configuration.
    """
    if remote_app not in current_app.config.get(
            'SHIBBOLETH_IDENTITY_PROVIDERS'):
        raise Exception(
            'Identity provider not found for "{remote_app}"'.format(
                remote_app=remote_app))

    return current_app.config.get('SHIBBOLETH_IDENTITY_PROVIDERS')[remote_app]
