# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 TUGRAZ.
#

"""Handlers for shibboleth endpoints."""

from __future__ import absolute_import, print_function

from flask import current_app, redirect, session
from flask_login import current_user, logout_user
from invenio_db import db
from invenio_oauthclient.errors import AlreadyLinkedError
from invenio_oauthclient.handlers import get_session_next_url, \
    oauth_error_handler, token_session_key
from invenio_oauthclient.utils import create_csrf_disabled_registrationform, \
    fill_form, oauth_authenticate, oauth_get_user, oauth_link_external_id, \
    oauth_register
from werkzeug.local import LocalProxy

from .utils import get_account_info

_security = LocalProxy(lambda: current_app.extensions['security'])

_datastore = LocalProxy(lambda: _security.datastore)


@oauth_error_handler
def authorized_signup_handler(auth, remote=None, *args, **kwargs):
    """
    Handle sign-in/up functionality.

    Checks if user is already registered. If not registered, the function
    registers a new user and authenticates the new user. If there already
    exists a user object in the database, the user is only authenticated and
    logged in.

    :param auth: (onelogin.saml2.auth) Auth object.
    :param remote: (str) Identity provider key.
    :returns: Redirect response.
    """

    # Remove any previously stored auto register session key
    session.pop(token_session_key(remote) + '_autoregister', None)


    # Sign-in/up user
    # ---------------
    if current_user.is_authenticated:
        logout_user()

    account_info = get_account_info(auth.get_attributes(), remote)

    user = oauth_get_user(remote, account_info=account_info)
    if user is None:
        # Auto sign-up if user not found
        form = create_csrf_disabled_registrationform()

        # Fill form with user data
        form = fill_form(form, account_info['user'])

        # Try to register user
        user = oauth_register(form)

        # if registration fails ...
        if user is None:
            return current_app.login_manager.unauthorized()

    # Authenticate user
    if not oauth_authenticate(remote, user, require_existing_link=False):
        return current_app.login_manager.unauthorized()

    # create external id link
    try:
        oauth_link_external_id(
            user, dict(id=account_info['external_id'], method=remote))
        db.session.commit()
    except AlreadyLinkedError:
        pass

    # Redirect to next
    next_url = get_session_next_url(remote)
    if next_url:
        return redirect(next_url)

    return redirect(current_app.config['SECURITY_POST_LOGIN_VIEW'])
